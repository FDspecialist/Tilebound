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

        #Unique position relative to board
        self.board_x = 0
        self.board_y = 0






    #pooling essentials
    def activate(self, _unitType):
        match _unitType:
            case "Infantry":
                self.UnitType = _unitType
                self.Health = 8
                self.Defence = 2
                self.Attack = 4
                self.AttackRange = 1
                self.MovementRange = 2
                self.Cost = 100
                self.Description = "Standard foot soldiers, defence stat intends that this unit is intended for holding defensive lines and occupying territory. Bonus defence when adjacent to another allied infantry piece. "
                self.WeaknessDesc = "Low RANGE, Low MOVEMENT RANGE"
            case "Archer":
                self.Health = 8
                self.Defence = 0
                self.Attack = 4
                self.AttackRange = 3
                self.MovementRange = 2
                self.Cost = 150
                self.Description = "Description: Archers, shoot projectiles, range allows for attacking without being attacked in return."
                self.WeaknessDesc = "Weak DEFENCE"
            case "Knight":
                self.Health = 8
                self.Defence = 1
                self.Attack = 5
                self.AttackRange = 1
                self.MovementRange = 3
                self.Cost = 250
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



