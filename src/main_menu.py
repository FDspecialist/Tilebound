import pygame
from button import Button
import configs
#note: See configs for info
class MainMenu:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        self.display = _display
        self.ScreenManager = _ScreenManager

        #Add buttons here, access by index
        self.buttons = [# Name, font size, button width, button height, posx, posy
            Button("START", 25, 100, 25, configs.SCREEN_MIDDLE_X, configs.SCREEN_MIDDLE_Y) # 1

        ]
    def run(self):
        #adjust screen size according to current view window
        screen_width, screen_height = pygame.display.get_surface().get_size()
        
        self.display.fill('blue')
        for button in self.buttons: #draw all buttons
            button.rundraw(self.display)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Hello World")


