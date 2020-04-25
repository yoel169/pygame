import pygame_gui
import pygame
from Levels.Game import Game
from Other.Menus import GameMenu

SW = 800
SH = 600

pygame.init()

pygame.display.set_caption('World Flying Shooter')
window_surface = pygame.display.set_mode((SW, SH),)

background = pygame.Surface((SW, SH))
background.fill((135, 206, 250)) #blue

manager = pygame_gui.UIManager((SW, SH),'attributes.json')  # create UI manager

is_running = True
play = False
won = False
score = 0
tracker = 0
option = True
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

                elif event.ui_element == gameMenu.confirm:
                    temp = gameMenu.dropMenu.get_single_selection()
                    if temp == 'manual shooting':
                        option = False
                    manager.clear_and_reset()
                    gameMenu.main_menu()

                elif event.ui_element == gameMenu.quit_button2:
                    manager.clear_and_reset()
                    gameMenu.main_menu()

        manager.process_events(event)

    if play:
        game = Game(SW, SH, window_surface, option)  # create new game
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
