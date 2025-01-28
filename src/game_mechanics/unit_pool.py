from src.game_mechanics.unit import Unit
from src.utils.stack import Stack


class UnitPool:
    def __init__(self):
        self.unit_pool = Stack()
        index = 225
        while index != 0:
            blank_unit = Unit()
            self.unit_pool.push(blank_unit)
            index -= 1
        print(f"UnitPool size: {self.unit_pool.size()}")