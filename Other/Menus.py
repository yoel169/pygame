import pygame
import pygame_gui
from Other.InputBox import InputBox
# ====================================== MENUS FOR GAME ===============================================

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
        self.savelist_selection = None
        self.savelist2_selection = None
        self.loadConfirm_button = None
        self.saveConfirm_button = None
        self.cancel_button = None
        self.launch_button = None
        self.load_button = None
        self.save_button = None
        self.setting_button = None
        self.setting_button2 = None
        self.setting_button3 = None
        self.shootMenu = None
        self.screenMenu = None
        self.movementMenu = None
        self.quit_button3 = None

    def main_menu(self):
        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        buttonSize2 = (0, 0, 70, 60)
        save_load_rect = pygame.Rect(buttonSize2)

        labelSize = (0, 0,1000, 110)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int( - self.SW / 2 + 500), -650)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text= ' WORLD FLYING SHOOTER',
                                            manager=self.manager, anchors=anchd, object_id='maintitle')

        button_layout_rect.bottomright = (int(-self.SW / 2) - 200, -450)
        self.play_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Play', manager=self.manager,
                                                   anchors=anchd, object_id='playbutton')

        save_load_rect.bottomright = (int(-self.SW / 2) - 280, -380)
        self.save_button = pygame_gui.elements.UIButton(relative_rect=save_load_rect,
                                                        text='Save', manager=self.manager,
                                                        anchors=anchd)

        save_load_rect.bottomright = (int(-self.SW / 2) -200, -380)
        self.load_button = pygame_gui.elements.UIButton(relative_rect=save_load_rect,
                                                        text='Load', manager=self.manager,
                                                        anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) -200, -310)
        self.info_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Instructions', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) - 200, -240)
        self.setting_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Settings', manager=self.manager,
                                                   anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) - 200, -170)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                   text='Quit', manager=self.manager,
                                                   anchors=anchd)

    def replay_menu(self, string):
        labelSize = (0, 0, 220, 90)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2) + 90, -600)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text=string,
                                            manager=self.manager, anchors=anchd, object_id='replay')

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

    def nextLevel(self, string):
        labelSize = (0, 0, 240, 90)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2 + 110), -600)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text=string,
                                            manager=self.manager, anchors=anchd, object_id='nextlevel')

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
        self.quit_button3 = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                         text='quit to menu', manager=self.manager,
                                                         anchors=anchd)

    # pick between file saves
    def load_menu(self, names):
        labelSize = (0, 0, 150, 40)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2) + 20, -700)
        label1 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Pick a save',
                                             manager=self.manager, anchors=anchd, object_id='saveFL')

        shootDSize = (0, 0, 200, 150)
        dD_rect = pygame.Rect(shootDSize)

        dD_rect.bottomright = (int(- self.SW / 2 + 50), -520)
        self.savelist_selection = pygame_gui.elements.UISelectionList(dD_rect, names, object_id='loadS',
                                                                manager =self.manager, allow_multi_select=False,
                                                                      anchors=anchd)

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 20, -400)
        self.loadConfirm_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                    text='Confirm', manager=self.manager,
                                                    anchors=anchd)
    # save menu
    def save_menu(self, names):

        labelSize = (0, 0, 150, 40)
        label_rect = pygame.Rect(labelSize)
        labesize2 = (0,0,210,40)

        label_rect.bottomright = (int(- self.SW / 2) + 25, -700)
        label1 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Pick a save',
                                            manager=self.manager, anchors=anchd, object_id='saveFL')

        shootDSize = (0, 0, 200, 150)
        dD_rect = pygame.Rect(shootDSize)

        dD_rect.bottomright = (int(- self.SW / 2 + 50), -500)
        self.savelist2_selection = pygame_gui.elements.UISelectionList(dD_rect, names, object_id= 'saveS',
                                                                manager= self.manager, allow_multi_select=False,
                                                                       anchors=anchd)

        label_rect = pygame.Rect(labesize2)
        label_rect.bottomright = (int(- self.SW / 2 + 60), -400)
        label2 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Or new save',
                                             manager=self.manager, anchors=anchd, object_id='saveFL2')

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) - 100, -170)
        self.saveConfirm_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                    text='Confirm', manager=self.manager,
                                                    anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 100, -170)
        self.cancel_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                               text='Cancel', manager=self.manager,
                                                               anchors=anchd)

    # description menu
    def info_menu(self):
        labelSize = (0, 0, 500, 120)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2 + 200), -600)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text='no exit',
                                            manager=self.manager, anchors=anchd)

    def launchMenu(self, names):
        labelSize = (0, 0, 1000, 110)
        label_rect = pygame.Rect(labelSize)

        label_rect.bottomright = (int(- self.SW / 2 + 500), -750)
        title = pygame_gui.elements.UILabel(relative_rect=label_rect, text=' WORLD FLYING SHOOTER',
                                            manager=self.manager, anchors=anchd, object_id='maintitle')

        labelSize = (0, 0, 150, 40)
        label_rect = pygame.Rect(labelSize)
        labesize2 = (0, 0, 210, 40)

        label_rect.bottomright = (int(- self.SW / 2) + 25, -650)
        label1 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Pick a save',
                                             manager=self.manager, anchors=anchd, object_id='saveFL')

        shootDSize = (0, 0, 200, 150)
        dD_rect = pygame.Rect(shootDSize)

        dD_rect.bottomright = (int(- self.SW / 2 + 50), -480)
        self.savelist_selection = pygame_gui.elements.UISelectionList(dD_rect, names, object_id='saveS',
                                                                       manager=self.manager, allow_multi_select=False,
                                                                       anchors=anchd)

        label_rect = pygame.Rect(labesize2)
        label_rect.bottomright = (int(- self.SW / 2 + 60), -380)
        label2 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Or new profile',
                                             manager=self.manager, anchors=anchd, object_id='saveFL2')

        buttonSize = (0, 0, 150, 60)
        button_layout_rect = pygame.Rect(buttonSize)

        button_layout_rect.bottomright = (int(-self.SW / 2) - 60, -170)
        self.launch_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                               text='Confirm', manager=self.manager,
                                                               anchors=anchd)

        button_layout_rect.bottomright = (int(-self.SW / 2) + 110, -170)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                          text='Exit', manager=self.manager,
                                                          anchors=anchd)