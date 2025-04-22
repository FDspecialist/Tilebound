class Player:
    def __init__(self, array):
        self.unit_list = []
        self.unit_select = {}

        #pathfinding/board interaction
        self.array = array

        #states
        self.states = {
            "Spawning" : False
        }
        self.activate_state = ""


        #Game Values
        self.unit_count = 0
        self.score = 0
        self.balance = 500
        self.base_tile = None
        self.current_spawn = ""

        #Text
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
    def reset_state(self):
        for key in self.states:
            self.states[key] = False
    def is_busy(self):
        for key in self.states:
            if self.states[key] == True:
                return True
        return False