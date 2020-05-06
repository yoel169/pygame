import pygame as py
import pygame_gui as gui
from Other.Constants import Constants
from Other.GuiHelper import GuiHelper
# ========================================= GAME HUD ===============================================

SW, SH = Constants.screenSize

SW2 = int(SW/2)
SH2 = int(SH/2)


class PlayerPanel:
    def __init__(self, manager):

        self.manager = manager
        self.player = []
        self.stageinfo = []
        self.maker = GuiHelper(SW2, SW, self.manager)

        # todo: container for ui elements

    def setPlayer(self, db):

        self.playerpanel = self.maker.make_panel(SW2 - 450, 340, 430, 300, 'playerpanel')

        self.player = db['player']
        self.stageinfo = db['stage']
        self.times = db['times']

        height = 30

        self.stage_label = gui.elements.UILabel(relative_rect=py.Rect((30, height), (170, 20)),
                                                text=('Stage: ' + str(self.stageinfo[0] + 1) + ' Part: ' +
                                                     str(self.stageinfo[1] + 1)), manager=self.manager,
                                                container=self.playerpanel,object_id='stageL')

        self.lives_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 2), (170, 20)),
                                               text=('lives: '+ str(self.player[3])),
                                               manager=self.manager, container=self.playerpanel, object_id='livesL')

        self.hp_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 3), (170, 20)),
                                                text=('health: ' + str(self.player[1]) + '/' +
                                                      str(self.player[2])), object_id='hpL',
                                                manager=self.manager, container=self.playerpanel)

        self.dam_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 4), (170, 20)),
                                                text=('damage: ' + str(self.player[4])),object_id='damL',
                                                manager=self.manager, container=self.playerpanel)

        self.pspeed_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 5), (170, 20)),
                                              text=('player speed: ' + str(self.player[5])), object_id='pspeedL',
                                              manager=self.manager, container=self.playerpanel)

        self.bspeed_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 6), (170, 20)),
                                                 text=('bullet speed: ' + str(self.player[6])), object_id='bspeedL',
                                                 manager=self.manager, container=self.playerpanel)

        self.bps_label = gui.elements.UILabel(relative_rect=py.Rect((30, height * 7), (170, 20)),
                                                text=('bps: ' + str(self.player[7]) + '/' +
                                                      str(self.player[8])), manager=self.manager, object_id='bpsL',
                                              container=self.playerpanel)

        self.Level_label = gui.elements.UILabel(relative_rect=py.Rect((200, height), (170, 20)),
                                                text=("Player Level: "+ str(self.player[11])), manager=self.manager,
                                                container=self.playerpanel, object_id='stageL')

        self.xp_label = gui.elements.UILabel(relative_rect=py.Rect((200, height * 2), (170, 20)),
                                                text=("xp: " + str(self.player[10])), manager=self.manager,
                                                container=self.playerpanel, object_id='stageL')

        self.score_label = gui.elements.UILabel(relative_rect=py.Rect((200, height * 3), (170, 20)),
                                             text=("score: " + str(self.player[9])), manager=self.manager,
                                             container=self.playerpanel, object_id='stageL')

        self.money_label = gui.elements.UILabel(relative_rect=py.Rect((200, height * 4), (170, 20)),
                                                text=("money: " + str(self.player[12])), manager=self.manager,
                                                container=self.playerpanel, object_id='stageL')
