class Tile:
    def __init__(self, name, action, room_type, door_n, door_e, door_s, door_w):
        self.__name = name
        self.__action = action
        self.__room_type = room_type
        self.__door_n = door_n
        self.__door_e = door_e
        self.__door_s = door_s
        self.__door_w = door_w

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)
