from src.utils.assets import Assets
class Tile:
    def __init__(self,X,Y):
        board_assets = Assets()
        board_assets.load_boardsprites()

        #properties

        #coordinates relative to board sprite
        self.x = X
        self.y = Y
        self.tile_image = board_assets.get_sprite("tile").convert_alpha()
        self.tile_rect = self.tile_image.get_rect()

    def draw(self):
        print("")
        #do logic here later


