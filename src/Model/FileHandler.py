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

    # Junho
    def load_game_with_pickle(self, filename):
        with open(str(self.root_dir / "Saves") + "\\" + filename + ".pkl", "rb") as file:
            game = pickle.load(file)

        # Restore the image_handler attribute
        game.image_handler = ImageHandler()

        return game
