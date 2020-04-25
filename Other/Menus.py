import pygame
import pygame_gui

anchd = {'left': 'right', 'right': 'right', 'top': 'bottom', 'bottom': 'bottom'}


class GameMenu():
    def __init__(self, width, height, manager):
        self.SW = width
        self.SH = height
        self.manager = manager
        self.replay_button = None
        self.play_button = None
        self.info_button = None
        self.quit_button = None
        self.quit_button2 = None
        self.confirm = None
        self.dropMenu = None

    def main_menu(self):
        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        labelSize = (0, 0,500, 100)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int( - self.SW / 2 + 200), -450)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text= ' WORLD FLYING SHOOTER',
                                            manager=self.manager, anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -320)
        self.play_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Play', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -240)
        self.info_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Instructions', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -160)
        self.setting_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Settings', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -80)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Quit', manager=self.manager,
                                                   anchors=anchd)

    def replay_menu(self):
        labelSize = (0, 0, 400, 100)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2 + 180), -350)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text='play again?',
                                            manager=self.manager, anchors=anchd)

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -100)
        self.quit_button2 = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Quit To Menu', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -200)
        self.replay_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                     text='Try Again', manager=self.manager,
                                                     anchors=anchd)

    def settings_menu(self):

        dropDownSize = (0, 0, 150, 60)
        dD_rect = pygame.Rect(dropDownSize)

        dD_rect.bottomright = (int(- self.SW / 2 + 50), -200)
        self.dropMenu = pygame_gui.elements.UISelectionList(dD_rect,['auto shooting', "manual shooting"],self.manager,
                                                    allow_multi_select=False, anchors=anchd)

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -100)
        self.confirm = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                         text='Confirm', manager=self.manager,
                                                         anchors=anchd)
