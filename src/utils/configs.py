import pygame
from src.utils.assets import Assets
font_assets = Assets()
font_assets.load_fonts()

class Configs:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720


    #board
    TILESIZE = 32
    GRID_WIDTH = 480
    GRID_HEIGHT = 480
    # user specific window sizes
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
