import pygame
pygame.init()
from collections import deque
from src.utils.assets import Assets
from src.utils.configs import Configs
from src.game_mechanics.unit import Unit
from src.utils.text import Text
class Tile:
    def __init__(self,X,Y, display):
        self.board_assets = Assets()
        self.board_assets.load_boardsprites()
        #note to future self:
        #All math variables for pathfinding algorithm will be stored inside Tile as it is relative to tile.

        #game properties
        self.x = X
        self.y = Y
        self.current_unit = Unit()
        self.type = "Regular"
        self.ownership = "Free"

        #base point properties
        self.base_neighbours = []
        self.base_registered = False
        self.base_highlight = False


        #pathfinding properties
        self.g_value = 0
        self.h_value = 0
        self.f_value = 0 #will be updated to be sum of g and h
        self.traversable = True
        self.parent = None
        self.neighbours = []

        #display orientations
        self.display = display

        #Pixel position relative to board
        self.blitposx = self.x * Configs.TILESIZE
        self.blitposy = self.y * Configs.TILESIZE
        #toggle debug
        self.vdebug = False

        #default image
        self.tile_image = self.board_assets.get_sprite("tile").convert_alpha()
        self.tile_image = pygame.transform.scale(self.tile_image, (Configs.TILESIZE,Configs.TILESIZE))

        #hover image
        self.tile_image_hover = self.board_assets.get_sprite("tile_hover").convert_alpha()
        self.tile_image_hover = pygame.transform.scale(self.tile_image_hover,(Configs.TILESIZE, Configs.TILESIZE))

        #Wall image
        self.tile_image_wall = self.board_assets.get_sprite("wall").convert_alpha()
        self.tile_image_wall = pygame.transform.scale(self.tile_image_wall, (Configs.TILESIZE, Configs.TILESIZE))

        #initialise default image
        self.active_image = self.tile_image
        self.tile_rect = self.tile_image.get_rect()

        #final display image after processing
        #maintain original images for different image states after blitting
        self.final_image = self.active_image.copy()

        # Set tile_rect position relative to sprite
        self.tile_rect.topleft = (self.blitposx, self.blitposy)

        #visual display information
        self.visual_x = Text(f"{self.x}", 22, Configs.GRAY, 10, Configs.TILESIZE-10)
        self.visual_y = Text(f"{self.y}", 22, Configs.GRAY, Configs.TILESIZE - 10, Configs.TILESIZE-10)


    #debug
    def detail(self):
        print(f"Tile[{self.x},{self.y}]\n   type: {self.type}\n    UnitType: {self.current_unit.UnitType}")
    #Add to board
    def blit_to_board(self, _board):
        _board.blit(self.final_image, (self.blitposx, self.blitposy))

    #Init Wall
    def set_wall(self):
        self.traversable = False
        self.type = "Wall"
        self.active_image = self.tile_image_wall
        self.blank_text()
        self.update_visual()
    def set_base_point(self,owner):
        base_point_image = self.tile_image
        match owner:
            case "Player":
                self.ownership = "Player"
                base_point_image = self.board_assets.get_sprite("PlayerBasePoint")
            case "Computer":
                self.ownership = "Computer"
                base_point_image = self.board_assets.get_sprite("ComputerBasePoint")
        self.traversable = False
        self.type = "BasePoint"
        self.active_image = base_point_image
        self.blank_text()
        self.update_visual()


    def blank_text(self):
        self.visual_x.update_text("")
        self.visual_y.update_text("")

    #check clicked
    def clicked(self, event, board_x, board_y):
        adjusted_rect = pygame.Rect(self.blitposx + board_x, self.blitposy + board_y, Configs.TILESIZE, Configs.TILESIZE)
        if event.type == pygame.MOUSEBUTTONDOWN and adjusted_rect.collidepoint(event.pos):
            return True
        return False

    #check hover and highlight
    def mouse_hover(self, mouse_pos, board_x, board_y):
        if self.base_registered:
            if self.base_highlight:
                return
            adjusted_rect = pygame.Rect(self.blitposx + board_x, self.blitposy + board_y, Configs.TILESIZE,Configs.TILESIZE)
            if adjusted_rect.collidepoint(mouse_pos):
                self.activate_highlight()
            else:
                self.deactivate_highlight()
        if not self.type == "wall":
            adjusted_rect = pygame.Rect(self.blitposx + board_x, self.blitposy + board_y, Configs.TILESIZE, Configs.TILESIZE)
            if adjusted_rect.collidepoint(mouse_pos):
                self.activate_highlight()
            else:
                self.deactivate_highlight()
    #unit handling
    def add_unit(self, unit):
        if self.traversable:
            self.current_unit = unit # Assign unit to tile
            self.lock()

    def remove_unit(self):
        self.current_unit = Unit()
        self.unlock()


    #path finding
    def clear(self):
        self.g_value = 0
        self.h_value = 0
        self.f_value = 0
        self.parent = None
        self.neighbours.clear()

    def lock(self):
        self.traversable = False

    def unlock(self):
        self.traversable = True

    def set_parent(self,new_parent):
        self.parent = new_parent

    def get_neighbours(self, board_array):
        if self.neighbours:
            return
        directions = [
            (-1, 0),( 1, 0),(0, 1),(0,-1),
            (-1,-1),( 1, 1),( 1,-1),(-1, 1)
        ]

        for dx,dy in directions:
            neighbour_x = self.x + dx
            neighbour_y = self.y + dy
            if 0 <= neighbour_x < 15 and 0 <= neighbour_y < 15:
                neighbour = board_array[neighbour_y][neighbour_x]
                if neighbour.traversable:
                    self.neighbours.append(neighbour)
    def set_base_neighbours(self, board_array):
        if self.base_neighbours:
            return
        directions = [
            (-1, 0),( 1, 0),(0, 1),(0,-1),
            (-1,-1),( 1, 1),( 1,-1),(-1, 1)
        ]

        for dx,dy in directions:
            neighbour_x = self.x + dx
            neighbour_y = self.y + dy
            if 0 <= neighbour_x < 15 and 0 <= neighbour_y < 15:
                neighbour = board_array[neighbour_y][neighbour_x]
                neighbour.base_registered = True
                self.base_neighbours.append(neighbour)

    #visuals
    def visual_debug(self):
        self.vdebug = True
        if self.vdebug:
            self.active_image = self.tile_image_hover
            self.update_visual()

    def visual_debug_click(self):
        self.vdebug = not self.vdebug
        if self.vdebug and self.type == "":
            self.active_image = self.tile_image_hover
            self.update_visual() #render unit
        elif not self.vdebug and self.type == "":
            self.active_image = self.tile_image
            self.update_visual() #render unit


    #base tile functions
    def activate_neighbour_highlights(self):
        for tile in self.base_neighbours:
            tile.activate_highlight()
            self.base_highlight = True
            tile.detail()
    def deactivate_neighbour_highlights(self):
        for tile in self.base_neighbours:
            tile.deactivate_highlight()
            self.base_highlight = False
            tile.detail()

    def activate_highlight(self):
        #for base tile neighbours
        self.vdebug = True
        if self.vdebug:
            self.active_image = self.tile_image_hover
            self.update_visual()  # render unit

    def deactivate_highlight(self):
        # for base tile neighbours
        self.vdebug = False
        if not self.vdebug:
            self.active_image = self.tile_image
            self.update_visual()  # render unit



    def update_visual(self):
        self.visual_x.draw(self.active_image)
        self.visual_y.draw(self.active_image)
        self.final_image = self.active_image.copy()
        if self.current_unit.UnitType != "blank":
            self.current_unit.draw(self.final_image) # Draw unit onto tile
