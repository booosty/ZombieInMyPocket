class Item:
    def __init__(self, name, action, uses, combinable, combines_with, makes):
        self.name = name
        self.action = action
        self.uses = uses
        self.combinable = combinable
        self.combines_with = combines_with
        self.makes = makes

    @staticmethod
    def add_attack(self, player, value):
        player.attack += value
