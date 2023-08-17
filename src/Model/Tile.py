class Tile:
    def __init__(self, name, x, y):
        self.__name = name
        self.__pos_x = x
        self.__pos_y = y

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)

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
