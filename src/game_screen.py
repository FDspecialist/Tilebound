import pygame
import configs
import sys
class GameScreen:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        self.display = _display
        self.ScreenManager = _ScreenManager
    def run(self, event):
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
        cover_surface = pygame.Surface((self.display.get_width(), self.display.get_height()))
        cover_surface.fill((0,0,255))
        self.display.blit(cover_surface, cover_surface.get_rect())