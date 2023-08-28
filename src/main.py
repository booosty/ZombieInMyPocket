import sys
from view.commands import Commands


if __name__ == "__main__":
    commands = Commands(sys.argv)
    commands.cmdloop()
