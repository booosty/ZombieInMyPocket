class Tile:
    def __init__(
        self,
        name,
        action,
        room_type,
        src,
        door_n,
        door_e,
        door_s,
        door_w,
        action_amount=0,
    ):
        self.name = name
        self.action = action
        self.action_amount = action_amount
        self.room_type = room_type
        self.img_src = src
        self.rotate_factor = 0
        self.door_n = door_n
        self.door_e = door_e
        self.door_s = door_s
        self.door_w = door_w
