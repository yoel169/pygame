import pygame_gui as gui
import pygame as py
from Other.Menus import GameMenu
from pygame.locals import VIDEORESIZE
from Actors.Players import Player
import json
from Other.PlayerPanel import PlayerPanel
from Game.Game import Game
from Other.Constants import Constants
from Other.InputBox import InputBox
from Saves.SaveLoad import PlayerHandler
import datetime
from pygame.locals import (
    K_ESCAPE,
    QUIT)

# INITIALIZE GAME
py.init()


class PlayerHub:
    def __init__(self, args):
        self.screen = args[3]
        self.background = args[2]
        self.SW = args[0]
        self.SH = args[1]

    def run(self, opt1, opt2, opt3):

        # loop variables
        time_delta = 0
        clock = py.time.Clock()
        running = True
        player = Player(False)
        won = False
        play = False
        inputbox = False

        # user variables
        score = 0
        tracker = 0
        option = opt1  # 0 for auto shooting, 1 for space, 2 for mouse
        option2 = opt2  # 0 for arrows, 1 for wads, 2 for mouse
        option3 = opt3  # 0 for windowed, 2 for fullscreen, 3 for hw

        # create player handler for load, save
        player_handler = PlayerHandler()
        save_files = []
        player_save = {}
        player_panel = None

        # ---------------------------------------------------- stages ------------------------------------------
        # hold all stages
        stages = []

        # screen args
        ls = [self.SW, self.SH, self.background, self.screen]

        # Load first 3 stages
        for x in range(1, 4):
            pack = 'Stages/stage' + str(x) + '.json'
            title = 'Stage ' + str(x)
            stages.append(Game(ls, title, pack, player))

        # stages and part tracker
        current_part = 0
        current_stage = 0
        maxstagenum = len(stages) - 1

        # ----------------------------------------------------------------------------------------------------------

        # CREATE GUI MANAGER and menu object
        manager = gui.UIManager((self.SW, self.SH))
        gameMenu = GameMenu(self.SW, self.SH, manager)

        # launch load/save menu and create input box
        gameMenu.launchMenu(player_handler.getSaves())
        inputbox = True
        inputboxd = InputBox(int(self.SW / 2) - 150, int(self.SH / 2) + 160, 30, 30)

        while running:

            # UPDATE MANAGER
            manager.update(time_delta)

            for event in py.event.get():

                # QUIT EVENT
                if event.type == py.QUIT or event.type == QUIT:
                    running = False

                elif event.type == py.KEYDOWN:

                    # ESC
                    if event.key == K_ESCAPE:
                        running = False
                        print('esc pressed')

                if event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:

                        if event.ui_element == gameMenu.back_b:
                            running = False

                        # confirm button from play launch
                        if event.ui_element == gameMenu.launch_button:

                            name1 = gameMenu.savelist_selection.get_single_selection()
                            name2 = inputboxd.text

                            player_save = player_handler.launch(name1,name2,option,option2)
                            option, option2 = player_save['settings'][0], player_save['settings'][1]

                            player.setInfo(player_save['player'])
                            current_stage, current_part = player_save['stage'][0], player_save['stage'][1]

                            inputbox = False
                            player_panel = PlayerPanel(self.screen, manager, self.background)
                            manager.clear_and_reset()
                            gameMenu.playerHubMenu()
                            player_panel.setPlayer(player_save)

                manager.process_events(event)
                if inputbox:
                    inputboxd.handle_event(event)

            if inputbox:
                inputboxd.update()

            # redraw bg and update gui
            self.screen.blit(self.background, (0, 0))
            manager.draw_ui(self.screen)
            if inputbox:
                inputboxd.draw(self.screen)

            # UPDATE SCREEN AND TICK CLOCK
            py.display.update()
            time_delta = clock.tick(60)