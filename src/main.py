import pygame
import configs
from main_menu import MainMenu
from game_screen import GameScreen
from about_screen import AboutScreen
from screen_manager import ScreenManager
class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tilebound")

        self.screen = pygame.display.set_mode((configs.USER_WIDTH, configs.USER_HEIGHT))
        self.master_surface = pygame.Surface((configs.USER_WIDTH, configs.USER_HEIGHT))
        print(f"\nCurrent resolution: {configs.USER_WIDTH},{configs.USER_HEIGHT}\n")

        #full screen logic handling

        self.clock = pygame.time.Clock()
        self.ScreenManager = ScreenManager('main menu')
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