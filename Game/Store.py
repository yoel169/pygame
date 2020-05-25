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

    def run(self, player):

        time_delta = 0
        runner = True
        clock = py.time.Clock()

        store_panel = self.maker.make_panel(SW2, SH2, 650, 800, 'store_panel')

        self.player = player

        # title and money
        self.maker.make_label(300, 25, 70, 20, 'Store', 'store_title', store_panel)
        self.money_label = self.maker.make_label(300, 50, 150, 20, 'Money: ' + str(self.player.money),
                                                 'store_pmoney',
                                                 store_panel)

        # store values
        buff_mutipliers = [1.15, 1.25, 1.5, 1.75, 2, 1.5, 2, 4, 8]
        game_multipliers = [1.05, 1.10, 1.20, 1.4, 1.7, 2, 2.5, 3.5, 5]

        self.leave_b = self.maker.make_button(300, 330, 150, 160, 'back', None)

        # ----------------------------------------- jet panel ----------------------------------------------------------
        jetpanel = self.maker.make_contained_panel(310, 210, 600, 210, 'jet_panel', store_panel)
        self.maker.make_label(300, 90, 100, 20, 'Jet Upgrades', 'store_jet', store_panel)

        # health
        health_panel = self.maker.make_contained_panel(300, 30, 600, 70, 'health_panel', jetpanel)
        self.health_title = self.maker.make_label(60, 10, 100, 20, 'Health ' + str(self.player.store[1]) + '/10',
                                                  'store_ht',
                                                  health_panel)
        self.base_hp = self.maker.make_label(60, 30, 90, 20, 'base: ' + str(self.player.base_hp), 'store_hb',
                                             health_panel)
        self.max_hp = self.maker.make_label(50, 50, 90, 20, 'max: ' + str(self.player.maxHealth), 'store_hm',
                                            health_panel)
        self.current_label = self.maker.make_label(250, 35, 200, 20, self.get_string(1), 'store_hcl',
                                                   health_panel)
        self.h_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((self.player.store[1] + 1) * 30),
                                             'store_hprice',
                                             health_panel)
        health_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', health_panel)

        # damage
        health_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'damage_panel', jetpanel)
        self.damage_title = self.maker.make_label(60, 10, 100, 20, 'Damage' + str(self.player.store[2]) + '/10',
                                                  'store_ht',
                                                  health_panel)
        self.base_dam = self.maker.make_label(50, 30, 90, 20, 'base: ' + str(self.player.base_damage), 'store_db',
                                              health_panel)
        self.max_dam = self.maker.make_label(50, 50, 90, 20, 'max: ' + str(self.player.damage_max), 'store_dm',
                                             health_panel)
        self.current_label_dam = self.maker.make_label(250, 35, 200, 20, self.get_string(2), 'store_dcl',
                                                       health_panel)
        self.dam_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((self.player.store[2] + 1) * 30),
                                               'store_dprice', health_panel)
        damage_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', health_panel)

        # speed
        health_panel = self.maker.make_contained_panel(300, 167, 600, 70, 'speed_panel', jetpanel)
        self.speed_title = self.maker.make_label(60, 10, 100, 20, 'Speed' + str(self.player.store[3]) + '/10',
                                                 'store_st',
                                                 health_panel)
        self.base_speed = self.maker.make_label(50, 30, 90, 20, 'base: ' + str(self.player.base_pspeed), 'store_sb',
                                                health_panel)
        self.max_speed = self.maker.make_label(50, 50, 90, 20, 'max: ' + str(self.player.pspeed_max), 'store_sm',
                                               health_panel)
        self.current_label_speed = self.maker.make_label(250, 35, 200, 20, self.get_string(3), 'store_scl',
                                                         health_panel)
        self.s_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((self.player.store[3] + 1) * 30),
                                             'store_sprice',
                                             health_panel)
        speed_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', health_panel)

        #  -------------------------------------------- buff panel ----------------------------------------------------
        buffpanel = self.maker.make_contained_panel(310, 430, 600, 150, 'buff_panel', store_panel)
        self.maker.make_label(300, 340, 110, 20, 'Buff Upgrades', 'store_buff', store_panel)

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
        gamepanel = self.maker.make_contained_panel(310, 650, 600, 150, 'game_panel', store_panel)
        self.maker.make_label(300, 550, 120, 20, 'Game Upgrades', 'store_game', store_panel)

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

                        # go back button WHY YOU NO WORK
                        if event.ui_element == self.leave_b:
                            print('exited')
                            runner = False

                        elif event.ui_element == health_buy_b:
                            if self.player.money >= (self.player.store[1] + 1) * 30:
                                self.buy(1)

                        elif event.ui_element == damage_buy_b:
                            if self.player.money >= (self.player.store[2] + 1) * 30:
                                self.buy(2)

                        elif event.ui_element == speed_buy_b:
                            if self.player.money >= (self.player.store[3] + 1) * 30:
                                self.buy(3)

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

                self.manager.process_events(event)

            self.screen.blit(self.background, (0, 0))

            self.update()

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)
            self.mon_price.rebuild()

            py.display.update()

        return self.player

    def get_string(self, pos):

        values_hp = [['base', 25], ['max', 100], ['life', 1]]
        values_dam = [['base', 10], ['max', 15]]
        values_speed = [['base', 0.3], ['max', 1]]
        hp_track = [1, 0, 0, 2, 0, 0, 1, 0, 0, 2]
        track = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

        if pos == 1:
            return ('increase: %s by %.1f' % (values_hp[hp_track[self.player.store[1]]][0],
                                                     values_hp[hp_track[self.player.store[1]]][1]))
        elif pos == 2:
            return 'increase: %s %.1f' % (values_dam[hp_track[self.player.store[2]]][0],
                                                     values_dam[track[self.player.store[2]]][1])
        else:
            return 'increase: %s by %.1f' % (values_speed[hp_track[self.player.store[3]]][0],
                                                     values_speed[track[self.player.store[3]]][1])

    def update(self):
        buff_mutipliers = [1.15, 1.25, 1.5, 1.75, 2, 1.5, 2, 4, 8]
        game_multipliers = [1.05, 1.10, 1.20, 1.4, 1.7, 2, 2.5, 3.5, 5]
        self.money_label.set_text('Money: %.3f' % self.player.money)

        self.health_title.set_text('Health %d/10' % self.player.store[1])
        self.base_hp.set_text('base: ' + str(self.player.base_hp))
        self.max_hp.set_text('max: ' + str(self.player.maxHealth))
        self.current_label.set_text(self.get_string(1))
        self.h_price.set_text('Price: ' + str((self.player.store[1] + 1) * 30))

        self.damage_title.set_text('Damage ' + str(self.player.store[2]) + '/10')
        self.base_dam.set_text('base: ' + str(self.player.base_damage))
        self.max_dam.set_text('max: ' + str(self.player.damage_max))
        self.current_label_dam.set_text(self.get_string(2))
        self.dam_price.set_text('Price: ' + str((self.player.store[2] + 1) * 30))

        self.speed_title.set_text('Speed ' + str(self.player.store[3]) + '/10')
        self.base_speed.set_text('base: %.1f' % self.player.base_pspeed)
        self.max_speed.set_text('max: ' + str(self.player.pspeed_max))
        self.current_label_speed.set_text(self.get_string(3))
        self.s_price.set_text('Price: ' + str((self.player.store[3] + 1) * 30))

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

        if pos in range(1, 4):

            values_hp = [['base', 25], ['max', 100], ['life', 1]]
            values_dam = [['base', 10], ['max', 15]]
            values_speed = [['base', 0.3], ['max', 1]]

            hp_track = [1, 0, 0, 2, 0, 0, 1, 0, 0, 2]
            track = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

            self.player.money -= (self.player.store[pos] + 1) * 30

            if pos == 1:
                if values_hp[hp_track[self.player.store[1]]][0] == 'base':
                    self.player.base_hp += values_hp[hp_track[self.player.store[1]]][1]
                elif values_hp[hp_track[self.player.store[1]]][0] == 'max':
                    self.player.maxHealth += values_hp[hp_track[self.player.store[1]]][1]
                else:
                    self.player.maxHealth += values_hp[hp_track[self.player.store[1]]][1]

            elif pos == 2:
                if values_dam[track[self.player.store[2]]][0] == 'base':
                    self.player.base_damage += values_dam[track[self.player.store[2]]][1]
                else:
                    self.player.damage_max += values_dam[track[self.player.store[2]]][1]

            else:
                if values_speed[track[self.player.store[3]]][0] == 'base':
                    self.player.base_pspeed += values_speed[track[self.player.store[3]]][1]
                else:
                    self.player.pspeed_max += values_speed[track[self.player.store[3]]][1]

        elif pos in range(4, 6):

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
