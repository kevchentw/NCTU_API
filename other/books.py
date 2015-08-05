from bs4 import BeautifulSoup as bs4
import requests
from psql import Postgres
import time
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.35'}

t = time.time()
def get(sysnum):
    url = "http://webpac.lib.nctu.edu.tw/F?func=find-b&find_code=SYS&request=" + str(sysnum)
    raw_data = requests.get(url)
    raw_data.encoding = 'utf-8'
    soup = bs4(raw_data.text, "html.parser")
    try:
        item = soup.find_all("table")[9].find_all("tr")[1].find_all("td", class_="td1")
    except IndexError:
        global t
        print(time.time()-t)
        t = time.time()
        print(raw_data.text)
        print("No Data, Retry in 10s...")
        time.sleep(10)
        return get(sysnum)
    if not item:
        return None
    data={}
    data["sysnum"] = str(sysnum)
    try:
        data["title"] = item[2].text.split("\n")[4][21:-3]
    except:
        data["title"] = ""
    if data["title"] == "" or data["title"] == "<BR>":
        return None
    try:
        data["author"] = item[3].text.replace('\xa0', ' ').strip()
    except:
        data["author"] = ""
    try:
        data["year"] = item[4].text.split("\n")[3][15:-3]
    except:
        data["year"] = 0
    if data["year"] == "<BR>" or not data["year"].isdigit():
        data["year"] = 0
    try:
        data["class_no"] = item[6].text.replace('\xa0', ' ').strip()
    except:
        data["class_no"] = ""
    isbn = item[9].text.split("\n")[3][17:].split("(")[0].strip()
    if isbn.isdigit():
        data["isbn"] = isbn
    else:
        data["isbn"] = 0
    try:
        data["amount"] = item[5].text.split("/")[0].split("(")[1].lstrip()
    except:
        data["amount"] = -1
    data["url_detail"] = item[2].text.split("\n")[3][28:-9]
    try:
        data["url_holding"] = item[5].find("a")["href"]
    except:
        data["url_holding"] = ""
    data["format"] = item[7].text.split("\n")[3][22:-3]
    print(data)
    return data

for i in range(101564, 200000):
    print(i)
    time.sleep(0.5)
    d = get(i)
    if d:
        p = Postgres()
        p.connect()
        p.add_book(d)
        p.disconnect()

