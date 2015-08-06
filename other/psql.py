import psycopg2
from datetime import datetime
import sys


class Postgres:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self, db="NCTU_Lib"):
        self.conn = psycopg2.connect(database=db, user="kevchentw", password="", host="140.113.244.244")
        self.cur = self.conn.cursor()

    def get_all(self, table):
        self.cur.execute("SELECT * FROM %s;" % table)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def delete_all(self, table):
        self.cur.execute("DELETE FROM %s;" % table)

    def execute(self, sql):
        err = None
        try:
            self.cur.execute(sql)
        except:
            err = str(sys.exc_info()[0])
            print("psql err: " + err)
        return err

    def create_insert_sql(self, d, table):
        k = ""
        v = ""
        for key in d.keys():
            k += str(key).lower() + ", "
            v += "'" + str(d[key]) + "'" + ", "
        k = k[:-2]
        v = v[:-2]
        sql = "INSERT INTO " + table + " (%s) " % k + "VALUES (%s) " % v
        print(sql)
        return sql

    def disconnect(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


