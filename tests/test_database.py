from unittest import TestCase, main
from unittest.mock import MagicMock
from src.database import Database, DbConnectionError

class TestDatabase(TestCase):
    def setUp(self):
        self.db = Database()
        self.db.cursor = MagicMock()
        self.db.sports_event_db = MagicMock()

    def test_add_data_empty_query(self):
        with self.assertRaises(ValueError):
            self.db.add_data("", ("Golf", ))

    def test_add_data_wrong_query(self):
        self.db.cursor.execute.side_effect = Exception("DB Error")

        query = "INSERT INTO non_existing_table (Name) VALUES (%s)"
        new_data = ("Golf", )
        with self.assertRaises(DbConnectionError):
            self.db.add_data(query, new_data)

    def test_add_data_normal_query(self):
        self.db.cursor.lastrowid = 123

        query = "INSERT INTO Sports (Name) VALUES (%s)"
        new_data = ("Golf", )
        result = self.db.add_data(query, new_data)

        self.assertEqual(result, 123)

    def test_get_data_empty_query(self):
        with self.assertRaises(ValueError):
            self.db.get_data("")

    def test_get_data_wrong_query(self):
        self.db.cursor.execute.side_effect = Exception("DB Error")

        query = "SELECT * FROM non_existent_table"
        with self.assertRaises(DbConnectionError):
            self.db.get_data(query)

if __name__ == "__main__":
    main()
