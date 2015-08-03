from bs4 import BeautifulSoup
import requests
from datetime import datetime

DORM = ["086", "087", "088", "089", "090", "091", "092", "093", "094", "095", "097"]


def get_url(dorm_id):
    url = "http://mailsys.nctu.edu.tw/mailnotify/main.asp?dorm="
    return url + dorm_id

if __name__ == '__main__':
    mail_data = []
    for dorm in DORM:
        r = requests.get(get_url(dorm))
        r.encoding = 'big5'
        raw = r.text
        soup = BeautifulSoup(raw)
        mail_list = soup.find_all("tr")
        for mail in mail_list[1:]:
            d = {}
            m = mail.find_all("td")
            d["id"] = m[0].string
            d["name"] = m[1].string
            d["date"] = datetime.strptime(m[2].string, '%Y/%m/%d')
            d["type"] = m[3].string.strip()
            mail_data.append(d)
    print(mail_data)

