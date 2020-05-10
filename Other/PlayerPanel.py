import pygame as py
import pygame_gui as gui
from Other.Constants import Constants
from Other.GuiHelper import GuiHelper

# ========================================= GAME HUD ===============================================

SW, SH = Constants.screenSize

SW2 = int(SW / 2)
SH2 = int(SH / 2)


class PlayerPanel:
    def __init__(self, manager):
        self.manager = manager
        self.player = []
        self.stageinfo = []
        self.maker = GuiHelper(SW2, SW, self.manager)

        # todo: container for ui elements

    def setPlayer(self, db):
        self.playerpanel = self.maker.make_panel(SW2 - 100, SH2, 430, 300, 'playerpanel')

        self.player = db['player']
        self.stageinfo = db['stage']
        self.times = db['times']

        height = 30

        self.stage_label = gui.elements.UILabel(relative_rect=py.Rect((30, height), (170, 20)),
                                                text=('Stage: ' + str(self.stageinfo[0] + 1) + ' Part: ' +
                                                      str(self.stageinfo[1] + 1)), manager=self.manager,
                                                container=self.playerpanel, object_id='stageL')

        lives_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 2), (170, 20)),
                                           text=('lives: ' + str(self.player['lives']) + '/' +
                                                 str(self.player['base_lives'])),
                                           manager=self.manager, container=self.playerpanel, object_id='livesL')

        hp_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 3), (170, 20)),
                                        text=('health: ' + str(self.player['health']) + '/' +
                                              str(self.player['maxHealth'])), object_id='hpL',
                                        manager=self.manager, container=self.playerpanel)

        dam_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 4), (170, 20)),
                                         text=('damage: ' + str(self.player['damage']) + '/' +
                                               str(self.player['damage_max'])), object_id='damL',
                                         manager=self.manager, container=self.playerpanel)

        pspeed_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 5), (170, 20)),
                                            text=('player speed: ' + str(self.player['pspeed'])) + '/' +
                                                 str(self.player['pspeed_max']), object_id='pspeedL',
                                            manager=self.manager, container=self.playerpanel)

        bspeed_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 6), (170, 20)),
                                            text=('bullet speed: ' + str(self.player['bspeed'])), object_id='bspeedL',
                                            manager=self.manager, container=self.playerpanel)

        bps_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 7), (170, 20)),
                                         text=('bps: ' + str(self.player['bps']) + '/' +
                                               str(self.player['bpsMax'])), manager=self.manager, object_id='bpsL',
                                         container=self.playerpanel)

        Level_label = gui.elements.UILabel(relative_rect=py.Rect((200, height), (170, 20)),
                                           text=("Player Level: " + str(self.player['level'])), manager=self.manager,
                                           container=self.playerpanel, object_id='stageL')

        xp_label = gui.elements.UILabel(relative_rect=py.Rect((200, height * 2), (170, 20)),
                                        text=("xp: " + str(self.player['xp'])), manager=self.manager,
                                        container=self.playerpanel, object_id='stageL')

        score_label = gui.elements.UILabel(relative_rect=py.Rect((200, height * 3), (170, 20)),
                                           text=("score: " + str(self.player['score'])), manager=self.manager,
                                           container=self.playerpanel, object_id='stageL')

        money_label = gui.elements.UILabel(relative_rect=py.Rect((200, height * 4), (170, 20)),
                                           text=("money: " + str(self.player['money'])), manager=self.manager,
                                           container=self.playerpanel, object_id='stageL')

        unlock_points_label = self.maker.make_label(285, (height * 5) + 20, 170, 30,
                                                    ('unlock points: ' + str(self.player['player_points'])),
                                                    'playerpoints',
                                                    self.playerpanel)
