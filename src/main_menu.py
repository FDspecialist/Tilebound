import pygame
from assets import Assets
from button import Button
import configs
#note: See configs for info
class MainMenu:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        self.ID_NAME = "MainMenu"
        self.display = _display
        self.ScreenManager = _ScreenManager

        #Load Backgrounds
        self.bg_load = Assets()
        self.bg_load.load_backgrounds()

        #Background
        self.background = self.bg_load.get_sprite("main_menu").convert_alpha()
        self.background_rect = self.display.get_rect()



        #Font init
        self.font_assets = Assets()
        self.font_assets.load_fonts()
        self.font = self.font_assets.get_font(configs.DEFAULT_FONT, 100)
        self.text_colour = (255, 255, 255)

        #Title
        self.title = self.font.render("Tilebound", True, self.text_colour)
        self.title_rect = self.title.get_rect()
        title_x = self.display.get_width() / 2
        title_y = 100
        self.title_rect.center = title_x, title_y

        #Add buttons here, access by index
        self.buttons = [# Name, font size, button width, button height, posx, posy
            #0
            Button("START", 25, 200, 50, configs.SCREEN_MIDDLE_X, configs.SCREEN_MIDDLE_Y)
        ]
    def run(self,event):
        if self.buttons[0].is_clicked(event):
            print("Screen acknowledges click.")
        self.display.blit(self.background, (self.background_rect))
        self.display.blit(self.title, (self.title_rect.centerx - (self.title.get_width()/2),self.title_rect.centery))

        for button in self.buttons: #draw all buttons
            button.rundraw(self.display, event)