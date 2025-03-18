from src.utils.minheap import MinHeap
from src.utils.stack import Stack
class Pathfinder:
    def __init__(self):
        self.path = Stack()
        self.open_list = MinHeap("tile")
        self.closed_list = []
        self.finished = False
        self.found_target = False

    def clear(self):
        #I will definitely need this once the computer starts adding new units
        self.path.stack.clear()
        self.open_list.min_heap.clear()
        self.closed_list.clear()
        self.finished = False
        self.found_target = False


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

    def path_constructor(self, target_tile):
        #initial current tile
        current_tile = target_tile
        #while current tile parent is not None
        while not current_tile.parent is None:
            self.path.push(current_tile)
            current_tile = current_tile.parent

    #IMPORTANT:
    #remember to make sure neighbours already in open list are not added again.
    def unit_path_finder(self, unit, array):
        #A* Path Finding Algorithm here
        target_unit = unit.target_object
        current_tile = array[unit.x,unit.y]
        target_tile = array[target_unit.x,target_unit.y]
        #set target_tile to traversable just so that it can be added as neighbour
        target_tile.traversable = True
        self.calculate_f_value(current_tile, target_tile)
        self.open_list.push(current_tile)

        #get neighbours and add to openlist
        while not self.open_list.is_empty():
            current_tile = self.open_list.pop()
            current_tile.visual_debug()
            if current_tile == target_tile:
                self.finished = True
                self.found_target = True
                break

            #add current tile to closed list
            #get neighbours,calculate values then add to open list
            self.closed_list.append(current_tile)
            current_tile.get_neighbours(array, self.closed_list)

            for ntile in current_tile.neighbours:
                if ntile in self.closed_list:
                    continue

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
            print(size)
            print(f"Size of path: {size}")
            rtn_path = self.path
            self.clear()
            return rtn_path
        else:
            self.path_constructor(current_tile)
            size = self.path.size()
            print(f"Size of path: {size}")
            rtn_path = self.path
            self.clear()
            return rtn_path


    def tile_path_finder(self, start_tile, end_tile):
        #for demonstration, put the same algorithm here but adapt for tiles only.
        #only really need to find the target and current tile differently.
        #return path ig???
        #add a flag for this too probably
        pass
