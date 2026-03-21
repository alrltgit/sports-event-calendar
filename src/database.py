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

    def add_data(self, event):
        try:
            query = """
                INSERT INTO Events (Date_Time, Competition_ID, Venue_ID, Status) VALUES 
                (%s, %s, %s, %s)
                """
            data = (event.date_time, event.competition_id, event.venue_id, event.status)

            self.cursor.execute(query, data)
            self.sports_events_db.commit()

        except Exception as e:
            raise DbConnectionError(f"Failed to add data: {e}")

    def get_data(self):
        try:
            query = """
                SELECT 
                    e.Date_Time, 
                    e.Status, 
                    c.Name, 
                    v.Name
                FROM Events e
                JOIN Competitions c
                    ON e.Competition_ID = c.ID
                JOIN Venues v
                    ON e.Venue_ID = v.ID
                """

            self.cursor.execute(query)
            data = self.cursor.fetchall()
            print(data)
        except Exception as e:
            raise DbConnectionError(f"Failed to add data: {e}")

        return data

