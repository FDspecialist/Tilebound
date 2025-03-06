import random
from src.utils.assets import Assets
from src.utils.pathfinder import Pathfinder
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




    #PATHFINDING
    #============================================Computer=================================================
    def set_target_unit(self,unit):
        if self.target_unit is None:
            self.target_unit = unit
        else:
            self.target_unit = unit

    def find_closest_unit(self,unit_list):
        #becareful with implementing this:
        #each time this function is called, target unit is likely to be changed
        #make sure an objective is achieved before calling again for the instance of the unit.

        #finds the closest unit from unit_list to current instance of unit
        shortest_distance = 19.8 # initially set to largest possible distance for 15x15
        closest_units = []
        closest_unit = None
        for unit in unit_list:
            #find distance with current unit
            current_distance = self.Pathfinder.chebyshev_distance(self,unit)
            print(f"instance x and y: {self.x}, {self.y}\ncompared x and y: {unit.x}, {unit.y}")
            print(current_distance)

            #when shorter distance found save distance and unit
            if current_distance < shortest_distance:
                shortest_distance = current_distance
                closest_units.append(unit)
            elif current_distance == shortest_distance:
                closest_units.append(unit)

        if len(closest_units) == 1:
            closest_unit = closest_units[0]
        else:
            select_random = random.randint(0, len(closest_units)-1)
            print(f"\n\nrandom index: {select_random}\nclosest_units length: {len(closest_units)-1}\n\n")
            closest_unit = closest_units[select_random]

        print(f"Closest unit to unit[{self.x},{self.y}] is unit[{closest_unit.x},{closest_unit.y}]")
        self.set_target_unit(closest_unit)

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

                #assign correct unit orientation
                if is_player:
                    self.unit_sprite = self.unit_load.get_sprite("player_infantry").convert_alpha()
                else:
                    self.unit_sprite = self.unit_load.get_sprite("computer_infantry").convert_alpha()

                #initial board position
                self.x = x
                self.y = y


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



