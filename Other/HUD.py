import pygame as py
import pygame_gui as gui
from pygame.locals import K_p
from Other.Constants import Constants
from Other.GuiHelper import GuiHelper
# ========================================= GAME HUD ===============================================

SW, SH = Constants.screenSize

SW2 = int(SW/2)
SH2 = int(SH/2)


class HUD:
    def __init__(self, screen, manager, bg, title, part, partmax, waves):

        self.screen = screen
        self.manager = manager
        self.background = bg
        self.maxWaves = waves
        self.maker = GuiHelper(SW, SH, manager)
        hud_size = (650, 0, 650, 140)
        hud_rect = py.Rect(hud_size)

        hudW = 620
        hudH = 100
        halfw = int(620/2)

        # todo: container for hud and rest of ui elements

        self.hud = gui.elements.ui_panel.UIPanel(relative_rect=hud_rect, starting_layer_height=3, manager=self.manager,
                                                 object_id='HUD',anchors={'left': 'left',
                                                                    'right': 'right',
                                                                    'top': 'top',
                                                                    'bottom': 'bottom'})

        self.title_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 5), (100, 20)),
                                                text=title,
                                                manager=self.manager, container=self.hud, object_id='hud_stage')

        self.part_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 60, 25), (100, 20)),
                                                text=('Part: ' + str(part) + '/'+ str(partmax)),
                                                manager=self.manager, container=self.hud, object_id='hud_part')

        self.time_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 50, 65), (200, 20)),
                                               text=('Time: '),  object_id='hud_time',
                                               manager=self.manager, container=self.hud)

        self.life_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 50, 5), (200, 20)),
                                               text='Lives: 0', object_id='hud_life',
                                               manager=self.manager, container=self.hud)

        self.health_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 90, 25), (120, 20)),
                                                 text='Health: 0', object_id='hud_health',
                                                 manager=self.manager, container=self.hud)

        self.score_label = gui.elements.UILabel(relative_rect=py.Rect((halfw - 80, 65), (150, 20)),
                                                text='Score: 0', object_id='hud_score',
                                                manager=self.manager, container=self.hud)

        self.money_label = gui.elements.UILabel(relative_rect=py.Rect((halfw + 50, 45), (200, 20)),
                                                text='Money: 0', object_id='hud_money',
                                                manager=self.manager, container=self.hud)

        self.wave_label = gui.elements.UILabel(relative_rect=py.Rect((0, 5), (200, 20)),
                                                 text='wave: ', object_id='hud_wave',
                                                 manager=self.manager, container=self.hud)

        self.damage_label = gui.elements.UILabel(relative_rect=py.Rect((0, 25), (200, 20)),
                                                text='damage: ', object_id='hud_damage',
                                                manager=self.manager, container=self.hud)

        self.bps_label = gui.elements.UILabel(relative_rect=py.Rect((0, 45), (200, 20)),
                                                 text='bullets every: ', object_id='hud_bps',
                                                 manager=self.manager, container=self.hud)

        self.bspeed_label = gui.elements.UILabel(relative_rect=py.Rect((0, 65), (200, 20)),
                                                 text='bullet speed: ', object_id='hud_bspeed',
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

        pause_panel = self.maker.make_panel(SW2 - 150, SH2 - 150, 200, 200, 'pause_panel')
        cont_button = self.maker.make_button(120,70,70,50,'continue', pause_panel)
        exit_button = self.maker.make_button(120,140,70,50,'exit', pause_panel)

        exit = False

        while(runner):

            time_delta = clock.tick(60)

            for event in py.event.get():
                if event.type == py.QUIT:
                    runner = False

                if event.type == py.KEYDOWN:
                    if event.key == K_p:
                        runner = False

                if event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.pause_button or event.ui_element == cont_button:
                            runner = False

                        elif event.ui_element == exit_button:
                            exit = True
                            runner = False

                self.manager.process_events(event)

            self.screen.blit(self.background, (0, 0))

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            py.display.update()

        cont_button.kill()
        exit_button.kill()
        pause_panel.kill()
        return exit