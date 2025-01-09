import pygame
from assets import Assets
font_assets = Assets()
font_assets.load_fonts()


#game constants
SCREEN_WIDTH = 640 * 2
SCREEN_HEIGHT = 360 * 2


# user specific window sizes
info = pygame.display.Info()
USER_WIDTH = 1280 #info.current_w
USER_HEIGHT = 768 #info.current_h

#Positioning in relation to dimensions of screen
SCREEN_MIDDLE_X = SCREEN_WIDTH / 2 # Set to x to align with horizontal half line
SCREEN_MIDDLE_Y = SCREEN_HEIGHT / 2# Set to y to align with vertical half line
FPS = 60

#font constant
DEFAULT_FONT = 'Pixel Digivolve'
