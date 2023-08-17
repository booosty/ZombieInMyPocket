from Tile import Tile


class OutdoorTile(Tile):
    def __init__(self, name, x, y):
        self.__type = "Outdoor"
        super().__init__(name, x, y)
