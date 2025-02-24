import sqlite3


def create_table():
    conn = sqlite3.connect("./Section24/lite.db")

    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL) ")

    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("./Section24/lite.db")

    cur = conn.cursor()

    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))

    conn.commit()
    conn.close()

def request():
    conn = sqlite3.connect("./Section24/lite.db")

    cur = conn.cursor()

    cur.execute("SELECT * FROM store")

    rows = cur.fetchall()

    conn.close()
    return rows

insert("Coffee", 15, 1)
print(request())