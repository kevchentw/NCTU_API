import psycopg2
from datetime import datetime

class Postgres:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self, db="NCTU_Lib"):
        self.conn = psycopg2.connect(database=db, user="kevchentw", password="", host="140.113.244.244")
        self.cur = self.conn.cursor()

    def get_all(self):
        self.cur.execute("SELECT * FROM books;")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def add_book(self, d):
        d['created'] = datetime.now().isoformat()
        d['lastmodified'] = datetime.now().isoformat()
        try:
            self.cur.execute("INSERT INTO books (title, author, year, class_no, isbn, amount, created, lastmodified, url_detail, url_holding, format, sysnum)\
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                             (d['title'], d['author'], d['year'], d['class_no'], d['isbn'],
                              d['amount'], d['created'], d['lastmodified'], d['url_detail'], d['url_holding'], d['format'], d['sysnum']))
        except psycopg2.IntegrityError:
            print("Book Already Exist")

    def add_bus_data(self, d):
        d['created'] = datetime.now().isoformat()
        if d['OnOff'] == "ON":
            d['OnOff'] = True
        else:
            d['OnOff'] = False
        try:
            self.cur.execute("INSERT INTO raw (lp, driver_name, speed, update_time, status, lat, lng, color_id, azimuth, created)\
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                             (d['LP'], d['DriverName'], d['Speed'], d['Updatetime'], d['OnOff'], d['Lat'], d['Lng'],
                              d['ColorId'], d['Azimuth'], d['created']))
        except:
            print("Unknown Err")

    def disconnect(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


def test():
    d = {}
    p = Postgres()
    p.connect()
    p.add_book(d)
    p.disconnect()

# test()

