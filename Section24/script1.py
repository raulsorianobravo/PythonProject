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

def delete(item):
    conn = sqlite3.connect("./Section24/lite.db")

    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = sqlite3.connect("./Section24/lite.db")

    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    conn.close()

insert("Coffee", 15, 9)
print(request())
update("Coffee", 135, 19)
print(request())
delete("Coffee")
print(request())
