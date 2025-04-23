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

        self.player_busy_state_text = Text("Player State: ", 25,Configs.GRAY, 200, 375)
        self.texts.append(self.player_busy_state_text)

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

                run_state = self.determine_state()
                match run_state:
                    case "Neutral":
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.neutral_logic_state(event)
                    case "Spawning":
                        self.spawn_logic_state(event)
                        self.spawn_visuals_state()
                    case "Moving":
                        moveable_list = self.board.selected_tile.list_moveable(self.board.array)
                        unit = self.board.selected_tile.current_unit
                        start_tile = self.board.selected_tile
                        self.movement_logic_state(event, moveable_list, unit, start_tile)
                        self.movement_visuals_state(moveable_list)


        #update texts
        self.player_unit_count_text.update_text(f"Player Unit Count: {self.Player.unit_count}")
        self.computer_unit_count_text.update_text(f"Computer Unit Count: {self.Computer.unit_count}")
        self.player_balance_text.update_text(f"Resources: {self.Player.balance}")
        self.draw()


    def determine_state(self):
        run_state = ""
        if not self.Player.is_busy():
            run_state = "Neutral"
            self.player_busy_state_text.update_text("Player State: Neutral")
            return run_state
        elif self.Player.states["Spawning"]:
            run_state = "Spawning"
            self.player_busy_state_text.update_text("Player State: Spawning")
            return run_state
        elif self.Player.states["Moving"]:
            self.player_busy_state_text.update_text("Player State: Moving")
            return run_state

    def spawn_player_unit(self, selection):
        #It spends the player's resources to create an infantry unit, places the unit on the selected tile,
        #updates the tile's appearance, and then closes the tile menu.
        if self.Player.balance - Configs.UNIT_STATS[selection]["Cost"] >= 0:
            self.Player.balance = self.Player.balance - Configs.UNIT_STATS[selection]["Cost"]
            infantry_unit = Configs.UNIT_POOL.get_unit()
            infantry_unit.activate(selection, self.isPlayer, self.board.selected_tile.x, self.board.selected_tile.y)
            self.Player.assign_unit(infantry_unit)
            self.board.selected_tile.add_unit(infantry_unit)
            self.board.selected_tile.update_visual()
            self.tile_menu.deactivate()


    def spawn_logic_state(self, event):
        print("run_spawning_state started")
        clicked = self.board.search_tile_among(event, self.Player.base_tile.base_neighbours)
        if clicked and self.board.selected_tile.traversable:
            self.spawn_player_unit(self.Player.current_spawn)
            self.Player.reset_state()
    def spawn_visuals_state(self):
        if self.Player.states["Spawning"]:
            self.Player.base_tile.activate_neighbour_highlights()
        else:
            self.Player.base_tile.deactivate_neighbour_highlights()


    def attack_logic_state(self,event):
        print("attack_logic_state started")
        clicked = self.board.search_tile_among(event, self.Player.base_tile.base_neighbours)
        pass
    def attack_visuals_state(self):
        pass

    def movement_logic_state(self,event,moveable_list,unit, start_tile):
        print("movement_logic_state started")
        clicked = self.board.search_tile(event)
        new_tile = self.board.selected_tile
        if clicked and new_tile in moveable_list:
            start_tile.remove_unit()
            start_tile.update_visual()
            unit.move(new_tile.x, new_tile.y)
            new_tile.add_unit(unit)
            new_tile.update_visual()
            self.Player.reset_state()
    def movement_visuals_state(self,moveable_list):
            if self.Player.states["Moving"]:
                self.board.activate_highlight_list(moveable_list)
            else:
                self.board.deactivate_highlight_list(moveable_list)
    def neutral_logic_state(self, event):
        print("run_neutral_state started")
        click_on_board = self.board.search_tile(event)
        if self.tile_menu.active:
            # click not on board or tile menu
            if event.button == 1 and click_on_board == False and self.tile_menu.button_hovering(event) == False:
                print("Not on board or tile menu")
                self.tile_menu.deactivate()

            # click on tile menu
            if event.button == 1 and self.tile_menu.button_hovering(event):
                selected_button = self.tile_menu.button_clicked(event)
                match selected_button:
                    # start menu
                    case "Spawn Unit":
                        self.tile_menu.set_menu("player_spawn_menu")
                    case "Spawn Enemy":
                        self.isPlayer = False
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

                    # player spawn menu
                    case "Spawn Infantry":
                        self.isPlayer = True
                        if self.Player.balance - Configs.INFANTRY_STATS["Cost"] >= 0:
                            self.Player.states["Spawning"] = True
                            self.Player.current_spawn = "Infantry"
                            self.tile_menu.deactivate()
                        else:
                            self.tile_menu.deactivate()

                    case "Spawn Archer":
                        self.isPlayer = True
                        if self.Player.balance - Configs.ARCHER_STATS["Cost"] >= 0:
                            self.Player.states["Spawning"] = True
                            self.Player.current_spawn = "Archer"
                            self.tile_menu.deactivate()
                        else:
                            self.tile_menu.deactivate()
                    case "Spawn Knight":
                        self.isPlayer = True
                        if self.Player.balance - Configs.KNIGHT_STATS["Cost"] >= 0:
                            self.Player.states["Spawning"] = True
                            self.Player.current_spawn = "Knight"
                            self.tile_menu.deactivate()

                    #unit tile menu:
                    case "Attack":
                        pass
                    case "Move":
                        self.Player.states["Moving"] = True
                        self.tile_menu.deactivate()

                        pass
                    case "Statistics":
                        pass

        else:
            if event.button == 1 and click_on_board == True:
                if self.board.selected_tile == self.Player.base_tile:
                    self.tile_menu.activate("BaseTile")
                elif self.board.selected_tile.current_unit.UnitType != "blank":
                    self.tile_menu.activate("UnitTile")
                else:
                    self.tile_menu.activate("RegularTile")

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