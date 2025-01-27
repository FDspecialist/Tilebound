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

        #Visually attaching Tiles to array.
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)
    def draw(self, display):
        display.blit(self.base, (Configs.SCREEN_MIDDLE_X - (self.base_rect.width //2), Configs.SCREEN_MIDDLE_Y - (self.base_rect.width //2)))



    #Tile operation handling shall exist within board.
    def tile_click_detect(self,event):
        for x in self.array:
            for tile in x:
                if tile.clicked(event):
                    tile.click_function()