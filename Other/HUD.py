import pygame as py
import pygame_gui as gui
from pygame.locals import K_p
from Other.Constants import Constants

# ========================================= GAME HUD ===============================================

SW, SH = Constants.screenSize

SW2 = int(SW/2)
SH2 = int(SW/2)


class HUD:
    def __init__(self, screen, manager, bg, title, part, partmax, waves):

        self.screen = screen
        self.manager = manager
        self.background = bg
        self.conf = None
        self.maxWaves = waves

        hud_size = (650, 0, 620, 100)
        hud_rect = py.Rect(hud_size)

        hudW = 620
        hudH = 100
        halfw = int(620/2)

        # todo: container for hud and rest of ui elements

        self.hud = gui.elements.ui_panel.UIPanel(relative_rect=hud_rect, starting_layer_height=3, manager=self.manager,
                                                 object_id='gamehud',anchors={'left': 'left',
                                                                    'right': 'right',
                                                                    'top': 'top',
                                                                    'bottom': 'bottom'})

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 5), (100, 20)),
                                                text=title,
                                                manager=self.manager, container=self.hud)

        self.part_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 25), (100, 20)),
                                                text=('Part: ' + str(part) + '/'+ str(partmax)),
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

        self.score_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 65), (150, 20)),
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

        self.pause_button = gui.elements.UIButton(relative_rect=py.Rect((hudW - 90, 20), (70, 50)),
                                               text='pause',
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

    # pause game with button or by pressing p
    def pause(self):

        runner = True
        clock = py.time.Clock()

        while(runner):

            time_delta = clock.tick(60)
            exit = False

            for event in py.event.get():
                if event.type == py.QUIT:
                    runner = False

                if event.type == py.KEYDOWN:
                    if event.key == K_p:
                        runner = False

                if event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.pause_button:
                            runner = False

                self.manager.process_events(event)

            self.screen.blit(self.background, (0, 0))

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            py.display.update()