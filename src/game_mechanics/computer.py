from src.utils.pathfinder import Pathfinder

class Computer:
    def __init__(self,array):
        self.unit_list = []
        self.unit_select = {}
        self.unit_count = 0

        #pathfinding/board interaction
        self.pathfinder = Pathfinder()
        self.array = array
    def assign_unit(self, unit):
        self.unit_list.append(unit)
        self.unit_select[(unit.x,unit.y)] = unit
        self.unit_count = len(self.unit_list)
    def remove_unit(self,unit,x,y):
        self.unit_list.remove(unit)
        self.unit_select[(x,y)] = None
        self.unit_count = len(self.unit_list)
    def get_unit(self,x,y):
        return self.unit_select[(x,y)]

    def update_unit_pos(self,unit,array):
        #had to invert x and y here
        array[unit.y,unit.x].add_unit(unit)

    def move_units_to_enemy(self,player_units, array):
        #foreach unit:
        #   find target unit
        #   find path to target
        #   move (last action before end of unit turn)
        #   if adjacent to target then dont do anything move

        #only do function if both player and computer have units.
        if len(self.unit_list) == 0 or len(player_units) == 0:
            return

        path = []
        #temp commented for now
        for unit in self.unit_list:
            print("For this unit")
            unit.find_closest_object(player_units)
            path = self.pathfinder.unit_path_finder(unit, self.array)
            steps = unit.MovementRange
            distance = len(path)
            hold_position = False
            index = 0
            #disable for path showcase:
            #==0
            if distance == 0:
                #hold position
                hold_position = True
            elif distance <= steps:
                index = steps - distance
                #shorter distance
            else:
                index = distance - steps

            if hold_position:
                #not moving
                continue
            row = unit.x
            col = unit.y
            array[col, row].remove_unit()
            array[col, row].update_visual()
            index = distance - steps
            destination_tile = path[index]

            print(f"Tile at index {steps}: TILE[{path[index].x},{path[index].y})")

            # set new x and y for unit, and update new tile
            unit.move(destination_tile.x, destination_tile.y)
            self.update_unit_pos(unit, array)
            #==1