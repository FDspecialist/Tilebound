import pygame
import time
from src.utils.configs import Configs
configs = Configs()
from src.screens.main_menu import MainMenu
from src.screens.game_screen import GameScreen
from src.screens.about_screen import AboutScreen
from src.utils.screen_manager import ScreenManager
class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((configs.USER_WIDTH, configs.USER_HEIGHT))
        self.master_surface = pygame.Surface((configs.USER_WIDTH, configs.USER_HEIGHT))
        pygame.display.set_caption("Tilebound")
        print(f"\nCurrent resolution: {configs.USER_WIDTH},{configs.USER_HEIGHT}\n")

        #full screen logic handling

        self.clock = pygame.time.Clock()
        self.ScreenManager = ScreenManager('main menu')

        #screen init
        self.main_menu = MainMenu(self.master_surface, self.ScreenManager)
        self.game_screen = GameScreen(self.master_surface, self.ScreenManager)
        self.about_screen = AboutScreen(self.master_surface, self.ScreenManager)
        self.screens = {
            'main menu': self.main_menu,
            'game screen': self.game_screen,
            'about screen': self.about_screen
        }

    def run(self):
        while True:
            self.screens[self.ScreenManager.get_state()].run()
            self.screen.blit(self.master_surface, (0, 0))

            pygame.display.update() #double buffering
            self.clock.tick(configs.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()