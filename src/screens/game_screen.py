import pygame
import sys
from src.utils.configs import Configs
from src.utils.assets import Assets
from src.utils.button import Button
from src.utils.text import Text
from src.game_mechanics.tile_menu import TileMenu
from src.game_mechanics.board import Board
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

        #change to toggle tile coordinates later
        #self.tile_debug = False


        #game properties
        Configs.UNIT_POOL = UnitPool() #Refresh UnitPool each time GameScreen is initialised
        self.board = Board(self.display)
        self.tile_menu = TileMenu()
        self.Player = self.board.Player
        self.Computer = self.board.Computer


        self.enable_player = True # Player Turn Bool
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
        self.player_unit_count_text = Text("Player Unit Count: 0", 25, Configs.LIGHT_BLUE,150, 225)
        self.texts.append(self.player_unit_count_text)

        #1
        self.computer_unit_count_text = Text("Computer Unit Count: 0",25,Configs.RED, 170,275)
        self.texts.append(self.computer_unit_count_text)
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


    #handle game loop for player
    def player_turn(self):
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


                #Check for player input
                # if event.type == pygame.MOUSEBUTTONDOWN and self.tile_debug:
                #     self.board.check_clicked_debug(event)

                # Handle mouse inputs
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Check for clicks on board
                    click_on_board = self.board.search_tile(event)

                    #left click, not on board
                    if event.button == 1:
                        self.tile_menu.deactivate()

                    #Left click, on board
                    if event.button == 1 and click_on_board == True:
                        if self.tile_menu.active == False:
                            self.tile_menu.activate(self.board.selected_tile.x,self.board.selected_tile.y)
                        else:
                            self.tile_menu.update_pos(self.board.selected_tile.x,self.board.selected_tile.y)

                    # if click_on_board and self.board.selected_tile.traversable:
                    #     # spawn infantry for now
                    #     infantry_unit = Configs.UNIT_POOL.get_unit()
                    #     infantry_unit.activate("Infantry", self.isPlayer, self.board.selected_tile.x, self.board.selected_tile.y)
                    #     self.board.selected_tile.add_unit(infantry_unit)
                    #
                    #     if self.isPlayer:
                    #         self.Player.assign_unit(infantry_unit)
                    #     else:
                    #         self.Computer.assign_unit(infantry_unit)
                    #     self.board.selected_tile.update_visual()
                    #
                    #     print(f"\nPlayer Unit Count: {self.Player.unit_count}")
                    #     print(f"self.player_unit_count_text: {self.player_unit_count_text.text}\n")
                    #     self.player_unit_count_text.update_text(f"Player Unit Count: {self.Player.unit_count}")
                    #     self.computer_unit_count_text.update_text(f"Computer Unit Count: {self.Computer.unit_count}")
        self.draw()

    #handle game process for computer
    def computer_turn(self):
        print("\n\nComputer turn started\n")

        self.Computer.move_units_to_enemy(self.Player.unit_list)
        #DO NOT GET RID: updates visuals and ends turn
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
        self.board.update_all()#update visuals of all tiles
        self.run_turns()


    def draw(self):
        if self.tile_menu.active:
            self.tile_menu.blit_to(self.display)
        self.display.blit(self.background, self.background_rect)
        self.board.draw(self.display)
        for button in self.buttons:
            button.draw(self.display)
        for text in self.texts:
            text.draw(self.display)
        pygame.display.update()