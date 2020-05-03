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
        self.conf = None

        hud_size = (SW2 - 50, SH2 - 470, 400, 380)
        hud_rect = py.Rect(hud_size)

        hudW = 400
        hudH = 380
        halfw = int(hudW/2)

        # todo: container for ui elements

        self.hud = gui.elements.ui_panel.UIPanel(relative_rect=hud_rect, starting_layer_height=3, manager=self.manager,
                                                 object_id='playerpanel',anchors={'left': 'left',
                                                                    'right': 'right',
                                                                    'top': 'top',
                                                                    'bottom': 'bottom'})

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((120, 10), (120, 30)),
                                                text='Player Info', manager=self.manager, container=self.hud
                                                , object_id='paneltitle')

        self.stage_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 25), (100, 20)),
                                               text=('Part: ' + str(part) + '/' + str(partmax)),
                                               manager=self.manager, container=self.hud)

        self.time_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 50, 65), (200, 20)),
                                               text=('Time: '),
                                               manager=self.manager, container=self.hud)

        self.life_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 50, 5), (200, 20)),
                                               text='Lives: 0',
                                               manager=self.manager, container=self.hud)

        self.health_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 90, 25), (120, 20)),
                                                 text='Health: 0',
                                                 manager=self.manager, container=self.hud)

        self.score_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 65), (100, 20)),
                                                text='Score: 0',
                                                manager=self.manager, container=self.hud)

        self.money_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 50, 45), (200, 20)),
                                                text='Money: 0',
                                                manager=self.manager, container=self.hud)

        self.wave_label = gui.elements.UILabel(relative_rect=py.Rect((0, 5), (200, 20)),
                                               text='wave: ',
                                               manager=self.manager, container=self.hud)

        self.damage_label = gui.elements.UILabel(relative_rect=py.Rect((0, 25), (200, 20)),
                                                 text='damage: ',
                                                 manager=self.manager, container=self.hud)

        self.bps_label = gui.elements.UILabel(relative_rect=py.Rect((0, 45), (200, 20)),
                                              text='bullets every: ',
                                              manager=self.manager, container=self.hud)

        self.bspeed_label = gui.elements.UILabel(relative_rect=py.Rect((0, 65), (200, 20)),
                                                 text='bullet speed: ',
                                                 manager=self.manager, container=self.hud)

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