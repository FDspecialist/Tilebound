import pygame
from src.utils.assets import Assets
from src.game_mechanics.unit_pool import UnitPool
font_assets = Assets()
font_assets.load_fonts()

class Configs:
    #relative my personal machine c:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    #colour
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    LIGHT_BLUE = (0,200,255)
    GRAY = (125,125,125)
    BLACK = (0,0,0)

    #Unit Pool
    UNIT_POOL = UnitPool()



    #board
    TILESIZE = 48
    GRID_WIDTH = 720
    GRID_HEIGHT = 720

    # user specific window sizes
    info = pygame.display.Info()
    USER_WIDTH = info.current_w
    USER_HEIGHT = info.current_h

    #Positioning in relation to dimensions of screen
    SCREEN_MIDDLE_X = USER_WIDTH / 2  # Set to x to align with horizontal half line
    SCREEN_MIDDLE_Y = USER_HEIGHT / 2 # Set to y to align with vertical half line
    FPS = 60

    #font constant
    DEFAULT_FONT = 'Pixel Digivolve'


    #Unit Stats

    INFANTRY_STATS = {
        "Health": 8,
        "Defence": 2,
        "Attack": 4,
        "AttackRange": 1,
        "MovementRange": 2,
        "Cost": 100,
        "Description": (
            "Standard foot soldiers, defence stat intends that this unit is intended "
            "for holding defensive lines and occupying territory. Bonus defence when "
            "adjacent to another allied infantry piece."
        ),
        "WeaknessDesc": "Low RANGE, Low MOVEMENT RANGE"
    }

    ARCHER_STATS = {
        "Health": 8,
        "Defence": 0,
        "Attack": 4,
        "AttackRange": 3,
        "MovementRange": 2,
        "Cost": 150,
        "Description": (
            "Description: Archers, shoot projectiles, range allows for attacking without being attacked in return."
        ),
        "WeaknessDesc": "Weak DEFENCE"
    }

    KNIGHT_STATS = {
        "Health": 8,
        "Defence": 1,
        "Attack": 5,
        "AttackRange": 1,
        "MovementRange": 3,
        "Cost": 250,
        "Description": (
            "Mounted infantry, reduced defence for increased movement range. Cavalries excel in damage and speed. "
            "Bonus damage to infantry if attacking right after moving."
        ),
        "WeaknessDesc": "Reduced DAMAGE when stationary, Low DEFENCE"
    }

    UNIT_STATS = {
        "Infantry" : INFANTRY_STATS,
        "Archer" : ARCHER_STATS,
        "Knight" : KNIGHT_STATS
    }

#debugging
test_unit = Configs.UNIT_POOL.get_unit()
print(test_unit.Description)

infantry_description = Configs.UNIT_STATS["Knight"]["Health"]
print(f"\n{infantry_description}")