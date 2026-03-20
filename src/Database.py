import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self):
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DATABASE")

    def connect(self):
        sports_events_db = mysql.connector.connect(
            host = "localhost",
            user = self.user,
            password = self.password,
            database = self.database
        )
        cursor = sports_events_db.cursor()
        return cursor
