import pygame
pygame.init()
from src.utils.assets import Assets
from src.utils.configs import Configs
class Tile:
    def __init__(self,X,Y):
        board_assets = Assets()
        board_assets.load_boardsprites()
        #note to future self:
        #All math variables for pathfinding algorithm will be stored inside Tile as it is relative to tile.
        #properties
        #coordinates relative to board sprite
        #Assignment position
        self.x = X
        self.y = Y
        #Pixel position relative to board
        self.blitposx = self.x * Configs.TILESIZE
        self.blitposy = self.y * Configs.TILESIZE

        #image
        self.tile_image = board_assets.get_sprite("tile").convert_alpha()
        self.tile_image = pygame.transform.scale(self.tile_image, (Configs.TILESIZE,Configs.TILESIZE))
        self.tile_rect = self.tile_image.get_rect()

    def blit_to_board(self, _board):
        _board.blit(self.tile_image, (self.blitposx, self.blitposy))
    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.tile_rect.collidepoint(event.pos):
            print("[tile.py] clicked returns true")
            return True
    def click_function(self):
        print(f"Tile[{self.x},{self.y}]")
    def draw(self):
        print("")
        #do logic here later, likely used for placing objects on top

