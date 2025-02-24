import psycopg2
from dotenv import load_dotenv, dotenv_values, find_dotenv
import os

load_dotenv(find_dotenv())

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




create_table()
