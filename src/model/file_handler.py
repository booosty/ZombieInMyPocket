import json
from pathlib import Path
import pickle
import shelve
from model.image_handler import ImageHandler
import tkinter as tk
from tkinter import filedialog


class FileHandler:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent

    def load_data_from_json(self, filename):
        file = open(str(self.root_dir / "data") + "\\" + filename + ".json")
        data = json.load(file)
        file.close()
        return data

    # Junho
    def save_game_with_pickle(self, game, filename):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        root.attributes("-topmost", True)  # Make the file dialog appear on top

        file_path = filedialog.asksaveasfilename(
            initialfile=filename,
            defaultextension=".pkl",
            filetypes=[("Pickle Files", "*.pkl"), ("All Files", "*.*")]
        )

        if file_path:
            with open(file_path, "wb") as file:
                pickle.dump(game, file)

    # William
    def save_game_with_shelve(self, game, filename):
        with shelve.open(str(self.root_dir / "saves") + "\\" + filename + ".shelf", 'c') as file:
            file["game"] = game

    def load_game_with_shelve(self, filename):
        with shelve.open(str(self.root_dir / "saves") + "\\" + filename + ".shelf") as file:
            game = file["game"]
        return game

    # Junho
    def load_game_with_pickle(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        root.attributes("-topmost", True)  # Make the file dialog appear on top

        file_path = filedialog.askopenfilename(
            filetypes=[("Pickle Files", "*.pkl"), ("All Files", "*.*")]
        )

        root.attributes("-topmost", False)

        if file_path:
            with open(file_path, "rb") as file:
                game = pickle.load(file)

            # Restore the image_handler attribute
            game.image_handler = ImageHandler()

            return game


