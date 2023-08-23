import cmd

from Model.Direction import Direction
from Model.Game import Game
from Model.State import State


class Commands(cmd.Cmd):
    intro = "Welcome to Zombies in my Pocket!"

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>"
        self.game = Game()

    def do_start(self, line):
        """
        Starts a new game of Zombies in my Pocket
        """
        if self.game.state == State.STOPPED:
            self.game.create_game()
            self.game.get_game_status()
        else:
            print("You are already currently playing the game.")

    def do_move_n(self, line):
        """
        Moves player to a NORTH tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.NORTH)
        else:
            print("You are currently not in the moving state.")

    def do_move_e(self, line):
        """
        Moves player to a EAST tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.EAST)
        else:
            print("You are currently not in the moving state.")

    def do_move_s(self, line):
        """
        Moves player to a SOUTH tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.SOUTH)
        else:
            print("You are currently not in the moving state.")

    def do_move_w(self, line):
        """
        Moves player to a WEST tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.WEST)
        else:
            print("You are currently not in the moving state.")

    def do_rotate(self, line):
        """
        Rotates the current tile 90 degrees clockwise
        """
        if self.game.state == State.ROTATING:
            self.game.rotate_tile()
            self.game.get_game_status()
        else:
            print("You are currently not in the rotating state")

    def do_place(self, line):
        """
        Places tile at current location and rotation
        """
        if self.game.state == State.ROTATING:
            self.game.place_tile()
        else:
            print("You are currently not in the rotating state")

    def do_draw(self, line):
        """
        Draws a new dev card from the pile
        """
        if self.game.state == State.DRAWING:
            self.game.draw_devcard()
        else:
            print("You are not in the drawing state")

    def do_search(self, line):
        """
        Searches the current tile to see if the Totem is around
        """
        if self.game.state == State.DRAWING or State.ROTATING:
            current_tile = self.game.get_current_tile()
            if current_tile.name == "Evil Temple":
                self.game.player.hold_totem = True
                print(
                    "You have found the totem and quickly grab it, now go and bury it in the graveyard!"
                )
            else:
                print("Nope, nothing to be found around here!")
        else:
            print("You can't currently search at the moment")

    @staticmethod
    def do_exit(self):
        """
        Quit Zombies in my Pocket
        """
        print("Thank you for playing Zombies in my Pocket!")
        return True

    def do_get_status(self, line):
        """
        Returns players status of current player
        """
        if self.game.state != State.STOPPED:
            self.game.get_player_stats()
        else:
            print(
                "You are currently not playing a game, use 'start' to start a new game."
            )
