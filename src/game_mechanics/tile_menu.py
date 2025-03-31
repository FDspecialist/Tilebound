import pygame
pygame.init()
from src.utils.configs import Configs
from src.utils.button import Button
class TileMenu:
    def __init__(self):
        self.image = pygame.surface.Surface((225,150))
        self.image.fill(Configs.BLACK)
        self.active = False

        self.x = 0
        self.y = 0
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (self.x,self.y)

        #text, size, width, height, x, y
        self.spawn_unit_btn = Button("Spawn Unit", 20, 255,50, 126, 25)
        self.spawn_enemy_btn = Button("Spawn Enemy", 20, 255, 50, 126, 75)
        self.manual_debug_btn = Button("Manual Debug", 20, 255, 50, 126, 125)
        self.buttons = [
            #0
            self.spawn_unit_btn,
            #1
            self.spawn_enemy_btn,
            #2
            self.manual_debug_btn
        ]

    def activate(self, tx, ty):
        self.x = tx
        self.y = ty
        self.image_rect.topleft = (self.x, self.y)
        self.active = True

    def deactivate(self):
        self.active = False

    def responsive(self, event):
        #return a string determining which button was pressed.
        index_tracker = 0
        for button in self.buttons:
            if button.is_clicked(event):
                return index_tracker
            index_tracker = index_tracker + 1
    def blit_to(self, display):
        for button in self.buttons:
            button.draw(self.image)
        display.blit(self.image,self.image_rect)