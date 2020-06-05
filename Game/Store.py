import pygame as py
import pygame_gui as gui
from Other.Constants import Constants
from Other.GuiHelper import GuiHelper
from pygame.locals import (
    K_ESCAPE)

SW, SH = Constants.screenSize

SW2 = int(SW / 2)
SH2 = int(SH / 2)


# ============================================== LEEROYYYYYYYYYYYYYYYYYYYY JENKINSSSSSSSSSSSSSSSSSSSS ==================
class Store:
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
        self.reset_track = None

    def run(self, player):

        time_delta = 0
        runner = True
        clock = py.time.Clock()

        store_panel = self.maker.make_panel(SW2, SH2, 650, 800, 'store_panel')

        self.player = player
        self.selected = player.current_track

        # title and money
        self.maker.make_label(300, 25, 70, 20, 'Store', 'store_title', store_panel)

        self.money_label = self.maker.make_label(150, 50, 150, 20, 'Money: ' + str(self.player.money),
                                                 'store_pmoney',
                                                 store_panel)
        self.point_label = self.maker.make_label(400, 50, 150, 20, 'Points: ' + str(self.player.player_points),
                                                 'store_pmoney',
                                                 store_panel)

        # store values
        buff_mutipliers = [1.15, 1.25, 1.5, 1.75, 2, 1.5, 2, 4, 8]
        game_multipliers = [1.05, 1.10, 1.20, 1.4, 1.7, 2, 2.5, 3.5, 5]

        self.leave_b = self.maker.make_button(300, 800, 100, 60, 'back', None)

        # ----------------------------------------- jet panel ----------------------------------------------------------
        string = []
        if self.player.current_track == 0:
            string = ['speed', 'damage']
        else:
            string = ['damage', 'speed']

        self.track_selector = self.maker.make_contained_drop_down_menu(100, 295, 100, 40, 'pick_ddm',
                                                                       string, store_panel)

        self.reset_track = self.maker.make_button(500, 295, 120, 40, 'reset track', store_panel)

        self.jet_title = self.maker.make_label(300, 110, 220, 20,
                                               'Jet Upgrades: ' + self.track_selector.selected_option + ' track',
                                               'store_buff', store_panel)
        jetpanel = self.maker.make_contained_panel(310, 200, 600, 140, 'jet_panel', store_panel)

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

        #  -------------------------------------------- buff panel ----------------------------------------------------
        self.maker.make_label(300, 340, 110, 20, 'Buff Upgrades', 'store_buff', store_panel)
        buffpanel = self.maker.make_contained_panel(310, 430, 600, 140, 'buff_panel', store_panel)

        # offensive buffs
        offensive_panel = self.maker.make_contained_panel(300, 30, 600, 70, 'ob_panel', buffpanel)
        self.offensive_title = self.maker.make_label(60, 10, 100, 20, 'Offense ' + str(self.player.store[4]) + '/10',
                                                     'store_obt',
                                                     offensive_panel)
        self.dam_buff = self.maker.make_label(50, 30, 90, 20, 'dam: ' + str(5 * self.player.offensive_buff_multiplier),
                                              'store_obb', offensive_panel)
        self.bps_buff = self.maker.make_label(50, 50, 90, 20,
                                              'bps: ' + str(300 * self.player.offensive_buff_multiplier),
                                              'store_obbm', offensive_panel)
        self.current_label_ob = self.maker.make_label(250, 35, 250, 20,
                                                      'increase to ' + str(buff_mutipliers[self.player.store[4]]) + '%',
                                                      'store_obcl',
                                                      offensive_panel)
        self.ob_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((self.player.store[4] + 1) * 40),
                                              'store_obprice',
                                              offensive_panel)
        ob_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', offensive_panel)

        # support buffs
        support_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'sp_panel', buffpanel)
        self.support_title = self.maker.make_label(60, 10, 100, 20, 'Support ' + str(self.player.store[5]) + '/10',
                                                   'store_spbt',
                                                   support_panel)
        self.health_buff = self.maker.make_label(50, 30, 90, 20,
                                                 'hp: ' + str(15 * self.player.offensive_buff_multiplier),
                                                 'store_spb', support_panel)
        self.pspeed_buff = self.maker.make_label(60, 50, 110, 20,
                                                 'p speed: ' + str(5 * self.player.offensive_buff_multiplier),
                                                 'store_spbm', support_panel)
        self.current_label_sp = self.maker.make_label(250, 35, 250, 20,
                                                      'increase to:  ' + str(
                                                          buff_mutipliers[self.player.store[5]]) + '%',
                                                      'store_spcl',
                                                      support_panel)
        self.sp_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((self.player.store[5] + 1) * 40),
                                              'store_spprice',
                                              support_panel)
        sp_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', support_panel)

        #  -------------------------------------------- game panel ----------------------------------------------------
        self.maker.make_label(300, 550, 120, 20, 'Game Upgrades', 'store_game', store_panel)
        gamepanel = self.maker.make_contained_panel(310, 640, 600, 140, 'game_panel', store_panel)

        # money
        money_panel = self.maker.make_contained_panel(300, 30, 600, 70, 'mon_panel', gamepanel)
        self.money_title = self.maker.make_label(60, 10, 100, 20, 'Money ' + str(self.player.store[6]) + '/10',
                                                 'store_mont',
                                                 money_panel)
        self.money_cm = self.maker.make_label(50, 30, 90, 20, 'current: ' + str(self.player.money_gain_multiplier),
                                              'store_monb', money_panel)

        self.current_label_mon = self.maker.make_label(250, 35, 250, 20,
                                                       'increase to:  ' + str(
                                                           game_multipliers[self.player.store[6]]) + '%',
                                                       'store_moncl',
                                                       money_panel)
        self.mon_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((self.player.store[6] + 1) * 50),
                                               'store_monprice',
                                               money_panel)
        mon_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', money_panel)

        # xp
        xp_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'xp_panel', gamepanel)
        self.xp_title = self.maker.make_label(60, 10, 100, 20, 'XP ' + str(self.player.store[7]) + '/10', 'store_xpbt',
                                              xp_panel)
        self.xp_cm = self.maker.make_label(50, 30, 90, 20, 'current: ' + str(self.player.xp_gain_multiplier),
                                           'store_xpb', xp_panel)
        self.current_label_xp = self.maker.make_label(250, 35, 250, 20,
                                                      'increase to:  ' + str(
                                                          game_multipliers[self.player.store[7]]) + '%',
                                                      'store_xpcl',
                                                      xp_panel)
        self.xp_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((self.player.store[7] + 1) * 50),
                                              'store_xpprice',
                                              xp_panel)
        xp_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', xp_panel)

        # self.player.money = 1000

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

                        # go back button
                        if event.ui_element == self.leave_b:
                            print('exited')
                            runner = False

                        elif event.ui_element == ob_buy_b:
                            if self.player.money >= (self.player.store[4] + 1) * 40:
                                self.buy(4)

                        elif event.ui_element == sp_buy_b:
                            if self.player.money >= (self.player.store[5] + 1) * 40:
                                self.buy(5)

                        elif event.ui_element == xp_buy_b:
                            if self.player.money >= (self.player.store[7] + 1) * 50:
                                self.buy(7)

                        elif event.ui_element == mon_buy_b:
                            if self.player.money >= (self.player.store[6] + 1) * 50:
                                self.buy(6)

                        elif event.ui_element == bullet_buy_b:
                            if self.player.player_points >= self.player.point_store[self.selected][0] + 1:
                                self.buy(0)

                        elif event.ui_element == stat_buy_b:
                            if self.player.player_points >= self.player.point_store[self.selected][1] + 1:
                                self.buy(1)

                        elif event.ui_element == self.reset_track:
                            self.player.player_points += self.player.point_store[self.selected][2]
                            self.player.point_store[self.selected] = [0, 0, 0]
                            self.player.set_track()
                            print('reset ' + self.track_selector.selected_option + ' track')

                self.manager.process_events(event)

            self.screen.blit(self.background, (0, 0))

            self.update()

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            py.display.update()

        return self.player

    def update(self):
        buff_mutipliers = [1.15, 1.25, 1.5, 1.75, 2, 1.5, 2, 4, 8]
        game_multipliers = [1.05, 1.10, 1.20, 1.4, 1.7, 2, 2.5, 3.5, 5]

        self.money_label.set_text('Points: ' + str(self.player.player_points))

        strings = [['upgrade size', 'red bullets', 'emp 15%', 'emp 30%', '2x bullets'],
                   ['bps', 'speed', 'bps', 'speed', 'bps']]

        # speed track else damage track
        if self.track_selector.selected_option == 'speed':
            self.selected = 0
            self.player.current_track = 0
            self.player.set_track()
            bullet = 'x' + str(self.player.point_store[0][0] + 2)
            self.current_label.set_text(bullet)
            self.current_label_stat.set_text(strings[1][self.player.point_store[0][1]])
        else:
            self.selected = 1
            self.player.current_track = 1
            self.player.set_track()
            self.current_label.set_text(strings[0][self.player.point_store[1][0]])
            self.current_label_stat.set_text('damage')

        self.jet_title.set_text('Jet Upgrades: ' + self.track_selector.selected_option + ' track')

        # bullet
        self.bullet_title.set_text('Bullet ' + str(self.player.point_store[self.selected][0]) + '/5')
        self.b_price.set_text(str('Points: ' + str(self.player.point_store[self.selected][0] + 1)))

        # stat
        self.stat_title.set_text('Stats ' + str(self.player.point_store[self.selected][1]) + '/5')
        self.stat_price.set_text(str('Points: ' + str(self.player.point_store[self.selected][1] + 1)))

        self.money_label.set_text('Money: %.3f' % self.player.money)

        self.offensive_title.set_text('Offense ' + str(self.player.store[4]) + '/10')
        self.dam_buff.set_text('dam: %.2f' % 5 * self.player.offensive_buff_multiplier)
        self.bps_buff.set_text('bps: %.2f' % 300 * self.player.offensive_buff_multiplier)
        self.current_label_ob.set_text('increase to: %.2f%s' % (buff_mutipliers[self.player.store[4]], '%'))
        self.ob_price.set_text('Price: ' + str((self.player.store[4] + 1) * 40))

        self.support_title.set_text('Support ' + str(self.player.store[5]) + '/10')
        self.health_buff.set_text('hp: %.2f' % 15 * self.player.offensive_buff_multiplier)
        self.pspeed_buff.set_text('p speed: %.2f' % 5 * self.player.offensive_buff_multiplier)
        self.current_label_sp.set_text('increase to: %.2f%s' % (buff_mutipliers[self.player.store[5]], '%'))
        self.sp_price.set_text('Price: ' + str((self.player.store[5] + 1) * 40))

        self.money_title.set_text('Money ' + str(self.player.store[6]) + '/10')
        self.money_cm.set_text('current: %.2f' % self.player.money_gain_multiplier)
        self.current_label_mon.set_text('increase to: %.2f%s' % (game_multipliers[self.player.store[6]], '%'))
        self.mon_price.set_text('Price: ' + str((self.player.store[6] + 1) * 50))

        self.xp_title.set_text('XP ' + str(self.player.store[7]) + '/10')
        self.xp_cm.set_text('current: ' + str(self.player.xp_gain_multiplier))
        self.current_label_xp.set_text('increase to: %.2f%s' % (game_multipliers[self.player.store[7]], '%'))
        self.xp_price.set_text('Price: ' + str((self.player.store[7] + 1) * 50))

    def buy(self, pos):

        if pos in range(0, 2):
            self.player.point_store[self.selected][pos] += 1
            self.player.player_points -= self.player.point_store[self.selected][pos] + 1
            self.player.point_store[self.selected][2] += self.player.point_store[self.selected][pos] + 1
            self.player.set_track()

        else:
            if pos in range(4, 6):

                buff_mutipliers = [1.15, 1.25, 1.5, 1.75, 2, 1.5, 2, 4, 8]

                self.player.money -= (self.player.store[pos] + 1) * 40

                if pos == 4:
                    self.player.offensive_buff_multiplier = buff_mutipliers[self.player.store[pos]]
                else:
                    self.player.support_buff_multiplier = buff_mutipliers[self.player.store[pos]]

            else:

                game_multipliers = [1.05, 1.10, 1.20, 1.4, 1.7, 2, 2.5, 3.5, 5]

                self.player.money -= (self.player.store[pos] + 1) * 50

                if pos == 6:
                    self.player.money_gain_multiplier = game_multipliers[self.player.store[pos]]
                else:
                    self.player.xp_gain_multiplier = game_multipliers[self.player.store[pos]]

            self.player.store[pos] += 1
            print(str(pos))
