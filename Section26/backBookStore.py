import sqlite3

class Database:
    


    # Methods

    def __init__(self,db):
        Database.connect(self, db)
    
    def connect(self,db):        
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        # conn.close()

    def insert(self, title, author, year, isbn):
        # conn = sqlite3.connect("./Section26/books.db")
        # cur = conn.cursor()
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        #conn.close()

    def view(self):
        # conn = sqlite3.connect("./Section26/books.db")
        # cur = conn.cursor()
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        # conn = sqlite3.connect("./Section26/books.db")
        # cur = conn.cursor()
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        # conn.close()
        return rows


    def deleteTitle(self, title):
        # conn = sqlite3.connect("./Section26/lite.db")
        # cur = conn.cursor()
        self.cur.execute("DELETE FROM book WHERE title=?",(title,))
        self.conn.commit()
        # conn.close()

    def delete(self, id):
        # conn = sqlite3.connect("./Section26/books.db")
        # cur = conn.cursor()
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        # conn.close()

    def update(self,id, title, author, year, isbn):
        # conn = sqlite3.connect("./Section26/books.db")
        # cur = conn.cursor()
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year,isbn,id))
        self.conn.commit()
        #conn.close()
    
    def __del__(self):
        self.conn.close()

#connect()
#update(2,"S","s",1233,233232434)
#print(view())