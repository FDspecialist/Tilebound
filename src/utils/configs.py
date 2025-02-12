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

#debugging
test_unit = Configs.UNIT_POOL.get_unit()
print(test_unit.Description)