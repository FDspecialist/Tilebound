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
        #toggle debug
        self.vdebug = False

        #default image
        self.tile_image = board_assets.get_sprite("tile").convert_alpha()
        self.tile_image = pygame.transform.scale(self.tile_image, (Configs.TILESIZE,Configs.TILESIZE))

        #hover image
        self.tile_image_hover = board_assets.get_sprite("tile_hover").convert_alpha()
        self.tile_image_hover = pygame.transform.scale(self.tile_image_hover,(Configs.TILESIZE, Configs.TILESIZE))

        #initialise default image
        self.active_image = self.tile_image
        self.tile_rect = self.tile_image.get_rect()

        # Set tile_rect position relative to sprite
        self.tile_rect.topleft = (self.blitposx, self.blitposy)


        #menu UI
        self.menu = TileMenu()

    def blit_to_board(self, _board):
        _board.blit(self.active_image, (self.blitposx, self.blitposy))


    def clicked(self, event, board_x, board_y):
        adjusted_rect = pygame.Rect(self.blitposx + board_x, self.blitposy + board_y, Configs.TILESIZE, Configs.TILESIZE)
        if event.type == pygame.MOUSEBUTTONDOWN and adjusted_rect.collidepoint(event.pos):
            print(f"clicked on [{self.x},{self.y}]")
            return True
        return False


    def visual_debug(self):
        self.vdebug = not self.vdebug
        if self.vdebug:
            self.active_image = self.tile_image_hover
        else:
            self.active_image = self.tile_image


    def draw(self):
        print("")
        #do logic here later, likely used for placing objects on top
