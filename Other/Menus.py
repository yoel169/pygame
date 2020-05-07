from Other.GuiHelper import GuiHelper
from Other.PlayerPanel import PlayerPanel


# ====================================== MENUS FOR GAME ===============================================
# For buttons use 70 pixel space between buttons in height


class GameMenu():
    def __init__(self, width, height, manager):
        self.SW = width
        self.SH = height
        self.manager = manager

        # main menu
        self.play_b = None
        self.info_b = None
        self.setting_b = None
        self.quit_b = None

        # replay
        self.replay_b = None
        self.quit_replay_b = None

        # settings
        self.movement_selection = None
        self.screen_selection = None
        self.shoot_selection = None
        self.confirm_setting_b = None

        # next level
        self.next_level_b = None
        self.quit_next_level_b = None

        # profile select
        self.save_selection = None
        self.launch_hub_b = None
        self.quit_launcher_b = None

        # player hub
        self.cont_b = None
        self.unlocks_b = None
        self.stats_b = None
        self.back_b = None
        self.player_panel = PlayerPanel(self.manager)
        self.pick_b = None
        self.pick_ddm = None

        # gui helper maker
        self.maker = GuiHelper(self.SW, self.SH, self.manager)
        self.SW2 = int(self.SW / 2)
        self.SH2 = int(self.SH / 2)

    def main_menu(self):
        # buttonS2 = (70, 60)

        title = self.maker.make_label(self.SW2 + 500, 300, 1000, 110, 'WORLD FLYING SHOOTER', 'maintitle', None)

        button_s = (150, 60)
        height = self.SH2 + 20

        self.play_b = self.maker.make_button(self.SW2, height, button_s[0], button_s[1], 'Play', None)

        self.info_b = self.maker.make_button(self.SW2, height + 70, button_s[0], button_s[1], 'How to Play', None)

        self.setting_b = self.maker.make_button(self.SW2, height + (70 * 2), button_s[0], button_s[1], 'Settings', None)

        self.quit_b = self.maker.make_button(self.SW2, height + (70 * 3), button_s[0], button_s[1], 'Quit', None)

    def replay_menu(self, string):
        title = self.maker.make_label(self.SW2 + 50, self.SH2, 240, 90, string, 'replay', None)

        button_s = (150, 60)

        self.replay_b = self.maker.make_button(self.SW2, self.SH2 + 150, button_s[0], button_s[1], 'play again', None)

        self.quit_replay_b = self.maker.make_button(self.SW2, self.SH2 + 220, button_s[0], button_s[1], 'back to hub',
                                                    None)

    def settings_menu(self):
        button_s = (150, 60)

        self.movement_selection = self.maker.make_selection_list(self.SW2, self.SH2, 200, 70,
                                                                 ['arrow keys', "wads keys", "mouse"], 'movementS',
                                                                 None)

        self.screen_selection = self.maker.make_selection_list(self.SW2, self.SH2 + 100, 200, 70,
                                                               ["fullscreen", "hardware accelerated",
                                                                "windowed"], 'screenS', None)

        self.shoot_selection = self.maker.make_selection_list(self.SW2, self.SH2 + 200, 200, 70,
                                                              ['auto', "space", "mouse"], 'shootS', None)

        self.confirm_setting_b = self.maker.make_button(self.SW2 - 30, self.SH2 + 300, button_s[0], button_s[1], 'exit'
                                                        , None)

    def next_level(self, string):
        label_size = (240, 90)
        button_s = (150, 60)

        title = self.maker.make_label(self.SW2 + 50, self.SH2, label_size[0], label_size[1], string, 'nextlevel', None)

        self.next_level_b = self.maker.make_button(self.SW2, self.SH2 + 150, button_s[0], button_s[1], string
                                                   , None)

        self.quit_next_level_b = self.maker.make_button(self.SW2, self.SH2 + 220, button_s[0], button_s[1],
                                                        'back to hub'
                                                        , None)

    # pick between file saves
    def load_menu(self, names):
        todo = ''
        # labelSize = (0, 0, 150, 40)
        # label_rect = pygame.Rect(labelSize)
        #
        # label_rect.bottomright = (int(- self.SW / 2) + 20, -700)
        # label1 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Pick a save',
        #                                      manager=self.manager, anchors=anchd, object_id='saveFL')
        #
        # shootDSize = (0, 0, 200, 150)
        # dD_rect = pygame.Rect(shootDSize)
        #
        # dD_rect.bottomright = (int(- self.SW / 2 + 50), -520)
        # self.savelist_selection = pygame_gui.elements.UISelectionList(dD_rect, names, object_id='loadS',
        #                                                         manager =self.manager, allow_multi_select=False,
        #                                                               anchors=anchd)
        #
        # buttonSize = (0, 0, 150, 60)
        # button_layout_rect = pygame.Rect(buttonSize)
        #
        # button_layout_rect.bottomright = (int(-self.SW / 2) + 20, -400)
        # self.loadConfirm_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
        #                                             text='Confirm', manager=self.manager,
        #                                             anchors=anchd)

    # save menu
    def save_menu(self, names):
        todo = ''

        # labelSize = (0, 0, 150, 40)
        # label_rect = pygame.Rect(labelSize)
        # labesize2 = (0,0,210,40)
        #
        # label_rect.bottomright = (int(- self.SW / 2) + 25, -700)
        # label1 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Pick a save',
        #                                     manager=self.manager, anchors=anchd, object_id='saveFL')
        #
        # shootDSize = (0, 0, 200, 150)
        # dD_rect = pygame.Rect(shootDSize)
        #
        # dD_rect.bottomright = (int(- self.SW / 2 + 50), -500)
        # self.savelist2_selection = pygame_gui.elements.UISelectionList(dD_rect, names, object_id= 'saveS',
        #                                                         manager= self.manager, allow_multi_select=False,
        #                                                                anchors=anchd)
        #
        # label_rect = pygame.Rect(labesize2)
        # label_rect.bottomright = (int(- self.SW / 2 + 60), -400)
        # label2 = pygame_gui.elements.UILabel(relative_rect=label_rect, text='Or new save',
        #                                      manager=self.manager, anchors=anchd, object_id='saveFL2')
        #
        # buttonSize = (0, 0, 150, 60)
        # button_layout_rect = pygame.Rect(buttonSize)
        #
        # button_layout_rect.bottomright = (int(-self.SW / 2) - 100, -170)
        # self.saveConfirm_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
        #                                             text='Confirm', manager=self.manager,
        #                                             anchors=anchd)
        #
        # button_layout_rect.bottomright = (int(-self.SW / 2) + 100, -170)
        # self.cancel_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
        #                                                        text='Cancel', manager=self.manager,
        #                                                        anchors=anchd)

    # description menu TODO
    def info_menu(self):
        todo = ''
        # labelSize = (0, 0, 500, 120)
        # label_rect = pygame.Rect(labelSize)
        #
        # label_rect.bottomright = (int(- self.SW / 2 + 200), -600)
        # title = pygame_gui.elements.UILabel(relative_rect=label_rect, text='no exit',
        #                                     manager=self.manager, anchors=anchd)

    # get player save or make a new one
    def launch_menu(self, names):
        label1 = self.maker.make_label(self.SW2, self.SH2 - 170, 210, 40, 'Load a Save', 'l1', None)

        self.save_selection = self.maker.make_selection_list(self.SW2, self.SH2, 200, 150, names, 'saveS', None)

        label2 = self.maker.make_label(self.SW2, self.SH2 + 100, 210, 40, 'Or New Profile', 'l2', None)

        self.launch_hub_b = self.maker.make_button(self.SW2 + 50, self.SH2 + 300, 150, 60, 'Go', None)
        self.quit_launcher_b = self.maker.make_button(self.SW2 - 100, self.SH2 + 300, 150, 60, 'Back', None)

    # player hub
    def player_hub(self, player_save, stages):
        # menu buttons
        self.cont_b = self.maker.make_button(400, 330, 150, 60, 'continue', None)
        self.pick_b = self.maker.make_button(300, 400, 50, 60, 'Go', None)
        self.pick_ddm = self.maker.make_drop_down_menu(300, 340, 100, 60, 'pick_ddm', stages)
        self.unlocks_b = self.maker.make_button(400, 470, 150, 60, 'unlocks', None)
        self.stats_b = self.maker.make_button(400, 540, 150, 60, 'stats', None)
        self.setting_b = self.maker.make_button(400, 610, 150, 60, 'settings', None)
        self.back_b = self.maker.make_button(400, 680, 150, 60, 'save and exit', None)

        # player info panel
        self.player_panel.setPlayer(player_save)

        #  -------------------------------------- player name panel ------------------------------------------
        name_panel = self.maker.make_panel(self.SW2 - 300, 80, 400, 180, 'namepanel')

        # title
        string = "Welcome Back " + str(player_save['name'])
        player_name = self.maker.make_label(330, 40, 300, 30, string, 'playername', name_panel)

        # times
        times = player_save['times']
        string = 'Created: ' + str(times[0])
        dob_label = self.maker.make_label(320, 80, 260, 20, string, 'dobL', name_panel)

        string = 'Last played: ' + str(times[1])
        last_save_label = self.maker.make_label(320, 120, 260, 20, string, 'time2L', name_panel)
