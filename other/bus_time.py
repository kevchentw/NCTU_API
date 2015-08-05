import requests
from lxml import etree
from psql import Postgres
import time

def get_raw():
    r = requests.get("http://117.56.78.38/sipa/busAzimuth.xml").text.encode()
    root = etree.fromstring(r)
    data = []
    for i in root:
        item = dict(i.items())
        data.append(item)
    return data


while 1:
    p = Postgres()
    p.connect("bus")
    data = get_raw()
    for d in data:
        p.add_bus_data(d)
    p.disconnect()
    time.sleep(10)
