from Direction import Direction


class Player:
    def __init__(self):
        self.health = 6
        self.attack = 1
        self.pos_x = 0
        self.pos_y = 0
        self.direction = Direction.NONE
        self.items = []
        self.hold_totem = False

    def get_health(self):
        return self.health
