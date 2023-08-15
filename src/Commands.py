import cmd
from Game import Game
from State import State


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
        else:
            print("You are already currently playing the game.")

    @staticmethod
    def do_exit(self):
        """
        Quit Zombies in my Pocket
        """
        print("Thank you for playing Zombies in my Pocket!")
        return True

    def do_get_health(self, line):
        """
        Returns players current health
        """
        if self.game.state != State.STOPPED:
            print(self.game.player.health)
        else:
            print(
                "You are currently not playing a game, use 'start' to start a new game."
            )
