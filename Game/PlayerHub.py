import pygame_gui as gui
import pygame as py
from Other.Menus import GameMenu
from Actors.Players import Player
from Game.Game import Game
from Other.InputBox import InputBox
from Other.Store import Store
from Saves.SaveLoad import PlayerHandler
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
        player = Player(True)
        won = False
        play = False
        inputbox = False
        kim_exit = False
        save = False  # saving player flag

        # user variables
        score = 0
        option = opt1  # 0 for auto shooting, 1 for space, 2 for mouse
        option2 = opt2  # 0 for arrows, 1 for wads, 2 for mouse
        # option3 = opt3  # 0 for windowed, 2 for fullscreen, 3 for hw

        # create player handler for player save handling
        player_handler = PlayerHandler()
        player_save = {}  # hold players data for player panel and for saving

        # ---------------------------------------------------- stages ------------------------------------------
        # hold all stages
        stages = []
        stage_names = []

        # screen args
        ls = [self.SW, self.SH, self.background, self.screen]

        # Load first 3 stages
        for x in range(1, 4):
            pack = 'Stages/stage' + str(x) + '.json'
            title = 'Stage ' + str(x)
            stage_names.append(title)
            stages.append(Game(ls, title, pack, player))

        # stages and part tracker
        current_part = 0
        current_stage = 0
        maxstagenum = len(stages) - 1

        # ----------------------------------------------------------------------------------------------------------

        # CREATE GUI MANAGER and menu object
        manager = gui.UIManager((self.SW, self.SH), 'Game/theme.json')
        gameMenu = GameMenu(self.SW, self.SH, manager)

        # store
        store = Store(self.screen, self.background, manager)

        # launch load/save menu and create input box
        gameMenu.launch_menu(player_handler.getSaves())
        inputbox = True
        inputboxd = InputBox(int(self.SW / 2) - 100, int(self.SH / 2) + 160, 30, 30)

        while running:

            # UPDATE MANAGER
            manager.update(time_delta)

            for event in py.event.get():

                # QUIT EVENT
                if event.type == py.QUIT:
                    running, kim_exit = False, True
                    save = True
                    print("exited and saved")

                elif event.type == py.KEYDOWN:

                    # ESC
                    if event.key == K_ESCAPE:
                        running = False
                        save = True
                        print('esc pressed')
                        print("exited and saved")

                if event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:

                        # go back button from hub
                        if event.ui_element == gameMenu.back_b:
                            running = False
                            save = True

                        # exit at profile selection menu
                        elif event.ui_element == gameMenu.quit_launcher_b:
                            running = False
                            save = False

                        # quit button called from replay menu or next level menu
                        elif event.ui_element == gameMenu.quit_replay_b or event.ui_element == gameMenu.quit_next_level_b:
                            manager.clear_and_reset()
                            gameMenu.player_hub(player_save, stage_names)

                        # next level button from retry or win menu
                        elif event.ui_element == gameMenu.next_level_b or event.ui_element == gameMenu.replay_b:
                            play = True

                        # go button for selecting a stage
                        elif event.ui_element == gameMenu.pick_b:
                            selection = gameMenu.pick_ddm.selected_option
                            for count, x in enumerate(stage_names, 0):
                                if selection == x:
                                    player_save['stage'] = current_stage, current_part = count, 0
                                    player.reset()
                                    player_save['player'] = player.getInfo()
                            play = True

                        # store button
                        elif event.ui_element == gameMenu.store_b:
                            manager.clear_and_reset()
                            store.run(player)

                        # confirm button from play launch
                        elif event.ui_element == gameMenu.launch_hub_b:

                            # get name selection and name from input box
                            name1 = gameMenu.save_selection.get_single_selection()
                            name2 = inputboxd.text

                            # feed it to launch handler to get a player save according to names and update setting
                            player_save = player_handler.launch(name1,name2,option,option2)
                            option, option2 = player_save['settings'][0], player_save['settings'][1]

                            # set the player and stage info based from save file
                            player.setInfo(player_save['player'])
                            player_save['player'] = player.getInfo(player_save)
                            current_stage, current_part = player_save['stage'][0], player_save['stage'][1]

                            # turn off inputbox, launch player hub and show player panel
                            inputbox = False
                            manager.clear_and_reset()
                            gameMenu.player_hub(player_save, stage_names)

                        # start next stage/ part
                        elif event.ui_element == gameMenu.cont_b:
                            play = True

                manager.process_events(event)
                if inputbox:
                    inputboxd.handle_event(event)

            if inputbox:
                inputboxd.update()

            # load next stage/part
            if play:
                manager.clear_and_reset()
                args = [option, option2]
                won, score, player, kim_exit = stages[current_stage].getPart(args, current_part, score)
                manager.clear_and_reset()  # reset GUI

                if kim_exit:
                    running = False

                # save
                player_save['player'] = player.getInfo(self)
                player_handler.save(player_save)

                player_save['player'] = player.getInfo()  # update player save file

                play = False
                manager.clear_and_reset()

                if not won:  # if lost launch replay menu

                    # if lives reached 0 reset part
                    if player.lives == 0:
                        current_part, score = 0, 0
                        player_save['stage'] = [current_stage, current_part]
                        player.reset()
                        player_save['player'] = player.getInfo()
                        gameMenu.replay_menu('no more lives')
                    else:
                        gameMenu.replay_menu('try again?')

                elif won:  # if won

                    # if there are no more parts in the stage
                    if current_part >= len(stages[current_stage].levels) - 1:

                        # reset player info and current part and increase current stage
                        score = 0
                        current_part = 0
                        player.reset()
                        player_save['player'] = player.getInfo()

                        # if we ran out of stages go to main menu else next stage todo make level selection menu
                        if current_stage >= maxstagenum:
                            gameMenu.player_hub(player_save, stage_names)
                        else:
                            current_stage += 1
                            manager.clear_and_reset()
                            gameMenu.next_level("next stage")

                    # else go to next part
                    else:
                        current_part += 1
                        gameMenu.next_level("next part")

                    player_save['stage'] = [current_stage, current_part]

            # redraw bg and update gui
            self.screen.blit(self.background, (0, 0))
            manager.draw_ui(self.screen)
            if inputbox:
                inputboxd.draw(self.screen)

            # UPDATE SCREEN AND TICK CLOCK
            py.display.update()
            time_delta = clock.tick(60)

        # save before exiting
        if save:
            player_save['player'] = player.getInfo(self)
            player_handler.save(player_save)

        return kim_exit