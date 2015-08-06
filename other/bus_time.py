import requests
from lxml import etree
from other.psql import Postgres
import time
from datetime import datetime

def get_raw():
    r = requests.get("http://117.56.78.38/sipa/busAzimuth.xml").text.encode()
    root = etree.fromstring(r)
    data = []
    for i in root:
        item = dict(i.items())
        data.append(item)
    return data

def add_bus_data(d):
        d['created'] = datetime.now().isoformat()
        if d['OnOff'] == "ON":
            d['OnOff'] = "1"
        else:
            d['OnOff'] = "0"
        if not d['Lat']:
            d['Lat'] = 0
        if not d['Lng']:
            d['Lng'] = 0
        psql = Postgres()
        psql.connect('bus')
        err = psql.execute(psql.create_insert_sql(d, 'raw'))
        if err:
            print(err)
        else:
            print("Insert Success")
        psql.disconnect()

while 1:
    data = get_raw()
    for d in data:
        add_bus_data(d)
    time.sleep(10)
