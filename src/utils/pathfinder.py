import math
class Pathfinder:
    def __init__(self):
        self.open_list = []
        self.closed_list = []
        self.finished = False
    def euclidean_distance(self, unit1, unit2):
        #formula: d = sqrt((x2 - x1)*2 + (y2- y1)*2)
        x1, y1 = unit1.x,unit1.y
        x2, y2 = unit2.x,unit2.y
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
    def calculate_f_value(self, current_tile, target_tile):
        current_tile.g_value = self.calculate_g_value(current_tile, target_tile)
        current_tile.h_value = self.calculate_h_value(current_tile, target_tile)
        current_tile.f_value = current_tile.g_value + current_tile.h_value
        return current_tile.f_value
    def calculate_g_value(self,current_tile, target_tile): # likely logic error here
        if current_tile.parent is None:
            return 0 #hence current tile is the starting tile
        else:
            dx = abs(current_tile.x - target_tile.x)
            dy = abs(current_tile.y - target_tile.y)


            if dx + dy == 1: # hence horizontal or vertical
                return current_tile.g_value + 1
            elif dx == 1 and dy == 1: # hence diagonal
                return current_tile.g_value + 1
            else:
                print("Tiles evaluated are NOT adjacent")
                return -1
    def calculate_h_value(self, current_tile, target_tile):
        h_value = self.euclidean_distance(current_tile, target_tile)
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








