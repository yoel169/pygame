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

    def run(self, player):

        time_delta = 0
        runner = True
        clock = py.time.Clock()

        store_panel = self.maker.make_panel(SW2, SH2, 650, 800, 'store_panel')

        # title and money
        self.maker.make_label(300, 25, 70, 20, 'Store', 'store_title', store_panel)
        money_label = self.maker.make_label(300, 50, 150, 20, 'Money: ' + str(player.money), 'store_pmoney',
                                            store_panel)

        # store values
        script = ['base', 'max', 'life']
        values_hp = [['base', 25], ['max', 100], ['life', 1]]
        values_dam = [['base', 10], ['max', 15]]
        values_speed = [['base', 0.3], ['max', 1]]
        buff_mutipliers = [1, 1.15, 1.25, 1.5, 1.75, 2, 1.5, 2, 4, 8]
        game_multipliers = [1, 1.05, 1.10, 1.20, 1.4, 1.7, 2, 2.5, 3.5, 5]

        self.leave_b = self.maker.make_button(300, 330, 150, 160, 'back', None)

        # ----------------------------------------- jet panel ----------------------------------------------------------
        jetpanel = self.maker.make_contained_panel(310, 210, 600, 210, 'jet_panel', store_panel)
        self.maker.make_label(300, 90, 100, 20, 'Jet Upgrades', 'store_jet', store_panel)

        # health
        health_panel = self.maker.make_contained_panel(300, 30, 600, 70, 'health_panel', jetpanel)
        health_title = self.maker.make_label(60, 10, 100, 20, 'Health ' + str(player.store[1]) + '/10', 'store_ht',
                                             health_panel)
        base_hp = self.maker.make_label(60, 30, 90, 20, 'base: ' + str(player.base_hp), 'store_hb', health_panel)
        max_hp = self.maker.make_label(50, 50, 90, 20, 'max: ' + str(player.maxHealth), 'store_hm', health_panel)
        current_label = self.maker.make_label(250, 35, 200, 20, 'Increase base by 20 ', 'store_hcl', health_panel)
        h_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((player.store[1] + 1) * 30), 'store_hprice',
                                        health_panel)
        health_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', health_panel)

        # damage
        health_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'damage_panel', jetpanel)
        damage_title = self.maker.make_label(60, 10, 100, 20, 'Damage' + str(player.store[2]) + '/10', 'store_ht',
                                             health_panel)
        base_dam = self.maker.make_label(50, 30, 90, 20, 'base: ' + str(player.base_damage), 'store_db', health_panel)
        max_dam = self.maker.make_label(50, 50, 90, 20, 'max: ' + str(player.damage_max), 'store_dm', health_panel)
        current_label_dam = self.maker.make_label(250, 35, 200, 20, 'Increase base by 20 ', 'store_dcl', health_panel)
        dam_price_ = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((player.store[2] + 1) * 30),
                                           'store_dprice',
                                           health_panel)
        damage_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', health_panel)

        # speed
        health_panel = self.maker.make_contained_panel(300, 167, 600, 70, 'speed_panel', jetpanel)
        speed_title = self.maker.make_label(60, 10, 100, 20, 'Speed' + str(player.store[3]) + '/10', 'store_st',
                                            health_panel)
        base_speed = self.maker.make_label(50, 30, 90, 20, 'base: ' + str(player.base_pspeed), 'store_sb', health_panel)
        max_speed = self.maker.make_label(50, 50, 90, 20, 'max: ' + str(player.pspeed_max), 'store_sm', health_panel)
        current_label_speed = self.maker.make_label(250, 35, 200, 20, 'Increase base by 20 ', 'store_scl', health_panel)
        s_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((player.store[3] + 1) * 30), 'store_sprice',
                                        health_panel)
        speed_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', health_panel)

        #  -------------------------------------------- buff panel ----------------------------------------------------
        buffpanel = self.maker.make_contained_panel(310, 430, 600, 150, 'buff_panel', store_panel)
        self.maker.make_label(300, 340, 110, 20, 'Buff Upgrades', 'store_buff', store_panel)

        # offensive buffs
        offensive_panel = self.maker.make_contained_panel(300, 30, 600, 70, 'ob_panel', buffpanel)
        offensive_title = self.maker.make_label(60, 10, 100, 20, 'Offense ' + str(player.store[6]) + '/10', 'store_obt',
                                                offensive_panel)
        dam_buff = self.maker.make_label(50, 30, 90, 20, 'dam: ' + str(5 * player.offensive_buff_multiplier),
                                         'store_obb', offensive_panel)
        bps_buff = self.maker.make_label(50, 50, 90, 20, 'bps: ' + str(300 * player.offensive_buff_multiplier),
                                         'store_obbm', offensive_panel)
        current_label_ob = self.maker.make_label(250, 35, 250, 20, 'Buff multiplier:  ', 'store_obcl',
                                                 offensive_panel)
        ob_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((player.store[6] + 1) * 40), 'store_obprice',
                                         offensive_panel)
        ob_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', offensive_panel)

        # support buffs
        support_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'sp_panel', buffpanel)
        support_title = self.maker.make_label(60, 10, 100, 20, 'Support ' + str(player.store[7]) + '/10', 'store_spbt',
                                              support_panel)
        health_buff = self.maker.make_label(50, 30, 90, 20, 'hp: ' + str(15 * player.offensive_buff_multiplier),
                                            'store_spb', support_panel)
        pspeed_buff = self.maker.make_label(50, 50, 90, 20,
                                            'p speed: ' + str(5 * player.offensive_buff_multiplier),
                                            'store_spbm', support_panel)
        current_label_sp = self.maker.make_label(250, 35, 250, 20, 'Buff multiplier: ', 'store_spcl',
                                                 support_panel)
        sp_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((player.store[7] + 1) * 40), 'store_spprice',
                                         support_panel)
        sp_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', support_panel)

        #  -------------------------------------------- game panel ----------------------------------------------------
        gamepanel = self.maker.make_contained_panel(310, 650, 600, 150, 'game_panel', store_panel)
        self.maker.make_label(300, 550, 110, 20, 'Game Upgrades', 'store_game', store_panel)

        # money
        money_panel = self.maker.make_contained_panel(300, 30, 600, 70, 'mon_panel', gamepanel)
        money_title = self.maker.make_label(60, 10, 100, 20, 'Money ' + str(player.store[4]) + '/10', 'store_mont',
                                            money_panel)
        money_cm = self.maker.make_label(50, 30, 90, 20, 'current: ' + str(player.money_gain_multiplier),
                                         'store_monb', money_panel)

        current_label_mon = self.maker.make_label(250, 35, 250, 20, 'Money multiplier:  ', 'store_moncl',
                                                  money_panel)
        mon_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((player.store[4] + 1) * 50),
                                          'store_monprice',
                                          money_panel)
        mon_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', money_panel)

        # xp
        xp_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'xp_panel', gamepanel)
        xp_title = self.maker.make_label(60, 10, 100, 20, 'XP ' + str(player.store[5]) + '/10', 'store_xpbt',
                                         xp_panel)
        xp_cm = self.maker.make_label(50, 30, 90, 20, 'current: ' + str(player.xp_gain_multiplier),
                                      'store_xpb', xp_panel)
        current_label_xp = self.maker.make_label(250, 35, 250, 20, 'XP multiplier: ', 'store_xpcl',
                                                 xp_panel)
        xp_price = self.maker.make_label(430, 35, 100, 20, 'Price: ' + str((player.store[5] + 1) * 50), 'store_xpprice',
                                         xp_panel)
        xp_buy_b = self.maker.make_button(550, 35, 50, 50, 'Buy', xp_panel)

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
                            runner = False

                self.manager.process_events(event)

            self.screen.blit(self.background, (0, 0))

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            py.display.update()
