import random
from src.utils.assets import Assets
from src.utils.pathfinder import Pathfinder
from src.utils.minheap import MinHeap
class Unit:
    def __init__(self):

        #Game Properties
        self.UnitType = "blank"
        self.Health = 0
        self.Defence = 0
        self.Attack = 0
        self.AttackRange = 0
        self.MovementRange = 0
        self.Cost = 0
        self.isPlayer = False

        #Descriptional Properties
        self.Description = "blank"
        self.WeaknessDesc = "blank"

        #Pathfinding Properties
        self.Pathfinder = Pathfinder()
        self.target_unit = None


        #Graphics properties
        self.unit_load = Assets()
        self.unit_load.load_boardsprites()

        self.unit_sprite = self.unit_load.get_sprite("tile")

        #Unique position relative to board
        self.x = 0
        self.y = 0

        #debug
        self.ID = ""




    #PATHFINDING
    #============================================Computer=================================================
    def set_target_unit(self,unit):
        if self.target_unit is None:
            self.target_unit = unit
        else:
            self.target_unit = unit

    def find_closest_unit(self,unit_list):
        #complete rework, using hashmap and minheap
        #since it uses a dictionary, which overwrites over already existing keys, the unit
        #will set the closest unit to be the most recently checked unit

        #will set closest unit to target for the foreseeable future

        dist_unit_map = {}
        known_distances = MinHeap("unit") #ensures that popped distance will be the shortest
        shortest_distance = 99
        unit_dist = 99
        for unit in unit_list:
            #find distance between self and unit
            unit_dist = self.Pathfinder.chebyshev_distance(self,unit)
            #link distance to unit (key: distance val: unit)
            dist_unit_map[unit_dist] = unit
            #push distance to minheap and order
            known_distances.push(unit_dist)
            print(f"chebyshev distance: {unit_dist}")

        shortest_distance = known_distances.pop()

        #error handling
        if shortest_distance > 15:
            print("Error: unit exists outside array")
            return

        #set the unit with shortest distance from the map as the target unit.
        self.set_target_unit(dist_unit_map[shortest_distance])







    def move(self,x ,y):
        self.x = x
        self.y = y

    def draw(self, board):
        board.blit(self.unit_sprite, (0,0))

    #pooling essentials
    def activate(self, unit_type, is_player, x, y):
        match unit_type:
            case "Infantry":
                self.UnitType = unit_type
                self.Health = 8
                self.Defence = 2
                self.Attack = 4
                self.AttackRange = 1
                self.MovementRange = 2
                self.Cost = 100
                self.isPlayer = is_player
                self.Description = "Standard foot soldiers, defence stat intends that this unit is intended for holding defensive lines and occupying territory. Bonus defence when adjacent to another allied infantry piece. "
                self.WeaknessDesc = "Low RANGE, Low MOVEMENT RANGE"

                # initial board position
                self.x = x
                self.y = y

                #assign correct unit orientation
                if is_player:
                    self.unit_sprite = self.unit_load.get_sprite("player_infantry").convert_alpha()
                    self.ID = self.ID + unit_type +" PLAYER["+str(x)+","+str(y)+"]"
                else:
                    self.unit_sprite = self.unit_load.get_sprite("computer_infantry").convert_alpha()
                    self.ID = self.ID + unit_type + " COMPUTER[" + str(x) + "," + str(y) + "]"

            case "Archer":
                self.Health = 8
                self.Defence = 0
                self.Attack = 4
                self.AttackRange = 3
                self.MovementRange = 2
                self.Cost = 150
                self.isPlayer = is_player
                self.Description = "Description: Archers, shoot projectiles, range allows for attacking without being attacked in return."
                self.WeaknessDesc = "Weak DEFENCE"
            case "Knight":
                self.Health = 8
                self.Defence = 1
                self.Attack = 5
                self.AttackRange = 1
                self.MovementRange = 3
                self.Cost = 250
                self.isPlayer = is_player
                self.Description = "Mounted infantry, reduced defence for increased movement range. Cavalries excel in damage and speed. Bonus damage to infantry if attacking right after moving. "
                self.WeaknessDesc = "Reduced DAMAGE when stationary, Low DEFENCE"

    def reset(self):
        self.UnitType = "blank"
        self.Health = 0
        self.Defence = 0
        self.Attack = 0
        self.AttackRange = 0
        self.MovementRange = 0
        self.Cost = 0
        self.isPlayer = False
        self.Description = "blank"
        self.WeaknessDesc = "blank"
        self.board_x = 0
        self.board_y = 0



