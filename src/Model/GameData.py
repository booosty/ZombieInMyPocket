from Model.DevCard import DevCard
from Model.Item import Item
from Model.Loader import Loader


class GameData:
    def __init__(self):
        self.dev_card_discard = []
        self.dev_card_deck = list(self.dev_card_discard)
        self.dev_card_discard = []
        self.dev_card_deck = list(self.dev_cards)
        self.dev_cards = []
        self.items = []
        self.loader = Loader()

        self.setup_game_data()

    def setup_game_data(self):
        self.import_dev_cards()
        self.import_items()

    def import_dev_cards(self):
        json_data = self.loader.load_data_from_json("devcard")

        for card in json_data:
            data = dict(card)
            item = data["item"]
            nine_effect = data["effect"]["nine"]
            ten_effect = data["effect"]["ten"]
            eleven_effect = data["effect"]["eleven"]

            dev_card = DevCard(
                item,
                nine_effect["message"],
                nine_effect["action"],
                ten_effect["message"],
                ten_effect["action"],
                eleven_effect["message"],
                eleven_effect["action"],
            )

            self.dev_cards.append(dev_card)

    def import_items(self):
        json_data = self.loader.load_data_from_json("items")

        for item in json_data:
            data = dict(item)
            new_item = Item(
                data["name"],
                data["action"],
                data["uses"],
                data["combinable"],
                data["combines-with"],
                data["makes"],
            )

            self.items.append(new_item)

    def initialize_dev_card_deck(self):
        random.shuffle(self.dev_card_deck)

    def draw_dev_card(self):
        if not self.dev_card_deck:
            # All Dev cards have been drawn, reset the deck and increment time
            self.time += 1
            random.shuffle(self.dev_card_deck)

        drawn_card = self.dev_card_deck.pop(0)
        return drawn_card

    def discard_dev_card(self, card):
        self.dev_card_discard.append(card)
