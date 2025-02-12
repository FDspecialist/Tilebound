import pygame
import sys
from src.utils.configs import Configs
from src.utils.assets import Assets
from src.utils.button import Button
from src.utils.text import Text
from src.game_mechanics.board import Board
from src.game_mechanics.unit import Unit
from src.game_mechanics.unit_pool import UnitPool
Configs = Configs()
class GameScreen:
    def __init__(self, _display, _screenmanager):
        pygame.init()
        self.ID_NAME = "GameScreen"
        self.display = _display
        display_dimensions = self.display.get_rect()
        print(f"display width: {display_dimensions.width}\ndisplay height: {display_dimensions.height}")
        self.ScreenManager = _screenmanager

        self.tile_debug = False


        #game properties
        Configs.UNIT_POOL = UnitPool() #Refresh UnitPool each time GameScreen is initialised
        self.enable_player = True
        self.isPlayer = False#Determines whether a unit is being assigned to the player or not



        #Load backgrounds
        self.bg_load = Assets()
        self.bg_load.load_backgrounds()

        #background // using main menu bg as placeholder
        self.background = self.bg_load.get_sprite("background1").convert_alpha()
        self.background_rect = self.display.get_rect()

        # Font init
        self.font_assets = Assets()
        self.font_assets.load_fonts()
        self.text_colour = (255, 255, 255)

        #Text
        self.texts = []

        #[

        #0
        self.possession_turn_text = Text("_", 40, Configs.GRAY,Configs.SCREEN_MIDDLE_X, 50)
        self.texts.append(self.possession_turn_text)

        #]


        #buttons
        self.buttons = [
            #0
            Button("back",20,100,50,50, 25),
            #1
            Button("Toggle Tile Debug",20,220,50,110,75),
            #2
            Button("End turn",20,100,50, Configs.USER_WIDTH - 50, Configs.USER_HEIGHT - 25),
            #3
            Button("Toggle Player Units", 16,220,50,110,125)
        ]


        #board
        self.board = Board(self.display)


    def player_turn(self):
        self.possession_turn_text.update_text("Player's Turn")
        if self.enable_player:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Prompted exit from game_screen.py")
                    pygame.quit()
                    sys.exit()


                #buttons
                if self.buttons[0].is_clicked(event):
                    print("game screen ----> main menu")
                    self.ScreenManager.set_state('main menu')
                if self.buttons[1].is_clicked(event):
                    self.tile_debug = not self.tile_debug
                    print("\nTILE DEBUG: ON\n")
                if self.buttons[2].is_clicked(event):
                    print("\nPlayer turn ended")
                    self.end_turn()
                if self.buttons[3].is_clicked(event):
                    print("Player Units Toggled")
                    self.isPlayer = not self.isPlayer


                #tile debug
                if event.type == pygame.MOUSEBUTTONDOWN and self.tile_debug:
                    self.board.check_clicked_debug(event)

                elif event.type == pygame.MOUSEBUTTONDOWN and not self.tile_debug:
                    self.board.check_clicked_game(event,self.isPlayer)

        self.draw()


    def computer_turn(self):
        print("\n\nComputer turn started\n")
        self.possession_turn_text.update_text("Computer's Turn")



        self.draw()
        self.end_turn()



    def end_turn(self):
        self.enable_player = not self.enable_player
    def run_turns(self):
        match self.enable_player:
            case True:
                self.player_turn()
            case False:
                self.computer_turn()

    def run(self):
        self.run_turns()


    def draw(self):
        self.display.blit(self.background, self.background_rect)
        self.board.draw(self.display)
        for button in self.buttons:
            button.draw(self.display)
        for text in self.texts:
            text.draw(self.display)
        pygame.display.update()