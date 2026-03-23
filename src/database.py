import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DbConnectionError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return self.args[0]

class Database:
    def __init__(self):
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DATABASE")
        self.cursor = None
        self.sports_events_db = None
        self.connect()

    def connect(self):
        self.sports_events_db = mysql.connector.connect(
            host = "localhost",
            user = self.user,
            password = self.password,
            database = self.database
        )

        self.cursor = self.sports_events_db.cursor()

    def add_data(self, sql_query, new_data):
        if not sql_query:
            raise ValueError("SQL query cannot be empty")

        try:
            self.cursor.execute(sql_query, new_data)
            self.sports_events_db.commit()

        except Exception as e:
            raise DbConnectionError(f"Failed to add data: {e}")

        return self.cursor.lastrowid

    def get_data(self, sql_query):
        if not sql_query:
            raise ValueError("SQL query cannot be empty")

        try:
            query = sql_query
            self.cursor.execute(query)
            data = self.cursor.fetchall()

        except Exception as e:
            raise DbConnectionError(f"Failed to add data: {e}")

        return data

