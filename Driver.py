import pygame_gui
import pygame
from Other.Menus import GameMenu
from pygame.locals import VIDEORESIZE
from Game.Game import Game
from Other.Constants import Constants
from Other.InputBox import InputBox
from Saves.SaveLoad import PlayerHandler
import datetime
from Actors.Players import Player
import json
from Other.PlayerPanel import PlayerPanel

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
play = False
won = False
gameReturn = False
continueMenu = False
clock = pygame.time.Clock()
time_delta = 0

# user variables
score = 0
tracker = 0
option = 0  # 0 for auto shooting, 1 for space, 2 for mouse
option2 = 0  # 0 for arrows, 1 for wads, 2 for mouse
option3 = 0  # 0 for windowed, 2 for fullscreen, 3 for hw
player = Player(True)  # create player

# stages and part tracker
currentPart = 0
currentStage = 0

# screen args
ls = [SW, SH, background, window_surface]

# hold all stages
stages = []

# create first 3 stages
for x in range(1,4):
    pack = 'Stages/stage' + str(x) + '.json'
    title = 'Stage ' + str(x)
    stages.append(Game(ls, title, pack, player))

maxStageNum = len(stages) - 1

# create player handler for load, save
playerHandler = PlayerHandler()
saveFiles = []
playerSave = {}

# setup menu class and launch main menu
gameMenu = GameMenu(SW, SH, manager)
gameMenu.main_menu()

# setup player info panel
playerPanel = PlayerPanel(window_surface,manager,background)
#input box
#input_box1 = InputBox(100, 100, 140, 32)

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Media/game2.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)


#playMusic()

while is_running:

    # update manager and window
    manager.update(time_delta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # doesn't do jack?
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], flags= pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
            pygame.display.flip()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                # exit button
                if event.ui_element == gameMenu.quit_button:
                    is_running = False

                # play button
                elif event.ui_element == gameMenu.play_button:
                    play = True

                # replay button if exit or lost
                elif event.ui_element == gameMenu.replay_button:
                    play = True

                # load menu
                elif event.ui_element == gameMenu.load_button:
                    manager.clear_and_reset()
                    saveFiles = playerHandler.getSaves()
                    gameMenu.load_menu(saveFiles)

                # load menu confirm
                elif event.ui_element == gameMenu.loadConfirm_button:
                    filename = gameMenu.savelist_selection.get_single_selection()
                    if filename is not None:
                        playerSave = PlayerHandler.loadSave(playerHandler, filename)
                        player.setInfo(playerSave['player'])
                        option, option2 = playerSave['settings'][0], playerSave['settings'][1]
                        currentStage, currentPart = playerSave['stage'][0], playerSave['stage'][1]
                        playerPanel.setPlayer(playerSave)
                    manager.clear_and_reset()
                    gameMenu.main_menu()

                # save
                elif event.ui_element == gameMenu.save_button:
                    if len(playerSave) == 0:
                        time1 = datetime.datetime.now()
                        time1 = time1.strftime("%m-%d-%y %I %p")
                        db = {'name': 'yoel', 'player': player.getInfo(), 'times': [time1,time1],
                              'settings': [option, option2], 'stage': [currentStage, currentPart]}
                        playerHandler.save(db)

                # settings button
                elif event.ui_element == gameMenu.setting_button:
                    manager.clear_and_reset()
                    gameMenu.settings_menu()

                # settings button called from replay menu
                elif event.ui_element == gameMenu.setting_button2:
                    manager.clear_and_reset()
                    gameMenu.settings_menu()
                    gameReturn = True

                # settings button called from win menu
                elif event.ui_element == gameMenu.setting_button3:
                    manager.clear_and_reset()
                    gameMenu.settings_menu()
                    continueMenu = True

                # info button from main menu
                #elif event.ui_element == gameMenu.info_button:
                    #manager.clear_and_reset()
                    #gameMenu.info_menu()

                # next level button
                elif event.ui_element == gameMenu.nextL_button:
                    play = True

                # confirm button from inside settings menu
                elif event.ui_element == gameMenu.confirm:
                    temp = gameMenu.shootMenu.get_single_selection()  # save shooting selection
                    temp2 = gameMenu.screenMenu.get_single_selection()  # save screen selection
                    temp3 = gameMenu.movementMenu.get_single_selection()  # save movement selection

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
                            info ={'screen': temp2}
                            json.dump(info, f, indent=2)

                    # update movement
                    if temp3 is not None:
                        if temp3 == 'wads keys':
                            option2 = 1
                            player.arrows = False
                        elif temp3 == 'mouse':
                            option2 = 2
                        else:
                            option2 = 0
                            player.arrows = True

                    manager.clear_and_reset()

                    # check if settings was called from retry again or not
                    if gameReturn:
                        gameMenu.replay_menu()
                    elif continueMenu:
                        gameMenu.nextLevel()
                    else:
                        gameMenu.main_menu()

                # quit button called from replay menu
                elif event.ui_element == gameMenu.quit_button2:
                    manager.clear_and_reset()
                    gameMenu.main_menu()

        manager.process_events(event)
       # input_box1.handle_event(event)

    #input_box1.update()

    if play:

        manager.clear_and_reset()
        args = [option, option2]
        won, score, player = stages[currentStage].getPart(args, currentPart, score)
        manager.clear_and_reset()  # reset GUI

        if not won:  # if lost launch replay menu

            play = False
            manager.clear_and_reset()

            # if lives reached 0 reset part
            if player.lives == 0:
                currentPart, score = 0, 0
                player.reset()
                gameMenu.replay_menu('no more lives')
            else:
                gameMenu.replay_menu('try again?')

        elif won:  # if won

            play = False
            manager.clear_and_reset()

            # if there are no more parts in the stage
            if currentPart >= len(stages[currentStage].levels) - 1:

                # reset player info and current part and increase current stage
                score = 0
                player.reset()
                currentStage += 1
                currentPart = 0

                # if we ran out of stages go to main menu else next stage
                if currentStage >= maxStageNum:
                    player.reset()
                    gameMenu.main_menu()
                else:
                    manager.clear_and_reset()
                    gameMenu.nextLevel("next stage")

            # else if there are more parts increase counter and summon holy menu
            else:
                currentPart += 1
                gameMenu.nextLevel("next part")

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
   #input_box1.draw(window_surface)
    time_delta = clock.tick(60)

    pygame.display.update()
