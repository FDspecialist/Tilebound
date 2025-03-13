class Computer:
    def __init__(self,array):
        self.unit_list = []
        self.unit_select = {}
        self.unit_count = 0

        #pathfinding/board interaction
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


    def move_units_to_enemy(self,player_units):
        #foreach unit:
        #   find target unit
        #   find path to target
        #   move (last action before end of unit turn)
        #   if adjacent to target then dont do anything move

        #only do function if both player and computer have units.
        if len(self.unit_list) == 0 or len(player_units) == 0:
            return

        for unit in self.unit_list:
            unit.find_closest_object(player_units)
            print(unit.target_object.ID)

