import pygame
pygame.init()
from src.utils.assets import Assets
from src.utils.configs import Configs
from src.game_mechanics.tile_menu import TileMenu
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

        #menu UI
        self.menu = TileMenu()

    def blit_to_board(self, _board):
        _board.blit(self.tile_image, (self.blitposx, self.blitposy))




    def clicked(self, event):
        mousepos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self.tile_rect.collidepoint((mousepos[0],mousepos[1])):
            return True
        return False

    def click_function(self, display, mousepos):
        self.menu.open(display, mousepos)


    def visual_debug(self):
        overlay = pygame.surface.Surface(self.tile_image.get_size(),pygame.SRCALPHA)
        overlay.fill((50,50,50,100))
        self.tile_image.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_ADD)

    def draw(self):
        print("")
        #do logic here later, likely used for placing objects on top

