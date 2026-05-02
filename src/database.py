import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

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
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "3307"))
        self.engine = None
        self.connect()

    def connect(self):
        database_url = URL.create(
            "mysql+pymysql",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )
        self.engine = create_engine(database_url)

    def add_data(self, sql_query, new_data):
        if not sql_query:
            raise ValueError("SQL query cannot be empty")

        try:
            with self.engine.begin() as connection:
                result = connection.execute(text(sql_query), new_data)

        except Exception as e:
            raise DbConnectionError(f"Failed to add data: {e}")

        return result.lastrowid

    def get_data(self, sql_query, params=None):
        if not sql_query:
            raise ValueError("SQL query cannot be empty")

        try:
            with self.engine.connect() as connection:
                result = connection.execute(text(sql_query), params or {})
                data = result.fetchall()

        except Exception as e:
            raise DbConnectionError(f"Failed to get data: {e}")

        return data
