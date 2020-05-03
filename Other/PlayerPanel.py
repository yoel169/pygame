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

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 5), (100, 20)),
                                                text='Player Info',
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