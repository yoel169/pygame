import pygame_gui
import pygame
from Levels import Level1, Level2, Level3, Level4
from Other.Menus import GameMenu
from pygame.locals import VIDEORESIZE
from Levels.LevelPackMaker import PackMaker
# from Levels.Stage1 import WaveMaker
pygame.init()

SW, SH = pygame.display.Info().current_w, pygame.display.Info().current_h

pygame.display.set_caption('World Flying Shooter')
window_surface = pygame.display.set_mode((SW, SH), flags=pygame.RESIZABLE)

background = pygame.image.load("BG.png").convert()
background = pygame.transform.scale(background, (SW, SH))

manager = pygame_gui.UIManager((SW, SH), 'attributes.json')  # create UI manager

is_running = True
play = False
won = False
score = 0
tracker = 0
option = 0  # 0 for auto shooting, 1 for space, 2 for mouse
option2 = 0  # 0 for arrows, 1 for wads, 2 for mouse
gameReturn = False
continueMenu = False
clock = pygame.time.Clock()

# levels
args = [SW, SH, background, window_surface, option, option2]

level1 = Level1.Level1(args)
level2 = Level2.Level2(args)
level3 = Level3.Level3(args)
level4 = Level4.Level4(args)

levels = [level1, level2, level3, level4]

level_tracker = 0
numLevels = 4

# -----------------------------------------------------------------------------------------
#levelTitle = 'Level 1'  # args0
#maxWaves = 3  # args1

#buffSpawn = [5,10,15]  # args2
#maxScore = [25,50,100]  # args4
#eTypes = [0,1,2]
#enemyTimers = [500,1000,2000]

ls = [SW, SH, background, window_surface]

#myStageMaker = WaveMaker(ls)

levelPack = PackMaker(ls, 'Levels/levelpack1.json')
# -------------------------------------------------------------------------------------------

gameMenu = GameMenu(SW, SH, manager)  # setup menu class
gameMenu.main_menu()  # launch main menu

time_delta = 0

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Media/game2.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


playMusic()

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
                if event.ui_element == gameMenu.quit_button:
                    is_running = False

                # play button
                elif event.ui_element == gameMenu.play_button:
                    play = True

                # replay button if exit or lost
                elif event.ui_element == gameMenu.replay_button:
                    play = True

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

                    # update movement
                    if temp3 is not None:
                        if temp3 == 'wads keys':
                            option2 = 1
                        elif temp3 == 'mouse':
                            option2 = 2
                        else:
                            option2 = 0

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

    if play:

        manager.clear_and_reset()
        #(won, score) = levels[level_tracker].run()  # launch and return if player won or lost and score
        args = [option, option2]
        #args2 = [levelTitle, maxWaves, buffSpawn,maxScore, eTypes, enemyTimers]
        #won, score = myStageMaker.makeStage(args, args2)
        won, score = levelPack.getStage(args, 0)
        manager.clear_and_reset()  # reset GUI

        if not won:  # if lost launch replay menu

            play = False
            manager.clear_and_reset()
            gameMenu.replay_menu()

        elif won:  # if won launch next level menu

            play = False
            manager.clear_and_reset()
            level_tracker += 1
            gameMenu.nextLevel()

            if level_tracker >= numLevels:
                play = False
                manager.clear_and_reset()
                gameMenu.main_menu()

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    time_delta = clock.tick(60)

    pygame.display.update()
