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
        self.full_screen = True # swtich only for dev purposes
        self.master_surface.fill((255,255,255))
        self.scaled_master_surface = pygame.Surface((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.ScreenManager = ScreenManager('main menu')
        self.main_menu = MainMenu(self.scaled_master_surface, self.ScreenManager)
        self.game_screen = GameScreen(self.scaled_master_surface, self.ScreenManager)
        self.screens = {
            'main menu': self.main_menu,
            'game screen': self.game_screen
        }

    def init_screens(self):
        index = 0
        target = len(self.screens) - 1
        while index != target:
            match index:
                case 0:
                    self.screens['main menu'].display = self.scaled_master_surface
                    index = index + 1
                    print("Reached case 0")
                case 1:
                    self.screens['game screen'].display = self.scaled_master_surface
                    index = + 1
                    print("Reached case 1")
            print(f"Reached end of switch-case\nindex: {index}\ntarget: {target}")



    def run(self):

        if self.full_screen:
            self.scaled_master_surface = pygame.transform.scale(self.master_surface,(configs.USER_WIDTH, configs.USER_HEIGHT))
            self.screen = pygame.display.set_mode((configs.USER_WIDTH, configs.USER_HEIGHT))
        else:
            self.scaled_master_surface = self.master_surface

        self.init_screens()


        while True:
            event_to_screen = None #To get the event and pass it into the current screen
            for event in pygame.event.get():
                event_to_screen = event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screens[self.ScreenManager.get_state()].run(event_to_screen)
            self.screen.blit(self.scaled_master_surface, (0, 0))

            pygame.display.flip() #double buffering
            self.clock.tick(configs.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()