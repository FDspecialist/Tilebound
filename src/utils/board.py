import pygame
from src.utils.tile import Tile
from src.utils.configs import Configs
Configs = Configs()
class Board:
    def __init__(self):
        #properties
        self.array = []

        #board_base, can change to a different sprite later
        self.base = pygame.surface.Surface((Configs.GRID_WIDTH,Configs.GRID_HEIGHT))
        self.base.fill((0, 0, 0))
        self.base_rect = self.base.get_rect()

    def draw(self, display):
        display.blit(self.base, (Configs.SCREEN_MIDDLE_X - (self.base_rect.width //2), Configs.SCREEN_MIDDLE_Y - (self.base_rect.width //2)))