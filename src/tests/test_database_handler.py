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
        mock_connect.assert_called_once_with(str(self.handler.root_dir / "saves") + "\\" + "game_save.db")

        self.assertEqual(result, mock_connection)
