import pygame_gui
import pygame
from Levels.Game import Game
from Other.Menus import GameMenu

SW = 1920
SH = 1080

pygame.init()

pygame.display.set_caption('World Flying Shooter')
window_surface = pygame.display.set_mode((SW, SH), flags= pygame.FULLSCREEN)


background = pygame.Surface((SW, SH))
background.fill((135, 206, 250)) #blue

manager = pygame_gui.UIManager((SW, SH),'attributes.json')  # create UI manager

is_running = True
play = False
won = False
score = 0
tracker = 0
option = 0  # 0 for auto shooting, 1 for space, 2 for mouse
option2 = 0  # 0 for arrows, 1 for wads, 2 for mouse
gameReturn = False
clock = pygame.time.Clock()

gameMenu = GameMenu(SW,SH,manager)  # setup menu class

gameMenu.main_menu()  # launch main menu

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == gameMenu.quit_button:
                    is_running = False

                elif event.ui_element == gameMenu.play_button:
                    play = True

                elif event.ui_element == gameMenu.replay_button:
                    play = True

                elif event.ui_element == gameMenu.setting_button:
                    manager.clear_and_reset()
                    gameMenu.settings_menu()

                elif event.ui_element == gameMenu.setting_button2:
                    manager.clear_and_reset()
                    gameMenu.settings_menu()
                    gameReturn = True

                elif event.ui_element == gameMenu.confirm:
                    temp = gameMenu.shootMenu.get_single_selection()
                    temp2 = gameMenu.screenMenu.get_single_selection()
                    temp3 = gameMenu.movementMenu.get_single_selection()

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
                            window_surface = pygame.display.set_mode((SW, SH), flags=pygame.FULLSCREEN | pygame.HWSURFACE |
                                                                      pygame.DOUBLEBUF)
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
                        play = True
                    else:
                        gameMenu.main_menu()

                elif event.ui_element == gameMenu.quit_button2:
                    manager.clear_and_reset()
                    gameMenu.main_menu()

        manager.process_events(event)

    if play:
        game = Game(SW, SH, window_surface, option, option2)  # create new game
        (won, score) = game.run()  # launch and return if player won or lost and score
        manager.clear_and_reset()  # reset GUI

        if not won:  # if lost launch replay menu
            play = False
            manager.clear_and_reset()
            gameMenu.replay_menu()

        elif won:  # if won launch main menu
            play = False
            manager.clear_and_reset()
            gameMenu.main_menu()

    # update manager and window
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
