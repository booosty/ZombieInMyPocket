import unittest
from unittest.mock import MagicMock, patch
from model.file_handler import FileHandler

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.handler = FileHandler()

    @patch('model.file_handler.json.load')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_load_data_from_json(self, mock_open, mock_json_load):
        file_content = '{"key": "value"}'
        mock_open.return_value.read.return_value = file_content

        result = self.handler.load_data_from_json('test_file')

        mock_open.assert_called_once_with(str(self.handler.root_dir / "data") + "/test_file.json")
        mock_json_load.assert_called_once_with(mock_open.return_value)

        self.assertEqual(result, {"key": "value"})

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('tkinter.Tk.withdraw')
    @patch('tkinter.Tk.attributes')
    @patch('tkinter.filedialog.asksaveasfilename', return_value='file_path.pkl')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_game_with_pickle(self, mock_open1, mock_asksaveasfilename, mock_attributes, mock_withdraw, mock_open2):
        game_state = {"player": "Test", "health": 10}

        # Test save_game_with_pickle
        self.handler.save_game_with_pickle(game_state, 'test_game')

        mock_withdraw.assert_called_once()
        mock_attributes.assert_called_once_with("-topmost", True)
        mock_asksaveasfilename.assert_called_once_with(
            initialfile='test_game',
            defaultextension=".pkl",
            filetypes=[("Pickle Files", "*.pkl")]
        )
        mock_open2.assert_called_once_with('file_path.pkl', 'wb')
        mock_open2.return_value.write.assert_called_once()

    @patch('shelve.open')
    @patch('tkinter.Tk.withdraw')
    @patch('tkinter.Tk.attributes')
    @patch('tkinter.filedialog.asksaveasfilename', return_value='file_path.shelf')
    def test_save_game_with_shelve(self, mock_asksaveasfilename, mock_attributes, mock_withdraw, mock_shelve_open):
        game_state = {"player": "Test", "health": 10}

        # Test save_game_with_shelve
        self.handler.save_game_with_shelve(game_state, 'test_game')

        mock_withdraw.assert_called_once()
        mock_attributes.assert_called_once_with("-topmost", True)
        mock_asksaveasfilename.assert_called_once_with(
            initialfile='test_game',
            defaultextension=".shelf",
            filetypes=[("Shelve Files", "*.shelf"), ("All Files", "*.*")]
        )
        mock_shelve_open.assert_called_once_with('file_path.shelf', 'c', protocol=4)
        mock_shelve_open.return_value.__setitem__.assert_called_once_with('game', game_state)

    @patch('shelve.open')
    @patch('tkinter.Tk.withdraw')
    @patch('tkinter.filedialog.askopenfilename', return_value='file_path.shelf')
    def test_load_game_with_shelve(self, mock_askopenfilename, mock_withdraw, mock_shelve_open):
        game_state = {"player": "Test", "health": 10}

        # Test load_game_with_shelve
        result = self.handler.load_game_with_shelve('test_game')

        mock_withdraw.assert_called_once()
        mock_askopenfilename.assert_called_once_with(filetypes=[("Shelve Files", "*.bak"), ("All Files", "*.*")])
        mock_shelve_open.assert_called_once_with('file_path.shelf')
        self.assertEqual(result, game_state)

    @patch('tkinter.Tk.withdraw')
    @patch('tkinter.filedialog.askopenfilename', return_value='file_path.pkl')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_load_game_with_pickle(self, mock_open, mock_askopenfilename, mock_withdraw):
        game_state = {"player": "Test", "health": 10}

        # Test load_game_with_pickle
        result = self.handler.load_game_with_pickle()

        mock_withdraw.assert_called_once()
        mock_askopenfilename.assert_called_once_with(filetypes=[("Pickle Files", "*.pkl")])
        mock_open.assert_called_once_with('file_path.pkl', 'rb')
        self.assertEqual(result, game_state)

    if __name__ == '__main__':
        unittest.main()