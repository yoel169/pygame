import pygame as py
import pygame_gui as gui
from Other.Constants import Constants

# ========================================= GAME HUD ===============================================

SW, SH = Constants.screenSize

SW2 = int(SW/2)
SH2 = int(SW/2)


class PlayerPanel:
    def __init__(self, screen, manager, bg):

        self.screen = screen
        self.manager = manager
        self.background = bg
        self.player = []
        self.stageinfo = []
        hud_size = (500, 300, 500, 380)
        self.hud_rect = py.Rect(hud_size)

        hudW = 500
        hudH = 380
        self.halfw = int(hudW/2)

        # todo: container for ui elements

    def setPlayer(self, db):

        self.playerpanel = gui.elements.ui_panel.UIPanel(relative_rect=self.hud_rect, starting_layer_height=3,
                                                         manager=self.manager,
                                                         object_id='playerpanel', anchors={'left': 'left',
                                                                                           'right': 'right',
                                                                                           'top': 'top',
                                                                                           'bottom': 'bottom'})

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((75, 5), (300, 28)),
                                                text=('Welcome ' + str(db['name'])), manager=self.manager, container=self.playerpanel
                                                , object_id='paneltitle')

        self.player = db['player']
        self.stageinfo = db['stage']
        self.times = db['times']

        self.dob_label = gui.elements.UILabel(relative_rect=py.Rect((100, 50), (260, 20)),
                                           text=('created: ' + str(self.times[0])), manager=self.manager,
                                              container=self.playerpanel, object_id='dobL')

        self.time2_label = gui.elements.UILabel(relative_rect=py.Rect((100, 80), (260, 20)),
                                              text=('last saved: ' + str(self.times[1])), manager=self.manager,
                                              container=self.playerpanel, object_id='time2L')

        self.stage_label = gui.elements.UILabel(relative_rect=py.Rect((35, 130), (170, 20)),
                                                text=('Stage: ' + str(self.stageinfo[0] + 1) + ' Part: ' +
                                                     str(self.stageinfo[1] + 1)), manager=self.manager,
                                                container=self.playerpanel,object_id='stageL')

        self.lives_label = gui.elements.UILabel(relative_rect=py.Rect((80, 160), (90, 20)),
                                               text=('lives: '+ str(self.player[3])),
                                               manager=self.manager, container=self.playerpanel, object_id='livesL')

        self.hp_label = gui.elements.UILabel(relative_rect=py.Rect((40, 190), (170, 20)),
                                                text=('health: ' + str(self.player[1]) + '/' +
                                                      str(self.player[2])), object_id='hpL',
                                                manager=self.manager, container=self.playerpanel)

        self.dam_label = gui.elements.UILabel(relative_rect=py.Rect((70, 220), (100, 20)),
                                                text=('damage: ' + str(self.player[4])),object_id='damL',
                                                manager=self.manager, container=self.playerpanel)

        self.pspeed_label = gui.elements.UILabel(relative_rect=py.Rect((45, 250), (170, 20)),
                                              text=('player speed: ' + str(self.player[5])), object_id='pspeedL',
                                              manager=self.manager, container=self.playerpanel)

        self.bspeed_label = gui.elements.UILabel(relative_rect=py.Rect((45, 280), (170, 20)),
                                                 text=('bullet speed: ' + str(self.player[6])), object_id='bspeedL',
                                                 manager=self.manager, container=self.playerpanel)

        self.bps_label = gui.elements.UILabel(relative_rect=py.Rect((50, 310), (150, 20)),
                                                text=('bps: ' + str(self.player[7]) + '/' +
                                                      str(self.player[8])), manager=self.manager, object_id='bpsL',
                                              container=self.playerpanel)

        self.Level_label = gui.elements.UILabel(relative_rect=py.Rect((220, 130), (170, 20)),
                                                text=("Player Level: "+ str(self.player[11])), manager=self.manager,
                                                container=self.playerpanel, object_id='stageL')

        self.xp_label = gui.elements.UILabel(relative_rect=py.Rect((220, 160), (170, 20)),
                                                text=("xp: " + str(self.player[10])), manager=self.manager,
                                                container=self.playerpanel, object_id='stageL')

        self.score_label = gui.elements.UILabel(relative_rect=py.Rect((220, 190), (170, 20)),
                                             text=("score: " + str(self.player[9])), manager=self.manager,
                                             container=self.playerpanel, object_id='stageL')

        self.money_label = gui.elements.UILabel(relative_rect=py.Rect((220, 220), (170, 20)),
                                                text=("money: " + str(self.player[12])), manager=self.manager,
                                                container=self.playerpanel, object_id='stageL')

    def redraw(self):
        self.playerpanel = gui.elements.ui_panel.UIPanel(relative_rect=self.hud_rect, starting_layer_height=3,
                                                         manager=self.manager,
                                                         object_id='playerpanel', anchors={'left': 'left',
                                                                                           'right': 'right',
                                                                                           'top': 'top',
                                                                                           'bottom': 'bottom'})

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((75, 5), (300, 28)),
                                                text='Player Info: ', manager=self.manager, container=self.playerpanel
                                                , object_id='paneltitle')
