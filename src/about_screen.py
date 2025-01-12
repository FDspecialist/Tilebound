import pygame
import sys
import configs
from assets import Assets
from button import Button

class AboutScreen:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        #basic screen properties
        self.ID_NAME = "AboutScreen"
        self.display = _display
        self.ScreenManager = _ScreenManager

        #background
        self.bg_load = Assets()
        self.bg_load.load_backgrounds()

        self.background = self.bg_load.get_sprite("main_menu").convert_alpha()
        self.background_rect = self.background.get_rect()

        #buttons
        self.buttons = [# Name, font size, button width, button height, posx, posy
            #0
            Button("main menu", 25, 255, 50, configs.SCREEN_MIDDLE_X, 100)
        ]

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.buttons[0].is_clicked(event):
                print("about screen ----> main menu")
                self.ScreenManager.set_state('main menu')

        self.display.blit(self.background, self.background_rect)
        for button in self.buttons:
            button.draw(self.display)
