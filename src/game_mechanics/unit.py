import pygame
from src.utils.assets import Assets

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

        #Graphics properties
        self.unit_load = Assets()
        self.unit_load.load_boardsprites()

        self.unit_sprite = self.unit_load.get_sprite("tile")

        #Unique position relative to board
        self.x = 0
        self.y = 0





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
                self.board_x = x
                self.board_y = y


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



