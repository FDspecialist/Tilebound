from src.utils.minheap import MinHeap
from src.utils.stack import Stack
import math
class Pathfinder:
    def __init__(self):
        self.path = Stack()
        self.open_list = MinHeap("tile")
        self.closed_list = []
        self.finished = False
        self.found_target = False

        #debug
        self.rtn_path_debug = []

    def clear(self):
        #I will definitely need this once the computer starts adding new units
        self.path.stack.clear()
        self.open_list.min_heap.clear()
        self.closed_list.clear()
        self.finished = False
        self.found_target = False
        self.rtn_path_debug.clear()


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
        return math.sqrt(dx + dy)

    def euclidean_distance_tile(self, tile1, tile2):
        #This function will calculate the difference between both x and y values of both points
        #both ordinates are compared and the greater ordinate is returned.
        #This is because diagonal movement in Tilebound has a movement cost of only 1.
        x1, y1 = tile1.x,tile1.y
        x2, y2 = tile2.x,tile2.y
        #print(f"Calculating euclidean distance between ({x1},{y1}) and ({x2},{y2})")
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return math.sqrt(dx + dy)
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
        current_tile.h_value = self.euclidean_distance_tile(current_tile, target_tile)

    def path_constructor(self, target_tile):
        #initial current tile
        current_tile = target_tile
        #while current tile parent is not None
        print("\nPATH LIST")
        while not current_tile.parent is None:
            current_tile.visual_debug()
            print(f"     PARENT TILE[{current_tile.parent.x},{current_tile.parent.y}] ---->TILE[{current_tile.x},{current_tile.y}]")
            self.path.push(current_tile)
            self.rtn_path_debug.append(current_tile)
            current_tile = current_tile.parent

    #IMPORTANT:
    #remember to make sure neighbours already in open list are not added again.
    def unit_path_finder(self, unit, array):
        #A* Path Finding Algorithm here
        target_unit = unit.target_object
        current_tile = array[unit.x,unit.y]
        print(f"--Pathfinder init--\n     Start:[{current_tile.x},{current_tile.y}]\n     End:[{target_unit.x},{target_unit.y}]")
        target_tile = array[target_unit.x,target_unit.y]
        #set target_tile to traversable just so that it can be added as neighbour
        target_tile.traversable = True
        self.calculate_f_value(current_tile, target_tile)
        self.open_list.push(current_tile)

        #get neighbours and add to openlist
        while not self.open_list.is_empty():
            #handle target tile being adjacent from beginning
            current_tile = self.open_list.pop()
            print(f"Current Tile: [{current_tile.x},{current_tile.y}]")
            # current_tile.visual_debug()
            if current_tile == target_tile:
                print(f"\nThese two are supposedly the same:\nCURRENT_TILE[{current_tile.x},{current_tile.y}]\nTARGET_TILE[{target_tile.x},{target_tile.y}]")
                self.finished = True
                self.found_target = True
                break

            #add current tile to closed list
            #get neighbours,calculate values then add to open list
            self.closed_list.append(current_tile)
            current_tile.get_neighbours(array, self.closed_list)

            print(f"\nNeighbour A* values:")
            for ntile in current_tile.neighbours:
                if ntile in self.closed_list or not ntile.traversable:
                    continue
                self.calculate_f_value(ntile,target_tile)
                print(f"Tile[{ntile.x},{ntile.y}] F: {ntile.f_value}  G: {ntile.g_value} H: {ntile.h_value}")
                new_g_value = current_tile.g_value + 1
                if ntile not in self.open_list.min_heap or new_g_value < ntile.g_value:
                    ntile.set_parent(current_tile)
                    self.calculate_f_value(ntile, target_tile)
                    if ntile not in self.open_list.min_heap:
                        self.open_list.push(ntile)
        if self.found_target:
            #back track parents here
            self.path_constructor(target_tile)
            size = self.path.size()
            print(f"path found")
            print(f"Size of path: {size}")
            rtn_path = self.path

            #reset everything for next unit
            for x in array:
                for tile in x:
                    tile.clear()
            self.clear()

            return rtn_path
        else:
            self.path_constructor(current_tile)
            size = self.path.size()
            print("Path not found")
            print(f"Size of path: {size}")
            rtn_path = self.path
            # reset everything for next unit
            for x in array:
                for tile in x:
                    tile.clear()
            self.clear()
            return rtn_path


    def rtn_path_list(self):
        print("\nPATH LIST: ")
        for tile in self.rtn_path_debug:
            print(f"     Tile[{tile.x},{tile.y}]")
