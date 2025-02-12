import pygame
pygame.init()
from src.utils.assets import Assets
from src.utils.configs import Configs
from src.game_mechanics.unit import Unit
from src.game_mechanics.tile_menu import TileMenu
class Tile:
    def __init__(self,X,Y, display):
        board_assets = Assets()
        board_assets.load_boardsprites()
        #note to future self:
        #All math variables for pathfinding algorithm will be stored inside Tile as it is relative to tile.

        #game properties
        self.x = X
        self.y = Y
        self.current_unit = Unit()
        self.traversable = True


        #display orientations
        self.display = display

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
            return True
        return False



    def add_unit(self, unit):
        if self.traversable == True:
            self.current_unit = unit # Assign unit to tile
            self.lock()
        else:
            print(f"Tile[{self.x},{self.y}] is locked")
    def remove_unit(self):
        self.unlock()


    def lock(self):
        self.traversable = False
    def unlock(self):
        self.traversable = True




    def visual_debug(self):
        print(f"Click on Tile[{self.x},{self.y}]")
        self.vdebug = not self.vdebug
        if self.vdebug:
            self.active_image = self.tile_image_hover
            self.update_visual()
        else:
            self.active_image = self.tile_image
            self.update_visual()


    def update_visual(self):
        if self.current_unit.UnitType != "blank":
            self.current_unit.draw(self.active_image) # Draw unit onto tile
