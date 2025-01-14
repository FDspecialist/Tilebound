import configs
from assets import Assets
from tile import Tile

class Board:
    def __init__(self):
        #15 x 15 board, each coord holds a tile
        self.array = []