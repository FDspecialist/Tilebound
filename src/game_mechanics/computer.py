class Computer:
    def __init__(self):
        self.unit_list = []
        self.unit_select = {}
    def assign_unit(self, unit):
        self.unit_list.append(unit)
        self.unit_select[(unit.x,unit.y)] = unit
    def remove_unit(self,unit,x,y):
        self.unit_list.remove(unit)
        self.unit_select[(x,y)] = None
    def get_unit(self,x,y):
        return self.unit_select[(x,y)]