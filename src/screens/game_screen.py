import pygame
import sys
from src.utils.configs import Configs
from src.utils.assets import Assets
from src.utils.button import Button
from src.game_mechanics.board import Board
from src.game_mechanics.unit_pool import UnitPool
from src.game_mechanics.unit import Unit #just in case lol
Configs = Configs()
class GameScreen:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        self.ID_NAME = "GameScreen"
        self.display = _display
        display_dimensions = self.display.get_rect()
        print(f"display width: {display_dimensions.width}\ndisplay height: {display_dimensions.height}")
        self.ScreenManager = _ScreenManager

        #game properties
        self.UnitPool = UnitPool()

        #Load backgorunds
        self.bg_load = Assets()
        self.bg_load.load_backgrounds()

        #background // using main menu bg as placeholder
        self.background = self.bg_load.get_sprite("background1").convert_alpha()
        self.background_rect = self.display.get_rect()

        # Font init
        self.font_assets = Assets()
        self.font_assets.load_fonts()
        self.text_colour = (255, 255, 255)

        #buttons
        self.buttons = [
            #0
            Button("back",20,100,50,50, 25)
        ]


        #board
        self.board = Board()

    def run(self):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.tile_click_detect(event)

            if event.type == pygame.QUIT:
                print("Prompted exit from game_screen.py")
                pygame.quit()
                sys.exit()
            if self.buttons[0].is_clicked(event):
                print("game screen ----> main menu")
                self.ScreenManager.set_state('main menu')


        self.display.blit(self.background, self.background_rect)
        self.board.draw(self.display)
        for button in self.buttons:
            button.draw(self.display)
