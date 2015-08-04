import psycopg2
from datetime import datetime

class Postgres:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(database="NCTU_Lib", user="kevchentw", password="", host="140.113.244.244")
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

    def disconnect(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


def test():
    d = {}
    d['title'] = "Joining processes : introduction to brazing and diffusion bonding /"
    d['author'] = "Nicholas, M. G."
    d['year'] = "1998"
    d['class_no'] = "TS718 N 53 1998"
    d['isbn'] = "0412793601"
    d['amount'] = "1"
    d['url_detail'] = "http://webpac.lib.nctu.edu.tw/F/7MRPB6XB3264XRMC3FGBRKSY9G11TXTNLV7A757QYFYYB7VR5J-38998?func=full-set-set&set_number=004889&set_entry=000001&format=999"
    d['url_holding'] = "http://webpac.lib.nctu.edu.tw/F/7MRPB6XB3264XRMC3FGBRKSY9G11TXTNLV7A757QYFYYB7VR5J-38999?func=item-global&doc_library=TOP01&doc_number=000100101&year=&volume=&sub_library=KL"
    d['format'] = "一般書"
    d['sysnum'] = "1234567"
    p = Postgres()
    p.connect()
    p.add_book(d)
    p.disconnect()

# test()

