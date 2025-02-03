import pygame
import numpy as np
from src.game_mechanics.tile import Tile
from src.utils.configs import Configs
Configs = Configs()
class Board:
    def __init__(self):
        #properties

        #board_base, can change to a different sprite later
        self.base = pygame.surface.Surface((Configs.GRID_WIDTH,Configs.GRID_HEIGHT))
        self.base.fill((0, 0, 0))
        self.base_rect = self.base.get_rect()



        # ARRAY = [[Tile(x,y) for x in range(15)]for y in range(15)]
        self.array = np.array([[Tile(x, y) for x in range(15)] for y in range(15)])
        self.process_array = []
        #Visually attaching Tiles to array.
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)
    def draw(self, display):
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)
        display.blit(self.base, (Configs.SCREEN_MIDDLE_X - (self.base_rect.width //2), Configs.SCREEN_MIDDLE_Y - (self.base_rect.width //2)))



    #Tile operation handling shall exist within board.
    def tile_click_detect(self,event, display):
        #move all items into temp array
        self.process_array = []
        for x in self.array:
            for tile in x:
                self.process_array.append(tile)

        #iterate through temp array, check for click, then return output if so
        for item in self.process_array:
            if item.clicked(event, display):
                print(f"clicked: [{item.x},{item.y}]")
                return

    def debug_tile(self,X,Y):
        for x in self.array:
            for tile in x:
                if tile.x == X and tile.y == Y:
                    print(f"tile x: {tile.x}\ntile y: {tile.y}")
                    tile.visual_debug()

        boardrows = len(self.array)
        boardcols = len(self.array[0])
        array_size = boardrows * boardcols
        print(f"Board Array size: {boardrows} x {boardcols}\nNumber of tile slots: {array_size}")
        print(f"Temp Array size: {len(self.process_array)}")
