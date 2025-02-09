import pygame

class TileMenu:
    def __init__(self):
        self.image = pygame.surface.Surface((55, 150))
        self.image.fill((255,255,255))

    def draw(self, display, mousepos):
        display.blit(self.image, (mousepos[0], mousepos[1]))