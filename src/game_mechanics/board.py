import pygame
import numpy as np
from typing import cast
from pygame import SurfaceType

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

        # display location
        self.board_x = (Configs.SCREEN_MIDDLE_X - (self.base_rect.width // 2))
        self.board_y = (Configs.SCREEN_MIDDLE_Y - (self.base_rect.width // 2))


        # ARRAY = [[Tile(x,y) for x in range(15)]for y in range(15)]
        self.array = np.array([[Tile(x, y) for x in range(15)] for y in range(15)])
        #Visually attaching Tiles to array.
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)


    def check_clicked(self, event):
        for row in range(15):
            for col in range(15):
                tile = cast(Tile, self.array[row,col])
                clicked = tile.clicked(event, self.board_x, self.board_y)
                if clicked:
                    tile.visual_debug()
                    return
        # for row in range(len(self.array)):
        #     for col in range(len(self.array)):
        #         tile = cast(Tile, self.array [row,col])
        #         tilex = tile.x
        #         tiley = tile.y
        #         print(f"Check tile [{tilex},{tiley}]")




    def draw(self, display):

        #update tile visuals
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)

        display.blit(self.base, (self.board_x, self.board_y))