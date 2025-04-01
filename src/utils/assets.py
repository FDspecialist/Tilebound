import os
import pygame
class Assets:
    def __init__(self):
        self.sprites = {}
        self.fonts = {}
        pygame.init()

    #sprite related
    def load_backgrounds(self):
        path = os.path.join("../Assets", "Backgrounds")
        for file in os.listdir(path):
            self.sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))
    def load_boardsprites(self):
        path = os.path.join("../Assets", "Board")
        for file in os.listdir(path):
            self.sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))
    def load_buttons(self):
        path = os.path.join("../Assets", "Buttons")
        for file in os.listdir(path):
            self.sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))
    def get_sprite(self, name):
        return self.sprites[name]
    def sprites(self):
        return self.sprites

    #font related
    def load_fonts(self):
        path = os.path.join("../Assets", "Fonts")
        for file in os.listdir(path):
            if file.endswith(".otf"):
                font_name = file.split('.')[0]
                self.fonts[font_name] = os.path.join(path, file) # store path instead
    def get_font(self, name, size):
        if name in self.fonts:
            return pygame.font.Font(self.fonts[name], size)
        else:
            print(f"{name} was not found")
    def fonts(self):
        return self.fonts

# testing
background_assets = Assets()
button_assets = Assets()
background_assets.load_backgrounds()
button_assets.load_buttons()
font_assets = Assets()
font_assets.load_fonts()
font = font_assets.get_font("Pixel Digivolve", 36)
font.render("Testing", False, (255,255,255))

board_assets = Assets()
board_assets.load_boardsprites()
wall_asset = board_assets.get_sprite("wall")