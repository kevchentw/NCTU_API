from bs4 import BeautifulSoup
import requests
from datetime import datetime
from Mail.models import Mail

DORM = ["086", "087", "088", "089", "090", "091", "092", "093", "094", "095", "097"]


def get_url(dorm_id):
    url = "http://mailsys.nctu.edu.tw/mailnotify/main.asp?dorm="
    return url + dorm_id


def delete_all_mail():
    Mail.objects.all().delete()


def insert_mail(mails):
    for _mail in mails:
        Mail(name=_mail['name'], date=_mail['date'], mail_id=_mail['id'], mail_type=_mail['type']).save()


def get_data():
    mail_data = []
    for dorm in DORM:
        r = requests.get(get_url(dorm))
        r.encoding = 'big5'
        raw = r.text
        soup = BeautifulSoup(raw)
        mail_list = soup.find_all("tr")
        for mail in mail_list[1:]:
            d = {}
            _m = mail.find_all("td")
            d["id"] = _m[0].string
            d["name"] = _m[1].string
            d["date"] = datetime.strptime(_m[2].string, '%Y/%m/%d')
            d["type"] = _m[3].string.strip()
            mail_data.append(d)
    # print(mail_data)
    return mail_data


def main():
    get_data()
    delete_all_mail()
    insert_mail(get_data())
