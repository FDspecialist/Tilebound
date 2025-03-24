import pygame
pygame.init()
from collections import deque
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

        #initialise default image
        self.active_image = self.tile_image
        self.tile_rect = self.tile_image.get_rect()

        # Set tile_rect position relative to sprite
        self.tile_rect.topleft = (self.blitposx, self.blitposy)


        #menu UI
        self.menu = TileMenu()


    #initialisation
    def blit_to_board(self, _board):
        _board.blit(self.active_image, (self.blitposx, self.blitposy))



    def clicked(self, event, board_x, board_y):
        adjusted_rect = pygame.Rect(self.blitposx + board_x, self.blitposy + board_y, Configs.TILESIZE, Configs.TILESIZE)
        if event.type == pygame.MOUSEBUTTONDOWN and adjusted_rect.collidepoint(event.pos):
            return True
        return False



    def add_unit(self, unit):
        if self.traversable:
            self.current_unit = unit # Assign unit to tile
            self.lock()
        else:
            print(f"Tile[{self.x},{self.y}] is locked")
    def remove_unit(self):
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
                neighbour = board_array[neighbour_x,neighbour_y]
                #if neighbour is traversable
                if neighbour.traversable:
                    print(f"     Neighbour[{neighbour.x},{neighbour.y}]")
                    self.neighbours.append(neighbour)
            else:
                print(f"Tile:[{neighbour_x},{neighbour_y}] was found to be invalid")

        #fat error here, neighbours list does NOT get all correct neighbours
        print(f"Neighbours list length: {len(self.neighbours)}")

    #BSF IMPLEMENTATION probably wont keep this tbf, may not work on square tiled board.
    # def get_neighbours(self, board_array, closed_list):
    #     self.neighbours = []  # Reset neighbors
    #
    #     # Define movement directions (8-way movement for Chebyshev distance)
    #     directions = [
    #         (-1, 0), (1, 0), (0, 1), (0, -1),  # Left, Right, Up, Down
    #         (-1, -1), (1, 1), (1, -1), (-1, 1)  # Diagonals
    #     ]
    #
    #     # BFS queue to explore valid neighbors
    #     queue = deque([(self.x, self.y)])  # Start from current tile
    #     visited = set()  # Keep track of visited tiles
    #
    #     print(f"\nNeighbour of Tile:[{self.x},{self.y}]:")
    #     while queue:
    #         x, y = queue.popleft()  # Get the next tile
    #
    #         for dx, dy in directions:
    #             nx, ny = x + dx, y + dy  # New neighbor coordinates
    #
    #             # Ensure within board bounds
    #             if 0 <= nx < len(board_array) and 0 <= ny < len(board_array[0]):
    #                 neighbour = board_array[nx][ny]  # Get tile object
    #
    #                 # Check if neighbor is valid and not visited
    #                 if neighbour.traversable and neighbour not in closed_list and neighbour not in visited:
    #                     print(f"     Neighbour[{neighbour.x},{neighbour.y}]")
    #                     self.neighbours.append(neighbour)
    #                     visited.add(neighbour)  # Mark as visited
    #                     queue.append((nx, ny))  # Continue exploring






    def visual_debug(self):
        print(f"Highlighting Tile[{self.x},{self.y}]")
        self.vdebug = not self.vdebug
        if self.vdebug:
            self.active_image = self.tile_image_hover
            self.update_visual() #render unit
        else:
            self.active_image = self.tile_image
            self.update_visual() # render unit



    def update_visual(self):
        if self.current_unit.UnitType != "blank":
            self.current_unit.draw(self.active_image) # Draw unit onto tile
