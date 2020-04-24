import pygame_gui
import pygame
from Levels.Game import Game

SW = 800
SH = 600

anchd = {'left': 'right', 'right': 'right', 'top': 'bottom', 'bottom': 'bottom'}

pygame.init()

pygame.display.set_caption('World Flying Fighter ')
window_surface = pygame.display.set_mode((SW, SH),)

background = pygame.Surface((SW, SH))
background.fill((135, 206, 250)) #blue

manager = pygame_gui.UIManager((SW, SH),'attributes.json')  # create UI manager


def menu():
    global quit_button, play_button, info_button

    buttonSize = (0, 0, 150, 60)
    button_layout_rect = pygame.Rect(buttonSize)

    button_layout_rect.bottomright = (int(-SW / 2) + 50, -100)

    quit_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                               text='Quit', manager=manager,
                                               anchors=anchd)

    button_layout_rect.bottomright = (int(-SW / 2) + 50, -300)

    play_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                               text='Play', manager=manager,
                                               anchors=anchd)

    button_layout_rect.bottomright = (int(-SW / 2) + 50, -200)

    info_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                               text='Instructions', manager=manager,
                                               anchors=anchd)


def replay_game():
    global replay_button, quit_button2

    buttonSize = (0, 0, 150, 60)

    button_layout_rect = pygame.Rect(buttonSize)

    button_layout_rect.bottomright = (int(-SW / 2) + 50, -100)

    quit_button2 = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                               text='Quit', manager=manager,
                                               anchors=anchd)

    button_layout_rect.bottomright = (int(-SW / 2) + 50, -200)
    replay_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                 text='Try Again', manager=manager,
                                                 anchors=anchd)


is_running = True
play = False
won = False
score = 0
tracker = 0
clock = pygame.time.Clock()

menu()

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == quit_button:
                    is_running = False

                elif event.ui_element == play_button:
                    play = True
                    info_button.remove()
                    play_button.remove()
                    info_button.remove()

                elif event.ui_element == replay_button:
                    replay_button.remove()
                    play = True

                elif event.ui_element == quit_button2:
                    manager.clear_and_reset()
                    menu()

        manager.process_events(event)

    if play:
        game = Game(SW, SH, window_surface)
        (won, score) = game.run()
        manager.clear_and_reset()

        if not won:
            play = False
            manager.clear_and_reset()
            replay_game()

        elif won:
            play = False
            manager.clear_and_reset()
            menu()

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
