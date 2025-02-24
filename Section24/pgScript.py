import psycopg2
from dotenv import load_dotenv, dotenv_values, find_dotenv
import os

load_dotenv(find_dotenv())

def connect():
    conn = psycopg2.connect(   
    user = os.getenv("DATABASE_USERNAME"),                                      
     password = os.getenv("DATABASE_PASSWORD"),                                  
    host = os.getenv("DATABASE_IP"),                                            
    port = os.getenv("DATABASE_PORT"),                                          
    database = os.getenv("DATABASE_NAME")
    
    ) 
    return conn

def create_table():
    conn = psycopg2.connect(   
        user = os.getenv("DATABASE_USERNAME"),                                      
        password = os.getenv("DATABASE_PASSWORD"),                                  
        host = os.getenv("DATABASE_IP"),                                            
        port = os.getenv("DATABASE_PORT"),                                          
        database = os.getenv("DATABASE_NAME")
    )    
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL) ")

    conn.commit()
    conn.close()

def insert(item, quantity, price, conn):
    
    cur = conn.cursor()

    #cur.execute("INSERT INTO store VALUES (%s, %s, %s)" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)" , (item,quantity,price))

    conn.commit()
    conn.close()

def request(conn):

    cur = conn.cursor()

    cur.execute("SELECT * FROM store")

    rows = cur.fetchall()

    conn.close()
    return rows

def delete(item, conn):

    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(item, quantity, price, conn):

    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item,))
    conn.commit()
    conn.close()

conn = connect()
create_table()
insert("Apple", 44, 29.8, conn)
conn = connect()
insert("Orange", 4, 3.8, conn)

conn = connect()
request(conn)

conn = connect()
delete("Apple",conn)

conn = connect()
update("Orange",44, 99.3, conn)

