import sys
from View.Commands import Commands


if __name__ == "__main__":
    commands = Commands(sys.argv)
    commands.cmdloop()
