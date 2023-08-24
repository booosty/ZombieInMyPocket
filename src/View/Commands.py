import cmd
from colorama import Fore, Style
from Model.Direction import Direction
from Model.Game import Game
from Model.State import State
from Model.FileHandler import FileHandler


class Commands(cmd.Cmd):
    intro = "Welcome to Zombies in my Pocket!"

    # Junho & William
    def __init__(self, args=""):
        cmd.Cmd.__init__(self)
        self.prompt = ">> "
        self.game = Game()
        self.file_handler = FileHandler()
        self.args = args
        self.command_methods = {
            "start": self.do_start,
            "help": self.do_help,
            "exit": self.do_exit,
        }

        if len(args) > 1:
            self.check_args(args)

    # Junho & William
    def check_args(self, args):
        for command in args:
            if command in self.command_methods:
                self.command_methods[command](command)
            else:
                print(f"Unknown command: {command}")

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
            current_tile = self.game.get_current_tile()
            self.game.rotate_tile(current_tile)  # Pass the current tile to the rotate_tile method
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

    # Junho
    def do_use_item(self, index):
        """
        Use an item from the players inventory based on the index e.g. use_item 1
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

    # Junho
    def do_attack(self, line):
        """
        Attacks zombies when they appear
        """
        if self.game.state == State.BATTLE:
            self.game.player.do_attack()
        else:
            print(
                Fore.RED
                + "You can't attack when there are no zombies around."
                + Style.RESET_ALL
            )

    # Junho
    def do_run(self, line):
        """
        Run away from a zombie attack
        You lose 1 health.
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

    # Junho
    def do_save(self, line):
        """
        Save the current game to a file
        """
        params = line.split()

        if len(params) < 2:
            print(Fore.RED + "Usage: save <filename> <method>" + Style.RESET_ALL)
            return

        filename = params[0]
        method = params[1]

        if self.game.state != State.STOPPED:
            try:
                if method == "pickle":
                    self.file_handler.save_game_with_pickle(self.game, filename)
                    print(Fore.GREEN + f"Game saved as '{filename}.pkl' using pickle" + Style.RESET_ALL)
                elif method == "shelf":
                    self.file_handler.save_game_with_shelve(self.game, filename)
                    print(Fore.GREEN + f"Game saved as '{filename}.shelf' using shelf" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Invalid save method. Use 'pickle' or 'shelf'." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"An error occurred while saving the game: {e}" + Style.RESET_ALL)
        else:
            print(
                Fore.RED
                + "You are currently not playing a game. Use 'start' to start a new game."
                + Style.RESET_ALL
            )

    # Junho
    def do_load(self, line):
        """
        Load a saved game from a file
        """
        params = line.split()

        if len(params) < 2:
            print(Fore.RED + "Usage: load <filename> <method>" + Style.RESET_ALL)
            return

        filename = params[0]
        method = params[1]

        try:
            if method == "pickle":
                loaded_game = self.file_handler.load_game_with_pickle(filename)
                if loaded_game:
                    self.game = loaded_game
                    self.game.image_handler.create_map_image(self.game.game_data.map, self.game.player)
                    print(Fore.GREEN + f"Game loaded from '{filename}.pkl'" + Style.RESET_ALL)
                    self.game.get_game_status()
                else:
                    print(Fore.RED + f"Could not load game from '{filename}.pkl'" + Style.RESET_ALL)
            elif method == "shelf":
                loaded_game = self.file_handler.load_game_with_shelve(filename)
                if loaded_game:
                    self.game = loaded_game
                    self.game.image_handler.create_map_image(self.game.game_data.map, self.game.player)
                    print(Fore.GREEN + f"Game loaded from '{filename}.shelf'" + Style.RESET_ALL)
                    self.game.get_game_status()
                else:
                    print(Fore.RED + f"Could not load game from '{filename}.shelf'" + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + f"An error occurred while loading the game: {e}" + Style.RESET_ALL)

    # Junho
    def do_help_all(self, line):
        """
        Display all available commands and descriptions
        """
        all_commands = [
            "start", "move_n", "move_e", "move_s", "move_w", "cower",
            "rotate", "place", "draw", "use_item", "search", "bury",
            "attack", "run", "get_inventory", "exit", "restart",
            "get_status", "save", "load", "help_all"
        ]
        print("Available commands:")
        for command in all_commands:
            doc = getattr(self, f"do_{command}").__doc__
            print(f"{command}: {doc}")
