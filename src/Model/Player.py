class Player:
    def __init__(self):
        self.health = 6
        self.attack = 1
        self.pos_x = 0
        self.pos_y = 0
        self.items = []
        self.hold_totem = False
        self.can_cower = False
        self.can_attack = False

    def add_item(self, item, charges) -> None:
        self.items.append([item, charges])

    def delete_item(self, item="") -> None:
        if item == "":
            raise Exception("Empty item cannot be deleted.")

        for items in self.items:
            if items[0] == item:
                self.items.pop(self.items.index(items))
