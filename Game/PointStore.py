import pygame as py
import pygame_gui as gui
from Other.Constants import Constants
from Other.GuiHelper import GuiHelper
from pygame.locals import (
    K_ESCAPE)

SW, SH = Constants.screenSize

SW2 = int(SW / 2)
SH2 = int(SH / 2)


class PointStore:
    def __init__(self, screen, bg, manager):
        self.screen = screen
        self.manager = manager
        self.screen = screen
        self.background = bg
        self.maker = GuiHelper(SW, SH, self.manager)

        self.leave_b = None
        self.player = None
        self.bullet_title = None
        self.current_label = None
        self.b_price = None
        self.stat_title = None
        self.current_label_stat = None
        self.stat_price = None
        self.money_label = None
        self.selected = None

    def run(self, player):
        time_delta = 0
        runner = True
        clock = py.time.Clock()
        self.selected = player.current_track

        store_panel = self.maker.make_panel(SW2, SH2, 650, 800, 'store_panel')

        self.player = player

        # title and money
        self.maker.make_label(300, 25, 90, 20, 'Point Store', 'store_title', store_panel)
        self.money_label = self.maker.make_label(300, 50, 150, 20, 'Points: ', 'store_pmoney', store_panel)

        self.leave_b = self.maker.make_button(300, 330, 150, 160, 'back', None)

        # track selector
        # self.maker.make_label(60, 35, 100, 20, 'Track', 'store_ht', bullet_panel)

        # ----------------------------------------- jet panel ----------------------------------------------------------
        jetpanel = self.maker.make_contained_panel(310, 260, 600, 140, 'jet_panel', store_panel)

        # bullet
        bullet_panel = self.maker.make_contained_panel(300, 30, 600, 70, 'health_panel', jetpanel)

        self.bullet_title = self.maker.make_label(60, 35, 100, 20, 'Bullet ', 'store_ht', bullet_panel)
        self.current_label = self.maker.make_label(250, 35, 200, 20, '', 'store_hcl', bullet_panel)
        self.b_price = self.maker.make_label(430, 35, 100, 20, 'Price: ', 'store_hprice', bullet_panel)

        bullet_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', bullet_panel)

        # stat
        stat_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'damage_panel', jetpanel)

        self.stat_title = self.maker.make_label(60, 35, 100, 20, 'Stats ', 'store_ht', stat_panel)
        self.current_label_stat = self.maker.make_label(250, 35, 200, 20, '', 'store_dcl', stat_panel)
        self.stat_price = self.maker.make_label(430, 35, 100, 20, 'Price: ', 'store_dprice', stat_panel)

        stat_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', stat_panel)

        while runner:

            time_delta = clock.tick(60)

            for event in py.event.get():
                if event.type == py.QUIT:
                    runner = False

                elif event.type == py.KEYDOWN:
                    # ESC
                    if event.key == K_ESCAPE:
                        runner = False

                elif event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:

                        # go back button WHY YOU NO WORK
                        if event.ui_element == self.leave_b:
                            print('exited')
                            runner = False

                        elif event.ui_element == bullet_buy_b:
                            if self.player.player_points >= self.player.point_store[self.selected][0]:
                                self.buy(0)

                        elif event.ui_element == stat_buy_b:
                            if self.player.player_points >= self.player.point_store[self.selected][1]:
                                self.buy(1)

                self.manager.process_events(event)

            self.screen.blit(self.background, (0, 0))

            self.update()

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            py.display.update()

        return self.player

    def buy(self, pos):
        self.player.point_store[self.selected][pos] += 1
        self.player.player_points -= self.player.point_store[self.selected][pos] + 1

    def update(self):

        self.money_label.set_text('Points: ' + str(self.player.player_points))

        strings = [['upgrade size', 'red bullets', 'emp 15%', 'emp 30%', '2x bullets'],
                   ['bps', 'speed', 'bps', 'speed', 'bps']]

        # speed track else damage track
        if self.selected == 0:
            bullet = 'x' + str(self.player.point_store[0][0] + 2)
            self.current_label.set_text(bullet)
            self.current_label_stat.set_text(strings[1][self.player.point_store[0][1]])
        else:
            self.current_label.set_text(strings[0][self.player.point_store[1][0]])
            self.current_label_stat.set_text('damage')

        # bullet
        self.bullet_title.set_text('Bullet ' + str(self.player.point_store[self.selected][0]) + '/5')
        self.b_price.set_text(str('Points: ' + str(self.player.point_store[self.selected][0] + 1)))

        # stat
        self.stat_title.set_text('Stats ' + str(self.player.point_store[self.selected][1]) + '/5')
        self.stat_price.set_text(str('Points: ' + str(self.player.point_store[self.selected][1] + 1)))
