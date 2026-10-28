import sqlite3
class database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("""
                       CREATE TABLE IF NOT EXISTS info(id INTEGER PRIMAY KEY,
                       name TEXT lname TEXT email TEXT password TEXT)
                       """)
        self.con.commit()

    def insert(self, name, lname, email, password):
            self.cur.execute("""
                INSERT INTO info (name, lname, email, password)
                VALUES (?, ?, ?, ?)
            """, (name, lname, email, password))
    
            self.con.commit()
    
    def login(self, email, password):
            self.cur.execute("""
                SELECT * FROM info
                WHERE email = ? AND password = ?
            """, (email, password))
    
            return self.cur.fetchone()     