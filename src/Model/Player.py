class Player:
    def __init__(self):
        self.__health = 6
        self.__attack = 1
        self.__pos_x = 0
        self.__pos_y = 0
        self.__items = []
        self.__hold_totem = False
        self.__can_cower = False
        self.__can_attack = False

    def get_health(self) -> int:
        return self.__health

    def set_health(self, value) -> None:
        self.__health = value

    health = property(get_health, set_health)

    def get_attack(self) -> int:
        return self.__attack

    def set_attack(self, value) -> None:
        self.__attack = value

    attack = property(get_attack, set_attack)

    def get_pos_x(self) -> int:
        return self.__pos_x

    def set_pos_x(self, value) -> None:
        self.__pos_x = value

    pos_x = property(get_pos_x, set_pos_x)

    def get_pos_y(self) -> int:
        return self.__pos_y

    def set_pos_y(self, value) -> None:
        self.__pos_y = value

    pos_y = property(get_pos_y, set_pos_y)

    def get_hold_totem(self) -> bool:
        return self.__hold_totem

    def set_hold_totem(self, value) -> None:
        self.__hold_totem = value

    hold_totem = property(get_hold_totem, set_hold_totem)

    def get_can_cower(self) -> bool:
        return self.__can_cower

    def set_can_cower(self, value) -> None:
        self.__can_cower = value

    can_cower = property(get_can_cower, set_can_cower)

    def get_can_attack(self) -> bool:
        return self.__can_attack

    def set_can_attack(self, value) -> None:
        self.__can_attack = value

    can_attack = property(get_can_attack, set_can_attack)

    def get_items(self) -> list:
        return self.__items

    items = property(get_items)

    def add_item(self, item, charges) -> None:
        self.__items.append([item, charges])

    def delete_item(self, item="") -> None:
        if item == "":
            raise Exception("Empty item cannot be deleted.")

        for items in self.__items:
            if items[0] == item:
                self.__items.pop(self.__items.index(items))
