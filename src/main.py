import sys
from View.Commands import Commands


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"You provided {len(sys.argv) - 1} command line arguments.")
    commands = Commands()
    commands.cmdloop()
