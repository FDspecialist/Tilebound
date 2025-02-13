import math
class Pathfinder:

    def __init__(self):
        self.placeholder = 0

    def euclidean_distance(self, unit1, unit2):
        #formula: d = sqrt((x2 - x1)*2 + (y2- y1)*2)
        x1, y1 = unit1.x,unit1.y
        x2, y2 = unit2.x,unit2.y
        return math.sqrt((x2-x1)**2+(y2-y1**2))
