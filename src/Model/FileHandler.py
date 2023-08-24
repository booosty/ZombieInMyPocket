import json
from pathlib import Path
import pickle
import shelve
from Model.ImageHandler import ImageHandler


class FileHandler:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent

    def load_data_from_json(self, filename):
        file = open(str(self.root_dir / "Data") + "\\" + filename + ".json")
        data = json.load(file)
        file.close()
        return data

    # Junho
    def save_game_with_pickle(self, game, filename):
        with open(str(self.root_dir / "Saves") + "\\" + filename + ".pkl", "wb") as file:
            pickle.dump(game, file)

    # William
    def save_game_with_shelve(self, game, filename):
        with shelve.open(str(self.root_dir / "Saves") + "\\" + filename + ".shelf", 'c') as file:
            file["game"] = game

    def load_game_with_shelve(self, filename):
        with shelve.open(str(self.root_dir / "Saves") + "\\" + filename + ".shelf") as file:
            game = file["game"]
        return game

    # Junho
    def load_game_with_pickle(self, filename):
        with open(str(self.root_dir / "Saves") + "\\" + filename + ".pkl", "rb") as file:
            game = pickle.load(file)

        # Restore the image_handler attribute
        game.image_handler = ImageHandler()

        return game
