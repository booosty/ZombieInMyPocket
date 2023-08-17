from Model.Player import Player
from State import State


class Game:
    def __init__(self):
        self.__player = None
        self.__state = State.STOPPED
        self.__time = 0

    def get_player(self) -> Player:
        return self.__player

    def set_player(self, player) -> None:
        self.__player = player

    player = property(get_player, set_player)

    def get_state(self) -> State:
        return self.__state

    def set_state(self, state) -> None:
        self.__state = state

    state = property(get_state, set_state)

    def get_time(self) -> int:
        return self.__time

    def set_time(self, value):
        self.__time = value

    time = property(get_time, set_time)

    def create_game(self):
        print("Starting a new game of Zombies in your Pocket...")
        self.player = Player()
        self.state = State.STARTED
        self.time = 1

    def get_stats(self):
        print(f"The current time is: {self.time}")
        print(f"Your current health is: {self.player.health}")
        print(f"Your current attack is: {self.player.attack}")
        print(f"You currently have the following items: {self.player.items}")
