from Player import Player
from State import State


class Game:
    def __init__(self):
        self.player = None
        self.state = State.STOPPED
        self.time = 0

    def create_game(self):
        self.player = Player()
        self.state = State.STARTED
