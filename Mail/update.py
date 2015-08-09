from bs4 import BeautifulSoup
import requests
from datetime import datetime
from Mail.models import Mail
from django_cron import CronJobBase, Schedule


DORM = ["086", "087", "088", "089", "090", "091", "092", "093", "094", "095", "097"]
DORM_NAME = ["七舍", "八舍", "九舍", "十舍", "十一舍", "十二舍", "十三舍", "竹軒", "女二舍", "研一舍", "研二舍"]


def get_url(dorm_id):
    url = "http://mailsys.nctu.edu.tw/mailnotify/main.asp?dorm="
    return url + dorm_id


def delete_all_mail():
    Mail.objects.all().delete()


def insert_mail(mails):
    for _mail in mails:
        Mail(name=_mail['name'], date=_mail['date'], mail_id=_mail['id'], mail_type=_mail['type'], dorm=_mail['dorm']).save()


def get_data():
    mail_data = []
    for idx, dorm in enumerate(DORM):
        r = requests.get(get_url(dorm))
        r.encoding = 'big5'
        raw = r.text
        soup = BeautifulSoup(raw, "html.parser")
        mail_list = soup.find_all("tr")
        for mail in mail_list[1:]:
            d = {}
            _m = mail.find_all("td")
            d["id"] = _m[0].string
            d["name"] = _m[1].string
            d["date"] = datetime.strptime(_m[2].string, '%Y/%m/%d')
            d["type"] = _m[3].string.strip()
            d["dorm"] = DORM_NAME[idx]
            mail_data.append(d)
    return mail_data


def main():
    print("Start update mail data")
    get_data()
    delete_all_mail()
    insert_mail(get_data())
    print("END")

class CronJob(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'Mail.cron_job'

    def do(self):
        main()
