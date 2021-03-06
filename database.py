import sqlite3
from datetime import datetime
conn = sqlite3.connect('files/storage.db')
db = conn.cursor()

class Database(object):
    def __init__(self):
        pass

    def writePrice(self, pair, date, price):
        db.execute("INSERT OR REPLACE INTO lastPrice "
                   "VALUES (?, ?, ?)", (pair, date, format(float(price), '.8f')))
        conn.commit()

    def getLastPrice(self, pair):
        db.execute("SELECT PRICE FROM lastPrice WHERE PAIR = ?", (pair,))
        value = db.fetchone()
        if value is None:
            results = 0.01
        else:
            results = value[0]
        return results

    def getLastTime(self, pair):
        db.execute("SELECT DATE FROM lastPrice WHERE PAIR = ?", (pair,))
        value = db.fetchone()
        if value is None:
            results = datetime.fromtimestamp(int("0"))
        else:
            results = datetime.strptime(value[0],'%Y-%m-%d %H:%M:%S.%f')
        return results

