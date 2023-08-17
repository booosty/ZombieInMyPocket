from Model.GameData import GameData
from Model.Player import Player
from State import State

#test commit
class Game:
    def __init__(self):
        self.game_data = None
        self.player = None
        self.state = State.STOPPED
        self.time = 0

    def create_game(self):
        print("Starting a new game of Zombies in your Pocket...")
        self.game_data = GameData()
        self.player = Player()
        self.state = State.STARTED
        self.time = 1

    def get_stats(self):
        print(f"The current time is: {self.time}")
        print(f"Your current health is: {self.player.health}")
        print(f"Your current attack is: {self.player.attack}")
        print(f"You currently have the following items: {self.player.items}")
