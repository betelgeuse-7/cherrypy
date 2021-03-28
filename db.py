import sqlite3

class DBConnection:
    def __init__(self, sqlite_db):
        #check_same_thread=False
        #to avoid SQLite objects created in a thread can only be used in that same thread.
        self.con = sqlite3.connect(sqlite_db, check_same_thread=False)
        self.cursor = self.con.cursor()
        self.dbname = sqlite_db

    def __repr__(self):
        return f"SQLITE_DB_CONN_TO : {self.dbname}"
    
    def select(self, column, table):
        self.cursor.execute(f"SELECT {column} FROM {table};")

    def select_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table};")
    

