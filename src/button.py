from assets import Assets
import configs
import pygame
class Button: # OK SO FAT LOGIC ERROR BUT HEY ATLEAST EVERYTHING RUNS
    def __init__(self, _text, _font_size,width, height, _x, _y):
        #display
        self.button_assets = Assets()
        self.button_assets.load_buttons()
        self.button_default = self.button_assets.get_sprite("button_default").convert_alpha()
        self.button_down = self.button_assets.get_sprite("button_down").convert_alpha()
        self.button_image = self.button_default
        self.button_image = pygame.transform.scale(self.button_image, (width, height))
        self.button_rect = self.button_image.get_rect()
        # set button position
        self.x = _x
        self.y = _y
        self.button_rect.center = (self.x, self.y)
        #text
        self.font_assets = Assets()
        self.font_assets.load_fonts()
        self.font_size = _font_size
        self.font = self.font_assets.get_font(configs.DEFAULT_FONT, self.font_size)
        self.text = _text
        self.text_colour = (255, 255, 255)
        self.text_surface = self.font.render(self.text, True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect()

    def rundraw(self, screen):
        #set the text to center of button
        text_x = ((self.button_image.get_width() - self.text_surface.get_width())// 2)
        text_y = ((self.button_image.get_height() - self.text_surface.get_height())// 2)
        self.button_image.blit(self.text_surface, (text_x, text_y))
        screen.blit(self.button_image, (self.button_rect))