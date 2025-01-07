import pygame
from assets import Assets
font_assets = Assets()
font_assets.load_fonts()

#game constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360
# user specific window sizes
info = pygame.display.Info()
USER_WIDTH = 1280 #info.current_w
USER_HEIGHT = 768 #info.current_h
# in case of reset
#1280
#729
SCREEN_MIDDLE_X = SCREEN_WIDTH / 2 # Set to x to align with horizontal half line
SCREEN_MIDDLE_Y = SCREEN_HEIGHT / 2# Set to y to align with vertical half line
FPS = 60

#font constant
DEFAULT_FONT = 'Pixel Digivolve'

#ignore, updat later
# LAST SUCCESSFUL VERSION
# DATE: 04/01/2025
# TIME: 17:12
# NOTES: Currently allows the programmer to switch screens (NOT DYNAMIC)