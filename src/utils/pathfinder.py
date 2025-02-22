import math
from minheap import MinHeap
from stack import Stack
class Pathfinder:
    def __init__(self):
        self.path = Stack()
        self.open_list = MinHeap()
        self.closed_list = []
        self.finished = False


    #moving into chebyshev // document this!!!
    def chebyshev_distance(self, unit1, unit2):
        #This function will calculate the difference between both x and y values of both points
        #both ordinates are compared and the greater ordinate is returned.
        #This is because diagonal movement in Tilebound has a movement cost of only 1.
        x1, y1 = unit1.x,unit1.y
        x2, y2 = unit2.x,unit2.y

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        return max(dx,dy)
    def calculate_f_value(self, current_tile, target_tile):
        #F value = G value + H value
        current_tile.g_value = self.calculate_g_value(current_tile)
        current_tile.h_value = self.calculate_h_value(current_tile, target_tile)
        current_tile.f_value = current_tile.g_value + current_tile.h_value
        return current_tile.f_value
    def calculate_g_value(self,current_tile): # likely logic error here
        if current_tile.parent is None:
            return 0 #hence current tile is the starting tile
        else:
            return current_tile.parent.g_value + 1
    def calculate_h_value(self, current_tile, target_tile):
        #finds Euclidean distance between both tiles.
        h_value = self.chebyshev_distance(current_tile, target_tile)
        return h_value

    def path_to_unit_target(self, unit, array):
        print()
        #A* Path Finding Algorithm here
        target_unit = unit.target_unit[0]
        current_tile = array[unit.x,unit.y]
        target_tile = array[target_unit.x,target_unit.y]

        #starting open list
        current_tile.get_neighbours(array)
        for neighbours in current_tile.get_neighbours:
            neighbours.calculate_current_f_value()

            #then sort into open list as stack








