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

        #start menu
        self.spawn_unit_btn = Button("Spawn Unit", 20, 240,50, self.x, 25 + self.y)
        self.spawn_enemy_btn = Button("Spawn Enemy", 20, 240, 50, self.x, 75 + self.y)
        self.manual_debug_btn = Button("Manual Debug", 20, 240, 50, self.x, 125 + self.y)

        #player spawn menu
        self.back_btn = Button("Back",20,240,50, self.x,25 + self.y)

        self.start = [
            #0
            self.spawn_unit_btn,
            #1
            self.spawn_enemy_btn,
            #2
            self.manual_debug_btn
        ]

        self.player_spawn_menu = [
            #0
            self.back_btn
        ]

        self.history = Stack()
        self.history.push(self.start)
        self.current_menu = self.history.peek()

    def activate(self):
        self.active = True
        self.history.push(self.start)
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