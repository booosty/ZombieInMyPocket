from Model.DevCard import DevCard
from Model.Loader import Loader


class GameData:
    def __init__(self):
        self.dev_cards = []
        self.items = []
        self.loader = Loader()

        self.setup_game_data()

    def setup_game_data(self):
        self.get_items()
        self.get_dev_cards()

    def get_dev_cards(self):
        json_data = self.loader.load_data_from_json("devcard")
        for card in json_data:
            data = dict(card)
            item = data["item"]
            dev_card = DevCard(item, None, None, None)
            self.dev_cards.append(dev_card)

    def get_items(self):
        return
