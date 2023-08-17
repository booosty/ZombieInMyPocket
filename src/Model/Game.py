from Model.GameData import GameData
from Model.Player import Player
from Model.State import State


class Game:
    def __init__(self):
        self.game_data = GameData()
        self.player = Player(self.game_data)
        self.state = State.STOPPED
        self.time = 0

    def create_game(self):
        print("Starting a new game of Zombies in your Pocket...")
        self.time = 9
        self.game_data.shuffle_devcard_deck()
        self.game_data.remove_two_devcards()
        self.state = State.STARTED

    def get_stats(self):
        print(f"The current time is: {self.time}")
        print(f"Your current health is: {self.player.health}")
        print(f"Your current attack is: {self.player.attack}")
        print(f"You currently have the following items: {self.player.items}")

    # Junho
    def draw_devcard(self):
        if len(self.game_data.dev_cards) < 1:
            # All Dev cards have been drawn, reset the deck and increment time
            self.time += 1
            self.game_data.import_dev_cards()
            self.game_data.shuffle_devcard_deck()

        drawn_card = self.game_data.dev_cards.pop(0)
        return drawn_card
