import pygame
import sys
import configs
from assets import Assets
class GameScreen:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        self.display = _display
        print(f"game_screen screen surface: {self.display}")
        self.ScreenManager = _ScreenManager

        #Load backgorunds
        self.bg_load = Assets()
        self.bg_load.load_backgrounds()

        #background // using main menu bg as placeholder
        self.background = self.bg_load.get_sprite("main_menu").convert_alpha()
        self.background_rect = self.display.get_rect()

    def run(self, event):
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()


        self.display.blit(self.background, self.background_rect)