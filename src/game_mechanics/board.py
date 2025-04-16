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

        self.selected_tile = None

        # game properties
        self.Player = Player(self.array)
        self.Computer = Computer(self.array)


    def init_structures(self):
        # coordinate list:
        wall_coords = [
            (4, 0), (10, 0), (4, 1), (10, 1), (4, 3), (10, 3), (0, 4), (1, 4), (3, 4), (4, 4), (10, 4), (11, 4),
            (13, 4), (14, 4),
            (6, 5), (7, 5), (8, 5), (5, 6), (9, 6), (5, 7), (9, 7), (5, 8), (9, 8), (6, 9), (7, 9), (8, 9), (0, 10),
            (1, 10), (3, 10),
            (4, 10), (10, 10), (11, 10), (13, 10), (14, 10), (4, 11), (10, 11), (4, 13), (10, 13), (4, 14), (10, 14)
        ]

        for row in range(15):
            for col in range(15):
                tile_coords = (row, col)
                if tile_coords in wall_coords:
                    tile = cast(Tile, self.array[row, col])
                    tile.set_wall()

        #basepoints
        player_base_tile = cast(Tile, self.array[13, 1]) #coords swapped again ;-;
        player_base_tile.set_base_point("Player")
        player_base_tile.set_base_neighbours(self.array)
        self.Player.base_tile = player_base_tile
        enemy_base_tile = cast(Tile, self.array[1, 13])
        enemy_base_tile.set_base_point("Computer")
        enemy_base_tile.set_base_neighbours(self.array)
        self.Computer.base_tile = enemy_base_tile


    def check_clicked_debug(self, event):
        for row in range(15):
            for col in range(15):
                tile = cast(Tile, self.array[row,col])
                clicked = tile.clicked(event, self.board_x, self.board_y)
                if clicked:
                    tile.visual_debug_click()
                    return

    def mouse_hover_highlight(self, mouse_pos):
        for row in range(15):
            for col in range(15):
                tile = cast(Tile, self.array[row,col])
                if tile.type == "Regular":
                    tile.mouse_hover(mouse_pos, self.board_x, self.board_y)

    #template functions:
    #Checks through board, if tile was clicked, return true and assign found tike to current selected tile
    def search_tile(self, event):
        for row in range(15):
            for col in range(15):
                tile = cast(Tile, self.array[row,col])
                clicked = tile.clicked(event, self.board_x, self.board_y)
                if clicked:
                    self.selected_tile = tile
                    return True
        return False

    def update_all(self):
        for row in range(15):
            for col in range(15):
                tile = cast(Tile, self.array[row,col])
                tile.update_visual()




    def draw(self, display):

        #update tile visuals
        for x in self.array:
            for tile in x:
                tile.blit_to_board(self.base)

        display.blit(self.base, (self.board_x, self.board_y))