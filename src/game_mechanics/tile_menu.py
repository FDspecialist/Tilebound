import pygame
pygame.init()
from src.utils.configs import Configs
from src.utils.button import Button
from src.utils.stack import Stack
class TileMenu:
    def __init__(self):
        self.image = pygame.surface.Surface((240,150))
        self.image.fill(Configs.BLACK)
        self.active = False

        self.x = 1248
        self.y = 120

        #start menu on base neighbour
        self.spawn_unit_btn = Button("Spawn Unit", 20, 240,50, self.x, 25 + self.y)
        self.spawn_enemy_btn = Button("Spawn Enemy", 20, 240, 50, self.x, 75 + self.y)
        self.manual_debug_btn = Button("Manual Debug", 20, 240, 50, self.x, 125 + self.y)
        self.exit_btn = Button("Exit",20, 240, 50,self.x, 175 + self.y)

        #start menu on default tile
        self.info_btn = Button("Info", 20, 240, 50, self.x, 25 + self.y)
        self.exit_btn2 = Button("Exit", 20, 240, 50, self.x, 75 + self.y)

        #player spawn menu
        self.back_btn = Button("Back",20,240,50, self.x,25 + self.y)
        self.spawn_infantry_btn = Button("Spawn Infantry",20,240,50,self.x,75 + self.y)
        self.spawn_archer_btn = Button("Spawn Archer", 20,240,50,self.x, 125 + self.y)
        self.spawn_knight_btn = Button("Spawn Knight", 20,240,50,self.x,175 + self.y)

        self.start = [
            self.spawn_unit_btn,
            self.spawn_enemy_btn,
            self.manual_debug_btn,
            self.exit_btn
        ]

        self.start2 = [
            self.info_btn,
            self.exit_btn2
        ]

        self.player_spawn_menu = [
            #0
            self.back_btn,
            #1
            self.spawn_infantry_btn,
            #2
            self.spawn_archer_btn,
            #3
            self.spawn_knight_btn
        ]

        self.history = Stack()
        self.history.push(self.start)
        self.current_menu = self.history.peek()

    def activate(self,isBase):
        self.active = True
        if isBase:
            self.history.push(self.start)
            self.current_menu = self.history.peek()
        else:
            self.history.push(self.start2)
            self.current_menu = self.history.peek()
    def deactivate(self):
        self.active = False
        self.history.stack.clear()

    def set_menu(self,selected_string):
        match selected_string:
            case "start":
                self.history.push(self.start)
                self.current_menu = self.history.peek()
            case "player_spawn_menu":
                self.history.push(self.player_spawn_menu)
                self.current_menu = self.history.peek()
            case "previous":
                self.history.pop()
                self.current_menu = self.history.peek()

    def button_hovering(self,event):
        for button in self.current_menu:
            button.is_hovering(event)
            return True

    def button_clicked(self,event):
        for button in self.current_menu:
            if button.is_clicked(event):
                if button.text == "Back":
                    self.set_menu("previous")
                return button.text

    def draw(self, display):
        for button in self.current_menu:
            button.draw(display)