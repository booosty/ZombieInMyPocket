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

    def add_attack(self, amount):
        self.attack += amount
        print(
            Fore.MAGENTA
            + f"You have increased your attack!, you now have {self.attack} attack."
            + Style.RESET_ALL
        )

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
                + f"[{index + 1}] - {item[0]} with {item[1]} uses left."
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

        if zombies_left > 0:
            self.set_health(-zombies_left)

        if (self.game.current_zombie_count - self.attack) > 0:
            self.attack = 0
        else:
            self.attack -= self.game.current_zombie_count

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

    def kill_all_zombies(self, item):
        print(
            Fore.CYAN
            + f"You used your {item} and killed all the zombies!"
            + Style.RESET_ALL
        )
        self.game.current_zombie_count = 0
        self.game.state = State.MOVING
        self.game.get_game_status()

    def negate_damage(self):
        self.game.current_zombie_count = 0
        self.do_attack()

    def use_item(self, index):
        index_num = int(index)
        if index_num > 2 or index_num > len(self.items):
            print(
                Fore.RED
                + f"Error: Invalid Index"
                + Style.RESET_ALL
            )
            return

        item_name = self.items[index_num - 1][0]
        item_uses = self.items[index_num - 1][1]

        for item in self.game_data.items:
            if item_name == item.name:
                match item.action:
                    case "negate_damage":
                        self.negate_damage()
                    case "add_attack":
                        self.add_attack(item.action_amount)
                    case "add_health":
                        self.set_health(item.action_amount)
                    case "kill_all_zombies":
                        self.kill_all_zombies(item.name)
                    case False:
                        print(
                            Fore.RED
                            + f"Item cannot be used"
                            + Style.RESET_ALL
                         )
                        return

        if item_uses == 1:
            self.delete_item(item_name)
            print(
                Fore.RED
                + f"You have used all charges of {item_name}"
                + Style.RESET_ALL
            )
        else:
            print(
                Fore.YELLOW
                + f"You have used 1 charge of {item_name}"
                + Style.RESET_ALL
            )
            self.items[index_num - 1][1] -= 1

