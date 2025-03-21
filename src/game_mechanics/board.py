import pygame
import numpy as np
from typing import cast
from src.game_mechanics.tile import Tile
from src.game_mechanics.player import Player
from src.game_mechanics.computer import Computer
from src.utils.configs import Configs
Configs = Configs()
class Board:
    def __init__(self, display):
        #board_base, can change to a different sprite later
        self.base = pygame.surface.Surface((Configs.GRID_WIDTH,Configs.GRID_HEIGHT))
        self.base.fill((0, 0, 0))
        self.base_rect = self.base.get_rect()

        # display location
        self.display = display

        self.board_x = (Configs.SCREEN_MIDDLE_X - (self.base_rect.width // 2))
        self.board_y = (Configs.SCREEN_MIDDLE_Y - (self.base_rect.width // 2))


        # ARRAY = [[Tile(x,y) for x in range(15)]for y in range(15)]
        self.array = np.array([[Tile(x, y, self.display) for x in range(15)] for y in range(15)])
        #Visually attaching Tiles to array.
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)

        # game properties
        self.Player = Player(self.array)
        self.Computer = Computer(self.array)


    def check_clicked_debug(self, event):
        for row in range(15):
            for col in range(15):
                tile = cast(Tile, self.array[row,col])
                clicked = tile.clicked(event, self.board_x, self.board_y)
                if clicked:
                    tile.visual_debug()
                    return
    def check_clicked_game(self, event, isPlayer):
        for row in range(15):
            for col in range(15):
                tile = cast(Tile, self.array[row,col])
                clicked = tile.clicked(event, self.board_x, self.board_y)
                if clicked and tile.traversable == True:
                    #spawn infantry for now
                    infantry_unit = Configs.UNIT_POOL.get_unit()
                    infantry_unit.activate("Infantry",isPlayer, tile.x, tile.y)
                    tile.add_unit(infantry_unit)

                    if isPlayer:
                        self.Player.assign_unit(infantry_unit)
                    else:
                        self.Computer.assign_unit(infantry_unit)
                    tile.update_visual()
                    return True
        return False


    def tile(self,x ,y): #python OOP actually sucks this doesn't even work..
        return self.array[x,y]
    def draw(self, display):

        #update tile visuals
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)

        display.blit(self.base, (self.board_x, self.board_y))