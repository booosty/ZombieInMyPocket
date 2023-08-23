from colorama import Fore, Style

from Model.State import State


class Player:
    def __init__(self, game_data, game):
        self.game = game
        self.game_data = game_data
        self.health = 6
        self.attack = 1
        self.x = 4
        self.y = 8
        self.items = []
        self.hold_totem = False

    def set_health(self, amount):
        verb = ""
        damage = amount

        if amount > 4:
            damage = 4

        self.health += damage

        if damage > 0:
            verb = "gain"
        else:
            verb = "lose"

        print(
            Fore.MAGENTA
            + f"You {verb} {damage} health!, you now have {self.health} health."
            + Style.RESET_ALL
        )

        if self.health <= 0:
            self.game.state = State.LOST
            print(
                Fore.RED
                + "Sorry you have run out of health! You loose."
                + Style.RESET_ALL
            )
            exit()

    def add_item(self, item) -> None:
        if len(self.items) > 2:
            print(
                Fore.RED
                + f"You already have 2 items, you cannot carry anymore."
                + Style.RESET_ALL
            )
            return
        for items in self.game_data.items:
            if items.name == item:
                print(
                    Fore.CYAN
                    + f"{items.name} with {items.uses} uses has been added to your inventory."
                    + Style.RESET_ALL
                )
                self.items.append([items.name, items.uses])

    def get_items(self):
        print(
            Fore.YELLOW
            + f"Your inventory:"
            + Style.RESET_ALL
        )
        for index, item in enumerate(self.items):
            print(
                Fore.CYAN
                + f"[{index}] - {item[0]} with {item[1]} uses left."
                + Style.RESET_ALL
            )

    def delete_item(self, item="") -> None:
        if item == "":
            raise Exception("Empty item cannot be deleted.")

        for items in self.items:
            if items[0] == item:
                self.items.pop(self.items.index(items))

    def do_attack(self):
        zombies_left = self.game.current_zombie_count - self.attack
        print(
            Fore.YELLOW
            + f"You attack the zombies.."
            + Style.RESET_ALL
        )
        self.set_health(-zombies_left)
        if (self.attack - zombies_left) <= 0:
            self.attack = 0
        else:
            self.attack -= zombies_left

        print(
            Fore.RED
            + f"You now have {self.attack} attack."
            + Style.RESET_ALL
        )
        self.game.current_zombie_count = 0
        self.game.state = State.MOVING
        self.game.get_game_status()

    def do_run(self):
        self.set_health(-1)
        print(
            Fore.YELLOW
            + f"You run away from the Zombies..."
            + Style.RESET_ALL
        )
        self.game.current_zombie_count = 0
        self.game.state = State.MOVING
        self.game.get_game_status()
