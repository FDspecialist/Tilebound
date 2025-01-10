import pygame
import sys
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


        #Load Icons
        self.icon_load = Assets()
        self.icon_load.load_icon()

        #icon
        self.icon_init = self.icon_load.get_sprite("icon").convert_alpha()
        self.icon = pygame.transform.scale(self.icon_init, (161, 86))


        #Font init
        self.font_assets = Assets()
        self.font_assets.load_fonts()
        self.text_colour = (255, 255, 255)

        #Title
        self.title_font = self.font_assets.get_font(configs.DEFAULT_FONT, 150)
        self.title = self.title_font.render("!Tilebound!", True, self.text_colour)
        self.title_rect = self.title.get_rect()
        title_x = self.display.get_width() / 2
        title_y = 100
        self.title_rect.center = title_x, title_y

        #Add buttons here, access by index
        self.buttons = [# Name, font size, button width, button height, posx, posy
            #0
            Button("START", 25, 200, 50, configs.SCREEN_MIDDLE_X, configs.SCREEN_MIDDLE_Y),

            #1
            Button("OPTIONS", 25, 200, 50, configs.SCREEN_MIDDLE_X, (configs.SCREEN_MIDDLE_Y + (75*1))),

            #2
            Button("ABOUT", 25, 200, 50, configs.SCREEN_MIDDLE_X, (configs.SCREEN_MIDDLE_Y + (75 *2))),

            #3
            Button("QUIT", 25, 200, 50, configs.SCREEN_MIDDLE_X, (configs.SCREEN_MIDDLE_Y + (75 * 3)))

        ]
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.buttons[0].is_clicked(event):
                print(f"button: {self.buttons[0].text} is clicked")
        self.display.blit(self.background, (self.background_rect))
        self.display.blit(self.title, (self.title_rect.centerx - (self.title.get_width()/2),self.title_rect.centery))
        self.display.blit(self.icon, (0, 0))

        for button in self.buttons: #draw all buttons
            button.draw(self.display)
