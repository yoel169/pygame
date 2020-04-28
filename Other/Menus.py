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
        self.setting_button2 = None
        self.movementMenu = None
        self.nextL_button = None
        self.setting_button3 = None

    def main_menu(self):
        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        labelSize = (0, 0,1000, 150)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int( - self.SW / 2 + 500), -650)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text= ' WORLD FLYING SHOOTER',
                                            manager=self.manager, anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -450)
        self.play_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Play', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -380)
        self.info_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Instructions', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -310)
        self.setting_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Settings', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -240)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Quit', manager=self.manager,
                                                   anchors=anchd)

    def replay_menu(self):
        labelSize = (0, 0, 500, 120)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2 + 200), -600)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text='play again?',
                                            manager=self.manager, anchors=anchd)

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -400)
        self.replay_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                          text='try again', manager=self.manager,
                                                          anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -320)
        self.setting_button2 = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                          text='settings', manager=self.manager,
                                                          anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -240)
        self.quit_button2 = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='quit to menu', manager=self.manager,
                                                   anchors=anchd)

    def settings_menu(self):

        shootDSize = (0, 0, 200, 70)
        dD_rect = pygame.Rect(shootDSize)

        dD_rect.bottomright = (int(- self.SW / 2 + 50), -550)
        self.movementMenu = pygame_gui.elements.UISelectionList(dD_rect, ['arrow keys', "wads keys", "mouse"],
                                                             self.manager,
                                                             allow_multi_select=False, anchors=anchd)

        dD_rect.bottomright = (int(- self.SW / 2 + 50), -450)
        self.screenMenu = pygame_gui.elements.UISelectionList(dD_rect, ["fullscreen", "hardware accelerated",
                                                                        "windowed"], self.manager,
                                                              allow_multi_select=False, anchors=anchd)
        shootDSize = (0, 0, 200, 70)
        dD_rect = pygame.Rect(shootDSize)

        dD_rect.bottomright = (int(- self.SW / 2 + 50), -350)
        self.shootMenu = pygame_gui.elements.UISelectionList(dD_rect,['auto', "space", "mouse"], self.manager,
                                                    allow_multi_select=False, anchors=anchd)

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 20, -200)
        self.confirm = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                         text='Confirm', manager=self.manager,
                                                         anchors=anchd)

    def nextLevel(self):

        labelSize = (0, 0, 500, 120)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2 + 200), -600)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text='you won!',
                                            manager=self.manager, anchors=anchd)

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -400)
        self.nextL_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                          text='next level', manager=self.manager,
                                                          anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -320)
        self.setting_button3 = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                            text='settings', manager=self.manager,
                                                            anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 50, -240)
        self.quit_button2 = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                         text='quit to menu', manager=self.manager,
                                                         anchors=anchd)