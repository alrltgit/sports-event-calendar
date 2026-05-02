from unittest import TestCase, main
from unittest.mock import MagicMock
from src.database import Database, DbConnectionError

class TestDatabase(TestCase):
    def setUp(self):
        self.db = Database.__new__(Database)
        self.db.engine = MagicMock()
        self.connection = MagicMock()
        self.db.engine.begin.return_value.__enter__.return_value = self.connection
        self.db.engine.connect.return_value.__enter__.return_value = self.connection

    def test_add_data_empty_query(self):
        with self.assertRaises(ValueError):
            self.db.add_data("", {"sport": "Golf"})

    def test_add_data_wrong_query(self):
        self.connection.execute.side_effect = Exception("DB Error")

        query = "INSERT INTO non_existing_table (Name) VALUES (:sport)"
        new_data = {"sport": "Golf"}
        with self.assertRaises(DbConnectionError):
            self.db.add_data(query, new_data)

    def test_add_data_normal_query(self):
        result = MagicMock()
        result.lastrowid = 123
        self.connection.execute.return_value = result

        query = "INSERT INTO Sports (Name) VALUES (:sport)"
        new_data = {"sport": "Golf"}
        result = self.db.add_data(query, new_data)

        self.assertEqual(result, 123)

    def test_get_data_empty_query(self):
        with self.assertRaises(ValueError):
            self.db.get_data("")

    def test_get_data_wrong_query(self):
        self.connection.execute.side_effect = Exception("DB Error")

        query = "SELECT * FROM non_existent_table"
        with self.assertRaises(DbConnectionError):
            self.db.get_data(query)

    def test_get_data_with_params(self):
        result = MagicMock()
        result.fetchall.return_value = [(1,)]
        self.connection.execute.return_value = result

        query = "SELECT ID FROM Sports WHERE Name = :sport"
        params = {"sport": "Football"}
        data = self.db.get_data(query, params)

        self.connection.execute.assert_called_once()
        executed_query, executed_params = self.connection.execute.call_args.args
        self.assertEqual(str(executed_query), query)
        self.assertEqual(executed_params, params)
        self.assertEqual(data, [(1,)])

if __name__ == "__main__":
    main()
