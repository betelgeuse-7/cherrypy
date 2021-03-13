import sqlite3 #SQLite for prototyping purposes.

class DBConnection:
    def __init__(self, dbname):
        self.dbname = dbname
        #connect
        self.con = sqlite3.connect(self.dbname, check_same_thread=False)
        self.cursor = self.con.cursor()

    def __repr__(self):
        return f"DBConnection object. TARGET_DB_NAME={self.dbname}"

    #is it secure???
    def fetch_all(self, table_name):
        return self.cursor.execute(f"""
                SELECT * FROM {table_name};
        """)

    def get(self, table_name, id):
        self.cursor.execute(f"""
            SELECT * FROM {table_name} WHERE id={id};
        """)
    
    def delete(self, table_name, id):
        self.cursor.execute(f"""
            DELETE FROM {table_name} WHERE id={id};
        """)

