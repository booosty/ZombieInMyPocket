import unittest
from unittest.mock import MagicMock, patch
from model.database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.handler = DatabaseHandler()

    @patch('model.database_handler.connect')
    def test_connect_sqlite_success(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        result = self.handler.connect_sqlite()
        mock_connect.assert_called_once_with(str(self.handler.root_dir / "saves") + "/" + "game_save.db")

        self.assertEqual(result, mock_connection)

    @patch('model.database_handler.connect', side_effect=Exception("Connection error"))
    def test_connect_sqlite_error(self, mock_connect):
        # Mock an exception during connection
        with self.assertRaises(Exception):
            self.handler.connect_sqlite()

        mock_connect.assert_called_once_with(str(self.handler.root_dir / "saves") + "/" + "game_save.db")

    @patch('model.database_handler.connect')
    def test_save_to_sqlite(self, mock_connect):
        # Mock the connection and cursor
        mock_connection = MagicMock()
        mock_cursor = mock_connection.cursor.return_value
        mock_connect.return_value = mock_connection

        game_state = {"player": "Test", "health": 10}

        self.handler.save_to_sqlite(game_state)

        mock_cursor.execute.assert_any_call("DROP TABLE IF EXISTS game")
        mock_cursor.execute.assert_any_call("CREATE TABLE game(id, data)")
        mock_cursor.execute.assert_any_call("INSERT INTO game VALUES (?, ?)", (1, MagicMock()))

        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()

    @patch('model.database_handler.connect')
    def test_load_from_sqlite(self, mock_connect):

        mock_connection = MagicMock()
        mock_cursor = mock_connection.cursor.return_value
        mock_connect.return_value = mock_connection

        mock_cursor.fetchall.return_value = [(MagicMock(),)]

        loaded_data = self.handler.load_from_sqlite()

        mock_cursor.execute.assert_called_once_with("SELECT data FROM game")
        mock_connection.close.assert_called_once()

        self.assertIsNotNone(loaded_data)
