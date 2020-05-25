import pygame as py
import pygame_gui as gui
from pygame.locals import K_p
from Other.Constants import Constants
from Other.GuiHelper import GuiHelper

# ========================================= GAME HUD ===============================================

SW, SH = Constants.screenSize

SW2 = int(SW / 2)
SH2 = int(SH / 2)


class HUD:
    def __init__(self, screen, manager, bg, title, part, partmax, waves):

        self.screen = screen
        self.manager = manager
        self.background = bg
        self.maxWaves = waves
        self.maker = GuiHelper(SW, SH, manager)
        hud_size = (650, 0, 650, 150)
        hud_rect = py.Rect(hud_size)

        hudW = 650
        hudH = 150
        halfw = int(650 / 2)

        # todo: container for hud and rest of ui elements

        self.hud = self.maker.make_panel(SW2, 75, 650, 140, 'HUD')

        part_string = 'Part: ' + str(part) + '/' + str(partmax)

        # left
        self.damage_label = self.maker.make_label(100, 15, 180, 20, '', 'hud_damage', self.hud)
        self.bps_label = self.maker.make_label(100, 35, 200, 20, '', 'hud_bps', self.hud)
        self.bspeed_label = self.maker.make_label(100, 55, 200, 20, '', 'hud_bspeed', self.hud)

        # middle section (stage info)
        self.title_label = self.maker.make_label(halfw - 35, 15, 150, 20, title, 'hud_stage', self.hud)
        self.part_label = self.maker.make_label(halfw - 35, 35, 150, 20, part_string, 'hud_part', self.hud)
        self.wave_label = self.maker.make_label(halfw - 35, 55, 150, 20, '', 'hud_wave', self.hud)
        self.score_label = self.maker.make_label(halfw - 35, 75, 150, 20, '', 'hud_part', self.hud)

        # right
        self.life_label = self.maker.make_label(halfw + 110, 15, 150, 20, '', 'hud_life', self.hud)
        self.health_label = self.maker.make_label(halfw + 110, 35, 150, 20, '', 'hud_health', self.hud)
        self.money_label = self.maker.make_label(halfw + 110, 55, 150, 20, '', 'hud_money', self.hud)
        self.xp_label = self.maker.make_label(halfw + 110, 85, 75, 20, '', 'hud_xp', self.hud)

        # right right
        self.pause_button = self.maker.make_button(halfw + 230, 45, 70, 50, 'menu', self.hud)
        self.time_label = self.maker.make_label(halfw + 230, 85, 150, 20, '', 'hud_time', self.hud)

    def update(self, wave, score, score2, health, health2, lives, lives2, damage, damage2, bps, bps2, bspeed,
               money, xp, time):
        self.wave_label.set_text(('wave: ' + str(wave) + '/' + str(self.maxWaves)))
        self.score_label.set_text(('Score: ' + str(score) + '/' + str(score2)))
        self.health_label.set_text('Health: %.2f/%d' % (health, health2))
        self.life_label.set_text(('Lives: ' + str(lives)) + '/' + str(lives2))
        self.damage_label.set_text('damage: %.2f/%d' % (damage, damage2))
        self.bps_label.set_text(('bullets every: ' + str(bps) + 'ms' + '/' + str(bps2) + 'ms'))
        self.bspeed_label.set_text('bullet speed: %.2f' % bspeed)
        self.money_label.set_text('Money: $%.2f' % money)
        self.time_label.set_text('Time: ' + str(time) + 's')
        self.xp_label.set_text('XP: %.2f' % xp)

    # pause game with button or by pressing p
    def pause(self):
        pause_panel = self.maker.make_panel(SW2, SH2, 200, 200, 'pause_panel')
        cont_button = self.maker.make_button(90, 60, 80, 50, 'continue', pause_panel)
        exit_button = self.maker.make_button(90, 110, 80, 50, 'exit', pause_panel)

        exit = False
        runner = True
        clock = py.time.Clock()

        while (runner):

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
