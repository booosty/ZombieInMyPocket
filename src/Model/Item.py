class Item:
    def __init__(self, name, action, uses, combinable, combines_with, makes):
        self.__name = name
        self.__action = action
        self.__uses = uses
        self.__combinable = combinable
        self.__combines_with = combines_with
        self.__makes = makes

    @staticmethod
    def add_attack(self, player, value):
        player.attack += value
