class Tile:
    def __init__(self, name, action, room_type, src, door_n, door_e, door_s, door_w):
        self.name = name
        self.action = action
        self.room_type = room_type
        self.img_src = src
        self.door_n = door_n
        self.door_e = door_e
        self.door_s = door_s
        self.door_w = door_w
