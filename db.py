import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class DBConnection:
    def __init__(self):
        POSTGRES_CONN = os.getenv('POSTGRES_CONNECTION_STRING')
        self.con = psycopg2.connect(POSTGRES_CONN)
        self.cursor = self.con.cursor()
        self.dbname = POSTGRES_CONN.split("/")[-1].split("?")[0]

    def __repr__(self):
        return f"POSTGRES_CONN : {self.dbname}"
