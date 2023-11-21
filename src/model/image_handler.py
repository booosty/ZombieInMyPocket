from PIL import Image, ImageOps
from pathlib import Path


class ImageHandler:
    """
    Image class and functions to create and save map based on game data
    """
    def __init__(self):
        self.size = (150, 150)
        self.root_dir = Path(__file__).parent.parent / "data" / "Images"

    # William
    def create_map_image(self, game_map, player, grid=(9, 9)):
        """
        Creates a new image based of current game map data and overwrites old image
        :param game_map:
        :param player:
        :param grid:
        :return:
        """
        width, height = self.size

        image_size = (width * grid[1], height * grid[0])
        map_image = Image.new("RGB", image_size)

        for row in range(grid[0]):
            for col in range(grid[1]):
                offset = width * col, height * row
                if game_map[row][col] == 0:
                    new_image = Image.open(str(self.root_dir) + "/blank.png")

                    new_image = ImageOps.fit(new_image, self.size)
                    new_image = ImageOps.expand(new_image, border=1, fill="black")
                    map_image.paste(new_image, offset)
                else:
                    new_image = Image.open(
                        str(self.root_dir) + "/" + game_map[row][col].img_src
                    )

                    rotated_image = None

                    match game_map[row][col].rotate_factor:
                        case 0:
                            rotated_image = new_image
                        case 1:
                            rotated_image = new_image.rotate(270)
                        case 2:
                            rotated_image = new_image.rotate(180)
                        case 3:
                            rotated_image = new_image.rotate(90)

                    new_image = ImageOps.fit(rotated_image, self.size)

                    map_image.paste(new_image, offset)

        map_image.save(Path(__file__).parent.parent / "generated.png", "PNG")
