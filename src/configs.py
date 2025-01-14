import pygame
from assets import Assets
font_assets = Assets()
font_assets.load_fonts()


#game constants (default settings)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

BOARD_WIDTH = 15
BOARD_HEIGHT = 15

# user specific window sizes
info = pygame.display.Info()
USER_WIDTH = 1280
USER_HEIGHT = 768
#1280
#768
#Positioning in relation to dimensions of screen
SCREEN_MIDDLE_X = USER_WIDTH / 2 # Set to x to align with horizontal half line
SCREEN_MIDDLE_Y = USER_HEIGHT / 2# Set to y to align with vertical half line
FPS = 60

#font constant
DEFAULT_FONT = 'Pixel Digivolve'
