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
        self.target_object = None # Set to target 'object' as this can either be a control point, or an enemy unit.

        #Graphics properties
        self.unit_load = Assets()
        self.unit_load.load_boardsprites()

        self.unit_sprite = self.unit_load.get_sprite("tile")

        #Unique position relative to board
        self.x = 0
        self.y = 0

        #debug

        #rework ID later, current methods allows for identical IDs.
        self.ID = ""




    #PATHFINDING
    #============================================Computer=================================================
    def set_target_object(self, obj):
        if self.target_object is None:
            self.target_object = obj
        else:
            self.target_object = obj

    def find_closest_object(self,object_list):
        #complete rework, using hashmap and minheap
        #since it uses a dictionary, which overwrites over already existing keys, the unit
        #will set the closest object to be the most recently checked object
        #will set closest object to target for the foreseeable future

        dist_obj_map = {}
        known_distances = MinHeap("unit") #ensures that popped distance will be the shortest
        shortest_distance = 99
        obj_dist = 99
        for obj in object_list:
            #find distance between self and obj
            obj_dist = self.Pathfinder.euclidean_distance(self,obj)
            #link distance to obj (key: distance val: obj)
            dist_obj_map[obj_dist] = obj
            #push distance to minheap and order
            known_distances.push(obj_dist)
            print(f"euclidean distance: {obj_dist}")

        shortest_distance = known_distances.pop()

        #error handling
        if shortest_distance > 15:
            print("Error: unit exists outside array")
            return

        #set the unit with shortest distance from the map as the target object.
        self.set_target_object(dist_obj_map[shortest_distance])

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
                    self.unit_sprite = self.unit_load.get_sprite("PlayerInfantry").convert_alpha()
                    self.ID = self.ID + unit_type +" PLAYER["+str(x)+","+str(y)+"]" #bad since ID can change
                else:
                    self.unit_sprite = self.unit_load.get_sprite("ComputerInfantry").convert_alpha()
                    self.ID = self.ID + unit_type + " COMPUTER[" + str(x) + "," + str(y) + "]" #bad since ID can change

            case "Archer":
                self.UnitType = unit_type
                self.Health = 8
                self.Defence = 0
                self.Attack = 4
                self.AttackRange = 3
                self.MovementRange = 2
                self.Cost = 150
                self.isPlayer = is_player
                self.Description = "Description: Archers, shoot projectiles, range allows for attacking without being attacked in return."
                self.WeaknessDesc = "Weak DEFENCE"

                # initial board position
                self.x = x
                self.y = y

                if is_player:
                    self.unit_sprite = self.unit_load.get_sprite("PlayerArcher").convert_alpha()
                    self.ID = self.ID + unit_type +" PLAYER["+str(x)+","+str(y)+"]"
                else:
                    self.unit_sprite = self.unit_load.get_sprite("ComputerArcher").convert_alpha()
                    self.ID = self.ID + unit_type + " COMPUTER[" + str(x) + "," + str(y) + "]"
            case "Knight":
                self.UnitType = unit_type
                self.Health = 8
                self.Defence = 1
                self.Attack = 5
                self.AttackRange = 1
                self.MovementRange = 3
                self.Cost = 250
                self.isPlayer = is_player
                self.Description = "Mounted infantry, reduced defence for increased movement range. Cavalries excel in damage and speed. Bonus damage to infantry if attacking right after moving. "
                self.WeaknessDesc = "Reduced DAMAGE when stationary, Low DEFENCE"

                # initial board position
                self.x = x
                self.y = y

                if is_player:
                    self.unit_sprite = self.unit_load.get_sprite("PlayerKnight").convert_alpha()
                    self.ID = self.ID + unit_type + " PLAYER[" + str(x) + "," + str(y) + "]"
                else:
                    self.unit_sprite = self.unit_load.get_sprite("ComputerKnight").convert_alpha()
                    self.ID = self.ID + unit_type + " COMPUTER[" + str(x) + "," + str(y) + "]"

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



