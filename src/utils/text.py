import pygame
pygame.init()
from src.utils.assets import Assets
from src.utils.configs import Configs
class Text:
    def __init__(self, text, size, colour, x, y):
        self.font_assets = Assets()
        self.font_assets.load_fonts()


        self.text = text
        self.size = size
        self.colour = colour
        self.font = self.font_assets.get_font(Configs.DEFAULT_FONT, self.size)
        self.text_surface = self.font.render(self.text, True, self.colour)
        self.x = x
        self.y = y
        self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))

    def update_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.colour)
        self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))

    def draw(self, display):
        display.blit(self.text_surface, self.text_rect)

