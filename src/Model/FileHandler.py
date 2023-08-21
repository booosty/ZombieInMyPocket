import json
from pathlib import Path


class FileHandler:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent / "Data"

    def load_data_from_json(self, filename):
        file = open(str(self.root_dir) + "\\" + filename + ".json")
        data = json.load(file)
        file.close()
        return data
