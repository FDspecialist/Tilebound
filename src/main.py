import pygame
import sys
import configs
from main_menu import MainMenu
from game_screen import GameScreen
from screen_manager import ScreenManager
class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tilebound")

        self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        self.master_surface = pygame.Surface((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        self.full_screen = False # swtich only for dev purposes
        self.master_surface.fill((255,255,255))
        self.scaled_master_surface = None

        self.clock = pygame.time.Clock()
        self.ScreenManager = ScreenManager('main_menu')
        self.main_menu = MainMenu(self.master_surface, self.ScreenManager)
        self.game_screen = GameScreen(self.master_surface, self.ScreenManager)
        self.screens = {
            'main_menu': self.main_menu,
            'game_screen': self.game_screen
        }
    def run(self):

        if self.full_screen:
            self.scaled_master_surface = pygame.transform.scale(self.master_surface,(configs.USER_WIDTH, configs.USER_HEIGHT))
            self.screen = pygame.display.set_mode((configs.USER_WIDTH, configs.USER_HEIGHT))
        else:
            self.scaled_master_surface = self.master_surface

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screens[self.ScreenManager.get_state()].run()
            self.screen.blit(self.scaled_master_surface, (0, 0))

            pygame.display.flip() #double buffering
            self.clock.tick(configs.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()