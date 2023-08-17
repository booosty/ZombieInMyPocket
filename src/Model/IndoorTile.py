from Tile import Tile


class IndoorTile(Tile):
    def __init__(self, name, x, y):
        self.__type = "Indoor"
        super().__init__(name, x, y)
