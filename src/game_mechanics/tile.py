import pygame
pygame.init()
from collections import deque
from src.utils.assets import Assets
from src.utils.configs import Configs
from src.game_mechanics.unit import Unit
from src.utils.text import Text
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
        self.type = ""


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
        self.tile_image = board_assets.get_sprite("tile").convert_alpha()
        self.tile_image = pygame.transform.scale(self.tile_image, (Configs.TILESIZE,Configs.TILESIZE))

        #hover image
        self.tile_image_hover = board_assets.get_sprite("tile_hover").convert_alpha()
        self.tile_image_hover = pygame.transform.scale(self.tile_image_hover,(Configs.TILESIZE, Configs.TILESIZE))

        #Wall image
        self.tile_image_wall = board_assets.get_sprite("wall").convert_alpha()
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



    #Add to board
    def blit_to_board(self, _board):
        _board.blit(self.final_image, (self.blitposx, self.blitposy))

    #Init Wall
    def set_wall(self):
        self.traversable = False
        self.type = "wall"
        self.active_image = self.tile_image_wall
        self.visual_x.update_text("")
        self.visual_y.update_text("")
        self.update_visual()

    #check clicked
    def clicked(self, event, board_x, board_y):
        adjusted_rect = pygame.Rect(self.blitposx + board_x, self.blitposy + board_y, Configs.TILESIZE, Configs.TILESIZE)
        if event.type == pygame.MOUSEBUTTONDOWN and adjusted_rect.collidepoint(event.pos):
            return True
        return False


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

    def get_neighbours(self, board_array, closed_list):
        #check if neighbours list is already populated, prevents accidental duplicates
        if self.neighbours:
            #dont find neighbours again if neighbours already found
            return

        #might only be working for y direction going upwards
        directions = [
            (-1, 0),( 1, 0),(0, 1),(0,-1), #left,right,up,down
            (-1,-1),( 1, 1),( 1,-1),(-1, 1) #downleft,upright,downright,upleft
        ]


        print(f"\nNeighbours of Tile[{self.x},{self.y}]:")
        #check each neighbour for direction
        #while also ignoring neighbours that are not on the array or neighbours that are not traversable or in closed list.
        for dx,dy in directions:
            #neighbour_x,neighbour_y = self.x + dx, self.y + dy
            neighbour_x = self.x + dx
            neighbour_y = self.y + dy
            print(f"\n     Performing: selfx:{self.x} + dx:{dx}, selfy:{self.y} + dy:{dy}")
            # if neighbour exists (within range)
            if 0 <= neighbour_x < 15 and 0 <= neighbour_y < 15:
                neighbour = board_array[neighbour_y][neighbour_x]
                #if neighbour is traversable
                if neighbour.traversable:
                    print(f"     Neighbour[{neighbour.x},{neighbour.y}]")
                    self.neighbours.append(neighbour)
            else:
                print(f"Tile:[{neighbour_x},{neighbour_y}] was found to be invalid")

        #fat error here, neighbours list does NOT get all correct neighbours
        print(f"Neighbours list length: {len(self.neighbours)}")


    #visuals
    def visual_debug(self):
        #print(f"Highlighting Tile[{self.x},{self.y}]")
        self.vdebug = True
        if self.vdebug:
            self.active_image = self.tile_image_hover
            self.update_visual() #render unit
            #print(f"Highlight Tile[{self.x},{self.y}]")

    def visual_debug_click(self):
        self.vdebug = not self.vdebug
        if self.vdebug and self.type == "":
            self.active_image = self.tile_image_hover
            self.update_visual() #render unit
        elif not self.vdebug and self.type == "":
            self.active_image = self.tile_image
            self.update_visual() #render unit
        print(f"Highlight Tile[{self.x},{self.y}]\n     Type: {self.type}\n     Unit: {self.current_unit.UnitType}")


    def update_visual(self):
        self.visual_x.draw(self.active_image)
        self.visual_y.draw(self.active_image)
        self.final_image = self.active_image.copy()
        if self.current_unit.UnitType != "blank":
            self.current_unit.draw(self.final_image) # Draw unit onto tile
