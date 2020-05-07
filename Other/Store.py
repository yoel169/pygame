import pygame as py
import pygame_gui as gui
from Other.Constants import Constants
from Other.GuiHelper import GuiHelper

SW, SH = Constants.screenSize

SW2 = int(SW / 2)
SH2 = int(SH / 2)


class Store():
    def __init__(self, screen, bg, manager):
        self.screen = screen
        self.manager = manager
        self.screen = screen
        self.background = bg
        self.maker = GuiHelper(SW, SH, self.manager)

    def run(self, player):

        time_delta = 0
        runner = True
        clock = py.time.Clock()

        store_panel = self.maker.make_panel(SW2 - 200, SH2, 610, 610, 'store_panel')

        # title and money
        self.maker.make_label(300, 25, 70, 20, 'Store', 'store_title', store_panel)
        money_label = self.maker.make_label(300, 50, 150, 20, 'Money: ' + str(player.money), 'store_pmoney',
                                            store_panel)

        script = ['base', 'max']
        values_hp = [['base', 25], ['max', 100]]
        values_dam = [['base', 5, 10], ['max', 10, 20]]
        values_speed = [['base', 0.5, 10], ['max', 10, 20]]

        leave_b = self.maker.make_button(300, 330, 150, 160, 'back', None)

        # -----------------------------------------jet --------------------------------------------------------------
        jetpanel = self.maker.make_contained_panel(300, 250, 600, 210, 'jet_panel', store_panel)
        self.maker.make_label(300, 90, 100, 20, 'Jet Upgrades', 'store_jet', store_panel)

        # health
        health_panel = self.maker.make_contained_panel(300, 35, 600, 70, 'health_panel', jetpanel)
        self.maker.make_label(50, 10, 100, 20, 'Health 0/10', 'store_ht', health_panel)
        base_hp = self.maker.make_label(30, 30, 70, 20, 'base: ', 'store_hb', health_panel)
        max_hp = self.maker.make_label(30, 50, 70, 20, 'max: ', 'store_hm', health_panel)
        current_label = self.maker.make_label(200, 35, 200, 20, 'Increase base by 20 ', 'store_hcl', health_panel)
        h_price = self.maker.make_label(400, 35, 100, 20, 'Price: ', 'store_hprice', health_panel)
        self.health_buy_b = self.maker.make_button(520, 35, 50, 50, 'Buy', health_panel)

        # damage
        health_panel = self.maker.make_contained_panel(300, 100, 600, 70, 'damage_panel', jetpanel)
        self.maker.make_label(50, 10, 100, 20, 'Damage 0/10', 'store_ht', health_panel)
        base_dam = self.maker.make_label(30, 30, 70, 20, 'base: ', 'store_db', health_panel)
        max_dam = self.maker.make_label(30, 50, 70, 20, 'max: ', 'store_dm', health_panel)
        current_label_dam = self.maker.make_label(200, 35, 200, 20, 'Increase base by 20 ', 'store_dcl', health_panel)
        dam_price_ = self.maker.make_label(400, 35, 100, 20, 'Price: ', 'store_dprice', health_panel)
        self.damage_buy_b = self.maker.make_button(520, 35, 50, 50, 'Buy', health_panel)

        # speed
        health_panel = self.maker.make_contained_panel(300, 167, 600, 70, 'speed_panel', jetpanel)
        self.maker.make_label(50, 10, 100, 20, 'Speed 0/10', 'store_st', health_panel)
        base_speed = self.maker.make_label(30, 30, 70, 20, 'base: ', 'store_sb', health_panel)
        max_speed = self.maker.make_label(30, 50, 70, 20, 'max: ', 'store_sm', health_panel)
        current_label_speed = self.maker.make_label(200, 35, 200, 20, 'Increase base by 20 ', 'store_scl', health_panel)
        s_price = self.maker.make_label(400, 35, 100, 20, 'Price: ', 'store_sprice', health_panel)
        self.speed_buy_b = self.maker.make_button(520, 35, 50, 50, 'Buy', health_panel)

        while runner:

            time_delta = clock.tick(60)

            for event in py.event.get():
                if event.type == py.QUIT:
                    runner = False

                if event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:

                        # go back button
                        if event.ui_element == leave_b:
                            runner = False

                self.manager.process_events(event)

            self.screen.blit(self.background, (0, 0))

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            py.display.update()
