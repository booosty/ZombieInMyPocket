import unittest
from unittest.mock import MagicMock
from model.database_handler import SQLiteHandler, SQLiteConnectionFactory


class TestSQLiteHandler(unittest.TestCase):
    def setUp(self):
        self.mock_connection_factory = MagicMock(spec=SQLiteConnectionFactory)
        self.handler = SQLiteHandler(self.mock_connection_factory)

    def test_save(self):
        mock_connection = MagicMock()
        mock_cursor = mock_connection.cursor.return_value

        self.mock_connection_factory.create_connection.return_value = mock_connection
        self.mock_connection_factory.create_cursor.return_value = mock_cursor

        game_state = {"player": "Test", "health": 10}

        self.handler.save(game_state)

        mock_cursor.execute.assert_any_call("DROP TABLE IF EXISTS game")
        mock_cursor.execute.assert_any_call("CREATE TABLE game(id, data)")
        mock_cursor.execute.assert_any_call("INSERT INTO game VALUES (?, ?)", (1, MagicMock()))

        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()

    def test_load(self):
        mock_connection = MagicMock()
        mock_cursor = mock_connection.cursor.return_value

        self.mock_connection_factory.create_connection.return_value = mock_connection
        self.mock_connection_factory.create_cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [(MagicMock(),)]

        loaded_data = self.handler.load()

        mock_cursor.execute.assert_called_once_with("SELECT data FROM game")
        mock_connection.close.assert_called_once()

        self.assertIsNotNone(loaded_data)


if __name__ == '__main__':
    unittest.main()
