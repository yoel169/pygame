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
        hud_size = (SW2 - 50, SH2 - 470, 500, 380)
        self.hud_rect = py.Rect(hud_size)

        hudW = 500
        hudH = 380
        self.halfw = int(hudW/2)

        # todo: container for ui elements

        self.playerpanel = gui.elements.ui_panel.UIPanel(relative_rect=self.hud_rect, starting_layer_height=3, manager=self.manager,
                                                         object_id='playerpanel', anchors={'left': 'left',
                                                                    'right': 'right',
                                                                    'top': 'top',
                                                                    'bottom': 'bottom'})

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((75, 5), (300, 28)),
                                                text='Player Info: ', manager=self.manager, container=self.playerpanel
                                                , object_id='paneltitle')

    def setPlayer(self, db):

        self.playerpanel = gui.elements.ui_panel.UIPanel(relative_rect=self.hud_rect, starting_layer_height=3,
                                                         manager=self.manager,
                                                         object_id='playerpanel', anchors={'left': 'left',
                                                                                           'right': 'right',
                                                                                           'top': 'top',
                                                                                           'bottom': 'bottom'})

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((75, 5), (300, 28)),
                                                text='Player Info: ', manager=self.manager, container=self.playerpanel
                                                , object_id='paneltitle')

        self.player = db['player']
        self.stageinfo = db['stage']
        self.times = db['times']

        self.title_label.set_text(str(db['name']))

        self.dob_label = gui.elements.UILabel(relative_rect=py.Rect((25, 70), (220, 20)),
                                           text=('created: ' + str(self.times[0])), manager=self.manager,
                                              container=self.playerpanel, object_id='dobL')

        self.time2_label = gui.elements.UILabel(relative_rect=py.Rect((200, 70), (220, 20)),
                                              text=('last saved: ' + str(self.times[1])), manager=self.manager,
                                              container=self.playerpanel, object_id='time2L')

        self.label1 = gui.elements.UILabel(relative_rect=py.Rect((25, 100), (100, 20)),
                                           text='player info', manager=self.manager, container=self.playerpanel,
                                           object_id='label1')

        self.stage_label = gui.elements.UILabel(relative_rect=py.Rect((25, 120), (200, 20)),
                                                text=('stage: ' + str(self.stageinfo[0] + 1) + ', part:' +
                                                     str(self.stageinfo[1] + 1)), manager=self.manager,
                                                container=self.playerpanel,object_id='stageL')

        self.lives_label = gui.elements.UILabel(relative_rect=py.Rect((25, 150), (200, 20)),
                                               text=('lives: '+ str(self.player[3])),
                                               manager=self.manager, container=self.playerpanel, object_id='livesL')

        self.hp_label = gui.elements.UILabel(relative_rect=py.Rect((25, 170), (200, 20)),
                                                text=('health: ' + str(self.player[1]) + '/' +
                                                      str(self.player[2])), object_id='hpL',
                                                manager=self.manager, container=self.playerpanel)

        self.dam_label = gui.elements.UILabel(relative_rect=py.Rect((25, 200), (200, 20)),
                                                text=('damage: ' + str(self.player[4])),object_id='damL',
                                                manager=self.manager, container=self.playerpanel)

        self.pspeed_label = gui.elements.UILabel(relative_rect=py.Rect((25, 200), (200, 20)),
                                              text=('player speed: ' + str(self.player[5])), object_id='pspeedL',
                                              manager=self.manager, container=self.playerpanel)

        self.bspeed_label = gui.elements.UILabel(relative_rect=py.Rect((25, 200), (250, 20)),
                                                 text=('player speed: ' + str(self.player[6])), object_id='bspeedL',
                                                 manager=self.manager, container=self.playerpanel)

        self.bps_label = gui.elements.UILabel(relative_rect=py.Rect((25, 220), (200, 20)),
                                                text=('bps: ' + str(self.player[7]) + '/' +
                                                      str(self.player[8])), manager=self.manager, object_id='bpsL',
                                              container=self.playerpanel)

    def update(self, wave, score, score2, health, health2, lives, damage, bps, bspeed, money, time):
        self.wave_label.set_text(('wave: ' + str(wave) + '/' + str(self.maxWaves)))
        self.score_label.set_text(('Score: ' + str(score) + '/' + str(score2)))
        self.health_label.set_text(('Health: ' + str(health) + '/' + str(health2)))
        self.life_label.set_text(('Lives: ' + str(lives)))
        self.damage_label.set_text(('damage: ' + str(damage)))
        self.bps_label.set_text(('bullets every: ' + str(bps) + 'ms'))
        self.bspeed_label.set_text(('bullet speed: ' + str(bspeed)))
        self.money_label.set_text(('Money: ') + str(money))
        self.time_label.set_text('Time: ' + str(time) + 's')