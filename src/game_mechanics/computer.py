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


    def move_to_player_units(self,player_units):

        #testing: finding closest unit.


        print("")