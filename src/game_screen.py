import pygame
import sys
import configs
from assets import Assets
from button import Button
class GameScreen:
    def __init__(self, _display, _ScreenManager):
        pygame.init()
        self.ID_NAME = "GameScreen"
        self.display = _display
        self.ScreenManager = _ScreenManager

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





        #text
        self.text_font = self.font_assets.get_font(configs.DEFAULT_FONT, 50)
        self.text = self.text_font.render("game goes here , nothing to see yet", True, self.text_colour)
        self.text_rect = self.text.get_rect()
        #text position
        self.text_x = self.display.get_width() / 2
        self.text_y = self.display.get_height() / 2
        self.text_rect.center = self.text_x, self.text_y

        #buttons
        self.buttons = [
            #0
            Button("back",20,100,50,50, 25)
        ]


    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Prompted exit from game_screen.py")
                pygame.quit()
                sys.exit()
            if self.buttons[0].is_clicked(event):
                print("game screen ----> main menu")
                self.ScreenManager.set_state('main menu')


        self.display.blit(self.background, self.background_rect)
        self.display.blit(self.text, self.text_rect)

        for button in self.buttons:
            button.draw(self.display)
