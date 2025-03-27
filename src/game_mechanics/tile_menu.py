import pygame
pygame.init()
from src.utils.configs import Configs
from src.utils.button import Button
class TileMenu:
    def __init__(self):
        self.image = pygame.surface.Surface((55, 150))
        self.image.fill(Configs.BLACK)
        self.active = False

        self.x = 0
        self.y = 0
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (self.x,self.y)

    def activate(self, tx, ty):
        self.x = tx
        self.y = ty
        self.active = True

    def deactivate(self):
        self.active = False

    def update_pos(self,nx, ny):
        self.x = nx
        self.y = ny

    def handle_buttons(self):
        #return a string determining which button was pressed.
        pass
    def blit_to(self, display):
        display.blit(self.image,self.image_rect)