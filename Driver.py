import pygame_gui
import pygame
from Other.Menus import GameMenu
from pygame.locals import VIDEORESIZE
from Game.PlayerHub import PlayerHub
from Other.Constants import Constants
import json

# ================================== DRIVER CLASS FOR GAME ======================================

pygame.init()

# get users screen resolution minus 60 height from bottom cause of taskbar
SW, SH = pygame.display.Info().current_w, pygame.display.Info().current_h - 60

# class variable of constant to share screen size among other classes
const = Constants()
Constants.screenSize = (SH, SH)

# set name
pygame.display.set_caption('World Flying Shooter')

# get game config and set window accordingly
info = {}
with open('gameconfig.json', 'r') as f:
    info = json.load(f)

# set screen according to config else set screen to resizable
if len(info) != 0:
    if info['screen'] == 'fullscreen':
        window_surface = pygame.display.set_mode((SW, SH), flags=pygame.FULLSCREEN)
    elif info['screen'] == 'hardware accelerated':
        window_surface = pygame.display.set_mode((SW, SH), flags=pygame.FULLSCREEN |
                                                    pygame.HWSURFACE | pygame.DOUBLEBUF)
    else:
        window_surface = pygame.display.set_mode((SW, SH), flags=pygame.RESIZABLE)
else:
    window_surface = pygame.display.set_mode((SW, SH), flags=pygame.RESIZABLE)


# get background
background = pygame.image.load("BG.png").convert()
background = pygame.transform.scale(background, (SW, SH))

# create UI manager
manager = pygame_gui.UIManager((SW, SH), 'attributes.json')

# driver variables
is_running = True
clock = pygame.time.Clock()
time_delta = 0
kim_exit = False

# user variables
option = 0  # 0 for auto shooting, 1 for space, 2 for mouse
option2 = 0  # 0 for arrows, 1 for wads, 2 for mouse
option3 = 0  # 0 for windowed, 2 for fullscreen, 3 for hw

# screen args for hub
ls = [SW, SH, background, window_surface]
hub = PlayerHub(ls)

# setup menu class
gameMenu = GameMenu(SW, SH, manager)


def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Media/game2.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)


#playMusic()

gameMenu.main_menu()

while is_running:

    # update manager and window
    manager.update(time_delta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], flags= pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
            pygame.display.flip()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                # exit button
                if event.ui_element == gameMenu.quit_b:
                    is_running = False

                # play button launch player selection launch menu
                elif event.ui_element == gameMenu.play_b:
                    kim_exit = hub.run(option, option2, option3)
                    if kim_exit:
                        is_running = False

                # # load menu
                # elif event.ui_element == gameMenu.load_button:
                #     manager.clear_and_reset()
                #     saveFiles = playerHandler.getSaves()
                #     gameMenu.load_menu(saveFiles)
                #
                # # load menu confirm button and launch menu confirm
                # elif event.ui_element == gameMenu.loadConfirm_button:
                #     filename = gameMenu.savelist_selection.get_single_selection()
                #     if filename is not None:
                #         playerSave = PlayerHandler.loadSave(playerHandler, filename)
                #         player.setInfo(playerSave['player'])
                #         option, option2 = playerSave['settings'][0], playerSave['settings'][1]
                #         currentStage, currentPart = playerSave['stage'][0], playerSave['stage'][1]
                #
                #     info['player'] = playerSave['name']
                #     with open('gameconfig.json', 'w') as f:
                #         json.dump(info, f, indent=2)
                #
                #     manager.clear_and_reset()
                #     playerPanel.setPlayer(playerSave)
                #     gameMenu.main_menu()
                #
                # # save menu
                # elif event.ui_element == gameMenu.save_button:
                #     manager.clear_and_reset()
                #     saveFiles = playerHandler.getSaves()
                #     gameMenu.save_menu(saveFiles)
                #     inputBoxD = InputBox(int(SW /2) - 150, int(SH / 2)+ 160, 30, 30)
                #     inputbox = True
                #
                # # save confirm button
                # elif event.ui_element == gameMenu.saveConfirm_button:
                #
                #     name = gameMenu.savelist2_selection.get_single_selection()
                #     time2 = datetime.datetime.now()
                #     time2 = time2.strftime("%m-%d-%y %I:%M:%S %p")
                #
                #     if name is not None:
                #         playerSave['times'][1] = time2
                #         playerSave['player'] = player.getInfo()
                #         playerHandler.save(playerSave)
                #     else:
                #         if len(inputBoxD.text) != 0:
                #             name = inputBoxD.text
                #         else:
                #             name = 'player'
                #
                #         db = {'name': name, 'player': player.getInfo(), 'times': [time1, time1],
                #               'settings': [option, option2], 'stage': [currentStage, currentPart]}
                #
                #         playerHandler.save(db)
                #         playerSave = db
                #
                #     info['player'] = playerSave['name']
                #     with open('gameconfig.json', 'w') as f:
                #         json.dump(info, f, indent=2)
                #
                #     inputbox = False
                #     manager.clear_and_reset()
                #     gameMenu.main_menu()
                #     playerPanel.setPlayer(playerSave)
                #
                # # cancel from save menu
                # elif event.ui_element == gameMenu.cancel_button:
                #     inputbox = False
                #     manager.clear_and_reset()
                #     gameMenu.main_menu()
                #     playerPanel.setPlayer(playerSave)

                # settings button
                elif event.ui_element == gameMenu.setting_b:
                    manager.clear_and_reset()
                    gameMenu.settings_menu()

                # # settings button called from replay menu
                # elif event.ui_element == gameMenu.setting_button2:
                #     manager.clear_and_reset()
                #     gameMenu.settings_menu()
                #     gameReturn = True

                # # settings button called from win menu
                # elif event.ui_element == gameMenu.setting_button3:
                #     manager.clear_and_reset()
                #     gameMenu.settings_menu()
                #     continueMenu = True

                # info button from main menu
                    # elif event.ui_element == gameMenu.info_b:
                    # manager.clear_and_reset()
                    # gameMenu.info_menu()

                # confirm button from inside settings menu
                elif event.ui_element == gameMenu.confirm_setting_b:
                    temp = gameMenu.shoot_selection.get_single_selection()  # save shooting selection
                    temp2 = gameMenu.screen_selection.get_single_selection()  # save screen selection
                    temp3 = gameMenu.movement_selection.get_single_selection()  # save movement selection

                    # update shooting
                    if temp is not None:
                        if temp == 'space':
                            option = 1
                        elif temp == 'mouse':
                            option = 2
                        else:
                            option = 0

                    # update screen
                    if temp2 is not None:
                        if temp2 == 'fullscreen':
                            window_surface = pygame.display.set_mode((SW, SH), flags=pygame.FULLSCREEN)
                        elif temp2 == 'hardware accelerated':
                            window_surface = pygame.display.set_mode((SW, SH), flags=pygame.FULLSCREEN |
                                                                    pygame.HWSURFACE | pygame.DOUBLEBUF)
                        else:
                            window_surface = pygame.display.set_mode((SW, SH), flags=pygame.RESIZABLE)

                        # update game config file
                        with open('gameconfig.json', 'w') as f:
                            info['screen'] = temp2
                            json.dump(info, f, indent=2)

                    # update movement
                    # if temp3 is not None:
                    #     if temp3 == 'wads keys':
                    #         option2 = 1
                    #         player.arrows = False
                    #     elif temp3 == 'mouse':
                    #         option2 = 2
                    #     else:
                    #         option2 = 0
                    #         player.arrows = True

                    # update save file
                    # playerSave['settings'] = [option, option2]

                    manager.clear_and_reset()
                    gameMenu.main_menu()

                    # check if settings was called from retry again or not
                    # if gameReturn:
                    #     gameMenu.replay_menu()
                    # elif continueMenu:
                    #     gameMenu.nextLevel()
                    # else:
                    #     playerPanel.setPlayer(playerSave)

        manager.process_events(event)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    time_delta = clock.tick(60)

    pygame.display.update()

# time2 = datetime.datetime.now()
# time2 = time2.strftime("%m-%d-%y %I:%M:%S %p")
# playerSave['times'][1] = time2
# playerSave['player'] = player.getInfo()
# playerHandler.save(playerSave)