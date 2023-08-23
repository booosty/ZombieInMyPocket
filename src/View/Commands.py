import cmd
from colorama import Fore, Style
from Model.Direction import Direction
from Model.Game import Game
from Model.State import State


class Commands(cmd.Cmd):
    intro = "Welcome to Zombies in my Pocket!"

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">> "
        self.game = Game()

    def do_start(self, line):
        """
        Starts a new game of Zombies in my Pocket
        """
        if self.game.state == State.STOPPED:
            self.game.create_game()
            self.game.get_game_status()
        else:
            print(
                Fore.RED
                + "You are already currently playing the game."
                + Style.RESET_ALL
            )

    def do_move_n(self, line):
        """
        Moves player to a NORTH tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.NORTH)
        else:
            print(
                Fore.RED
                + "You are currently not in the moving state."
                + Style.RESET_ALL
            )

    def do_move_e(self, line):
        """
        Moves player to a EAST tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.EAST)
        else:
            print(
                Fore.RED
                + "You are currently not in the moving state."
                + Style.RESET_ALL
            )

    def do_move_s(self, line):
        """
        Moves player to a SOUTH tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.SOUTH)
        else:
            print(
                Fore.RED
                + "You are currently not in the moving state."
                + Style.RESET_ALL
            )

    def do_move_w(self, line):
        """
        Moves player to a WEST tile
        :return:
        """
        if self.game.state == State.MOVING:
            self.game.move_player(Direction.WEST)
        else:
            print(
                Fore.RED
                + "You are currently not in the moving state."
                + Style.RESET_ALL
            )

    def do_cower(self, line):
        """
        Player cowers in their current tile
        Gains 3 Health
        """
        if self.game.state == State.MOVING:
            self.game.cower()
        else:
            print(
                Fore.RED
                + "You can not cower right now"
                + Style.RESET_ALL
            )

    def do_rotate(self, line):
        """
        Rotates the current tile 90 degrees clockwise
        """
        if self.game.state == State.ROTATING:
            self.game.rotate_tile()
            self.game.get_game_status()
        else:
            print(
                Fore.RED
                + "You are currently not in the rotating state"
                + Style.RESET_ALL
            )

    def do_place(self, line):
        """
        Places tile at current location and rotation
        """
        if self.game.state == State.ROTATING:
            self.game.place_tile()
        else:
            print(
                Fore.RED
                + "You are currently not in the rotating state"
                + Style.RESET_ALL
            )

    def do_draw(self, line):
        """
        Draws a new dev card from the pile
        """
        if self.game.state != State.STOPPED and self.game.state != State.BATTLE:
            self.game.draw_devcard()
        else:
            print(Fore.RED + "You cannot currently draw a card." + Style.RESET_ALL)

    def do_use_item(self, index):
        """
        Use item from inventory based on index e.g use_item 1
        :param index:
        :return:
        """
        if self.game.state != State.STOPPED:
            self.game.player.use_item(index)
        else:
            print(
                Fore.RED + "You can't currently use an item at the moment" + Style.RESET_ALL
            )

    def do_search(self, line):
        """
        Searches the current tile to see if the Totem is around
        """
        if self.game.state != State.STOPPED and self.game.state != State.BATTLE:
            self.game.search_tile()
        else:
            print(
                Fore.RED + "You can't currently search at the moment" + Style.RESET_ALL
            )

    def do_bury(self, line):
        """
        Bury the totem at the Graveyard
        """
        if self.game.state != State.STOPPED and self.game.state != State.BATTLE:
            self.game.bury_totem()
        else:
            print(
                Fore.RED
                + "You can't currently use this command at the moment"
                + Style.RESET_ALL
            )

    def do_attack(self, line):
        """
        Attack zombies that have appeared.
        """
        if self.game.state == State.BATTLE:
            self.game.player.do_attack()
        else:
            print(
                Fore.RED
                + "You can't attack when there are no zombies around."
                + Style.RESET_ALL
            )

    def do_run(self, line):
        """
        Run away from a zombie attack - losing 1 health.
        """
        if self.game.state == State.BATTLE:
            self.game.player.do_run()
        else:
            print(
                Fore.RED
                + "You can't run when there are no zombies around."
                + Style.RESET_ALL
            )

    def do_get_inventory(self, line):
        """
        Displays items that you currently hold in inventory and charges left.
        """
        if self.game.state != State.STOPPED:
            self.game.player.get_items()
        else:
            print(
                Fore.RED
                + "You can't currently use this command at the moment"
                + Style.RESET_ALL
            )

    @staticmethod
    def do_exit(self):
        """
        Quit Zombies in my Pocket
        """
        print(
            Fore.GREEN + "Thank you for playing Zombies in my Pocket!" + Style.RESET_ALL
        )
        return True

    def do_restart(self, line):
        """
        Restarts the current game. Does not save any progress.
        """
        print(Fore.RED + "Restarting game..." + Style.RESET_ALL)
        del self.game
        self.game = Game()
        self.game.create_game()
        self.game.get_game_status()

    def do_get_status(self, line):
        """
        Returns players status of current player
        """
        if self.game.state != State.STOPPED:
            self.game.get_player_stats()
        else:
            print(
                Fore.RED
                + "You are currently not playing a game, use 'start' to start a new game."
                + Style.RESET_ALL
            )
