from Player import Player
from State import State


class Game:
    def __init__(self):
        self.player = Player()
        self.state = State.STOPPED
        self.time = 0
