import pygame
import sys
from src.utils.assets import Assets
from src.utils.button import Button
from src.utils.configs import Configs


#note: See configs for info
class MainMenu:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        #basic screen properties
        self.ID_NAME = "MainMenu"
        self.display = _display
        self.ScreenManager = _ScreenManager

        #Load Backgrounds
        self.bg_load = Assets()
        self.bg_load.load_backgrounds()

        #Background
        self.background = self.bg_load.get_sprite("background1").convert_alpha()
        self.background_rect = self.display.get_rect()



        #Font init
        self.font_assets = Assets()
        self.font_assets.load_fonts()
        self.text_colour = Configs.WHITE

        #Title
        self.title_font = self.font_assets.get_font(Configs.DEFAULT_FONT, 150)
        self.title = self.title_font.render("!Tilebound!", True, self.text_colour)
        self.title_rect = self.title.get_rect()
        #Title position
        title_x = self.display.get_width() / 2
        title_y = 100
        self.title_rect.center = title_x, title_y

        #Add buttons here, access by index
        self.buttons = [# Name, font size, button width, button height, posx, posy
            #0
            Button("START", 25, 200, 50, Configs.SCREEN_MIDDLE_X, Configs.SCREEN_MIDDLE_Y),

            #1
            Button("OPTIONS", 25, 200, 50, Configs.SCREEN_MIDDLE_X, (Configs.SCREEN_MIDDLE_Y + (75 * 1))),

            #2
            Button("ABOUT", 25, 200, 50, Configs.SCREEN_MIDDLE_X, (Configs.SCREEN_MIDDLE_Y + (75 * 2))),

            #3
            Button("QUIT", 25, 200, 50, Configs.SCREEN_MIDDLE_X, (Configs.SCREEN_MIDDLE_Y + (75 * 3)))

        ]
    #iterate through all buttons on the screen, passes event into subroutine
    def check_buttons(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                match button.text:
                    case "START":
                        self.ScreenManager.set_state('game screen')
                    case "OPTIONS":
                        print("This is options")
                    case "ABOUT":
                        self.ScreenManager.set_state('about screen')
                    case "QUIT":
                        print("Exiting through QUIT button (main_menu.py)")
                        pygame.quit()
                        sys.exit()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_buttons(event)
        self.display.blit(self.background, self.background_rect)
        self.display.blit(self.title, (self.title_rect.centerx - (self.title.get_width()/2),self.title_rect.centery))

        for button in self.buttons: #draw all buttons
            button.draw(self.display)