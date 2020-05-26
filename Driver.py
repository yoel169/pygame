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
                    kim_exit = hub.run()
                    if kim_exit:
                        is_running = False

                # settings button
                elif event.ui_element == gameMenu.setting_b:
                    manager.clear_and_reset()
                    gameMenu.settings_menu()

                # info button from main menu
                    # elif event.ui_element == gameMenu.info_b:
                    # manager.clear_and_reset()
                    # gameMenu.info_menu()

        manager.process_events(event)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    time_delta = clock.tick(60)

    pygame.display.update()