import json
from abc import ABC
from pathlib import Path
import pickle
import shelve
from model.image_handler import ImageHandler
import tkinter as tk
from tkinter import filedialog


class SaveStrategy(ABC):
    """
    Save Strategy Interface
    """

    def save(self, game, filename):
        pass


class SavePickleStrategy(SaveStrategy):
    """
    Concrete Save with Pickle Strategy
    """

    def save(self, game, filename):
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        file_path = filedialog.asksaveasfilename(
            initialfile=filename,
            defaultextension=".pkl",
            filetypes=[("Pickle Files", "*.pkl")]
        )

        if file_path:
            with open(file_path, "wb") as file:
                pickle.dump(game, file)


class SaveShelveStrategy(SaveStrategy):
    """
    Concrete Save with Shelve Strategy
    """

    def save(self, game, filename=""):
        if filename != "":
            with shelve.open(str(FileHandler.root_dir / "saves") + "\\" + filename + ".db", flag='c',
                             protocol=4) as file:
                file["game"] = game
        else:
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)

            file_path = filedialog.asksaveasfilename(
                initialfile=filename,
                defaultextension=".shelf",
                filetypes=[("Shelve Files", "*.shelf"), ("All Files", "*.*")]
            )

            if file_path:
                with shelve.open(file_path, "c") as file:
                    file["game"] = game


class LoadStrategy(ABC):
    """
    Load Strategy Interface
    """

    def load(self, filename=""):
        pass


class LoadPickleStrategy(LoadStrategy):
    """
    Concrete Load with Pickle Strategy
    """

    def load(self, filename=""):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        root.attributes("-topmost", True)  # Make the file dialog appear on top

        file_path = filedialog.askopenfilename(
            filetypes=[("Pickle Files", "*.pkl")]
        )

        root.attributes("-topmost", False)

        if file_path:
            with open(file_path, "rb") as file:
                game = pickle.load(file)

            # Restore the image_handler attribute
            game.image_handler = ImageHandler()

            return game


class LoadShelveStrategy(LoadStrategy):
    """
    Concrete Load with Shelve Strategy
    """

    def load(self, filename=""):
        if filename != "":
            with shelve.open(str(FileHandler.root_dir / "saves") + "\\" + filename + ".db") as file:
                game = file["game"]
            return game
        else:
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                filetypes=[("Shelve Files", "*.bak"), ("All Files", "*.*")]
            )

            if file_path:
                # Remove extension from filepath
                file_path = file_path[:-4]
                print(file_path)
                with shelve.open(file_path) as file:
                    game = file["game"]
                return game


class FileHandler:
    """
    Object to hold file related methods e.g. saving/loading game state
    """
    root_dir = Path(__file__).parent.parent

    def __init__(self):
        self.save_strategy = None
        self.load_strategy = None

    def set_save_strategy(self, strategy):
        self.save_strategy = strategy

    def set_load_strategy(self, strategy):
        self.load_strategy = strategy

    def save_game(self, game, filename):
        self.save_strategy.save(game, filename)

    def load_game(self, filename=""):
        return self.load_strategy.load(filename)

    # William
    def load_data_from_json(self, filename):
        """
        Load json file from specified filename and return it
        :param filename:
        :return:
        """
        file = open(str(self.root_dir / "data") + "/" + filename + ".json")
        data = json.load(file)
        file.close()
        return data
