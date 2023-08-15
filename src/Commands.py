import cmd
from Game import Game


class Commands(cmd.Cmd):
    intro = "Welcome to Zombies in my Pocket!"
    prompt = ">>"

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.game = Game()

    def do_get_health(self, line):
        print(self.game.player.get_health())
