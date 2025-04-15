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
        self.tile_debug = False


        #game properties
        Configs.UNIT_POOL = UnitPool() #Refresh UnitPool each time GameScreen is initialised
        self.board = Board(self.display)
        self.board.init_structures()
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



        self.player_unit_count_text = Text("Player Unit Count: 0", 25, Configs.LIGHT_BLUE,150, 225)
        self.texts.append(self.player_unit_count_text)


        self.player_balance_text = Text(f"Resources: {self.Player.balance}",25,Configs.LIGHT_BLUE, 210, 275)
        self.texts.append(self.player_balance_text)

        self.computer_unit_count_text = Text("Computer Unit Count: 0",25,Configs.RED, 170,325)
        self.texts.append(self.computer_unit_count_text)

        self.game_turn_text = Text("Player Turn", 35, Configs.WHITE, Configs.SCREEN_MIDDLE_X, 60)
        self.texts.append(self.game_turn_text)



        #main buttons
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

        #player board options menu



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


                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get necessary data
                    click_on_board = self.board.search_tile(event)
                    #Tile Menu Handling take 2
                    if self.tile_menu.active:
                        #click not on board or tile menu
                        if event.button == 1 and not click_on_board and not self.tile_menu.button_hovering(event):
                            print("Not on board or tile menu")
                            self.tile_menu.deactivate()

                        #click on tile menu
                        if event.button == 1 and self.tile_menu.button_hovering(event):
                            selected_button = self.tile_menu.button_clicked(event)
                            match selected_button:
                                #start menu
                                case "Spawn Unit":
                                    self.tile_menu.set_menu("player_spawn_menu")
                                case "Spawn Enemy":
                                    if self.board.selected_tile.traversable:
                                        infantry_unit = Configs.UNIT_POOL.get_unit()
                                        infantry_unit.activate("Infantry", self.isPlayer, self.board.selected_tile.x, self.board.selected_tile.y)
                                        self.Computer.assign_unit(infantry_unit)
                                        self.board.selected_tile.add_unit(infantry_unit)
                                        self.board.selected_tile.update_visual()
                                        self.tile_menu.deactivate()
                                case "Manual Debug":
                                    self.board.selected_tile.visual_debug_click()
                                    self.tile_menu.deactivate()
                                case "Exit":
                                    self.tile_menu.deactivate()

                                #player spawn menu
                                case "Spawn Infantry":
                                    infantry_unit = Configs.UNIT_POOL.get_unit()
                                    continue
                                case "Spawn Archer":
                                    continue
                                case "Spawn Knight":
                                    continue

                    else:
                        if event.button == 1 and click_on_board == True:
                            self.tile_menu.activate()





                    # #TILE MENU HANDLING
                    # if self.tile_menu.active:
                    #     if event.button == 1 and not click_on_board and not tile_menu_hovering:
                    # else:
                    #     print("--TileMenu Inactive")
                    #     # Left click, on board
                    #     if event.button == 1 and click_on_board == True:

                    #Check for clicks on board


                    #only activate for unit testing while unit placement rework is being worked on
                    # click_on_board = self.board.search_tile(event)
                    # if self.tile_debug:
                    #     self.board.check_clicked_debug(event)
                    # if click_on_board and self.board.selected_tile.traversable and self.tile_debug == False:
                    #     # spawn infantry for now
                    #     infantry_unit = Configs.UNIT_POOL.get_unit()
                    #     infantry_unit.activate("Infantry", self.isPlayer, self.board.selected_tile.x, self.board.selected_tile.y)
                    #
                    #     if self.isPlayer and self.Player.balance - infantry_unit.Cost > 0:
                    #         self.Player.assign_unit(infantry_unit)
                    #         self.Player.balance = self.Player.balance - infantry_unit.Cost
                    #         self.board.selected_tile.add_unit(infantry_unit)
                    #     elif not self.isPlayer:
                    #         self.Computer.assign_unit(infantry_unit)
                    #         self.board.selected_tile.add_unit(infantry_unit)
                    #     self.board.selected_tile.update_visual()

        #update texts
        self.player_unit_count_text.update_text(f"Player Unit Count: {self.Player.unit_count}")
        self.computer_unit_count_text.update_text(f"Computer Unit Count: {self.Computer.unit_count}")
        self.player_balance_text.update_text(f"Resources: {self.Player.balance}")
        self.draw()

    #handle game process for computer
    def computer_turn(self):
        print("\n\nComputer turn started\n")

        self.Computer.move_units_to_enemy(self.Player.unit_list, self.board.array)

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
        if self.enable_player:
            self.game_turn_text.update_text("Player Turn. . .")
        else:
            self.game_turn_text.update_text("Computer Turn. . .")

        mouse_pos = pygame.mouse.get_pos()
        self.board.mouse_hover_highlight(mouse_pos)
        self.board.update_all()#update visuals of all tiles
        self.run_turns()


    def draw(self):
        #be wary of draw order
        self.display.blit(self.background, self.background_rect)
        self.board.draw(self.display)
        for button in self.buttons:
            button.draw(self.display)
        for text in self.texts:
            text.draw(self.display)
        if self.tile_menu.active:
            self.tile_menu.draw(self.display)
        pygame.display.update()