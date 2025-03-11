import math
from src.utils.minheap import MinHeap
from src.utils.stack import Stack
class Pathfinder:
    def __init__(self):
        self.path = Stack()
        self.open_list = MinHeap("tile")
        self.closed_list = []
        self.finished = False

    def clear(self):
        #not sure if i need this yet


    #moving into chebyshev // document this!!!
    #Pathfinding Handler
    def chebyshev_distance(self, unit1, unit2):
        #This function will calculate the difference between both x and y values of both points
        #both ordinates are compared and the greater ordinate is returned.
        #This is because diagonal movement in Tilebound has a movement cost of only 1.
        x1, y1 = unit1.x,unit1.y
        x2, y2 = unit2.x,unit2.y
        print(f"Calculating Chebyshev distance between ({unit1.ID}) and ({unit2.ID})")
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        #returns the greater value between dx and dy
        return max(dx,dy)

    def chebyshev_distance_tile(self, tile1, tile2):
        #This function will calculate the difference between both x and y values of both points
        #both ordinates are compared and the greater ordinate is returned.
        #This is because diagonal movement in Tilebound has a movement cost of only 1.
        x1, y1 = tile1.x,tile1.y
        x2, y2 = tile2.x,tile2.y
        print(f"Calculating Chebyshev distance between ({x1},{y1}) and ({x2},{y2})")
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return max(dx,dy)
    def calculate_f_value(self, current_tile, target_tile):
        #F value = G value + H value
        #assign values to instance of current_tile
        self.calculate_g_value(current_tile)
        self.calculate_h_value(current_tile, target_tile)
        current_tile.f_value = current_tile.g_value + current_tile.h_value
    def calculate_g_value(self,current_tile): # likely logic error here
        if current_tile.parent is None:
            current_tile.g_value = 0
        else:
            current_tile.g_value = current_tile.parent.g_value + 1
    def calculate_h_value(self, current_tile, target_tile):
        #finds Euclidean distance between both tiles.
        current_tile.h_value = self.chebyshev_distance_tile(current_tile, target_tile)


    #IMPORTANT:
    #remember to make sure neighbours already in open list are not added again.
    def path_to_unit_target(self, unit, array):
        print()
        #A* Path Finding Algorithm here
        target_unit = unit.target_unit
        current_tile = array[unit.x,unit.y]
        target_tile = array[target_unit.x,target_unit.y]

        self.calculate_f_value(current_tile)
        self.open_list.push(current_tile)

