import pygame_gui as gui
import pygame as py
from Other.HUD import HUD
from pygame.locals import (
    K_p,
    K_SPACE,
    K_ESCAPE,
    QUIT,
    MOUSEMOTION)
import random
from Actors.Players import Player
from Actors.Neutrals import Cloud, Bullet1, HealthBuff, DamageBuff, BulletBuff
from Actors.Enemies import BlueJet, EBullet


class Level1:
    def __init__(self, ls):  # width, height, bg, screen, option, option2
        args = ls
        self.screen = args[3]
        self.SW = args[0]
        self.SH = args[1]
        self.auto = True  # default auto to on
        self.space = False  # default space shooting to off
        self.mouse = False  # default mouse movement to off
        self.background = args[2]

        # shoot auto, with space or with mouse
        if args[4] == 0:
            self.auto = True
        elif args[4] == 1:
            self.space = True
            self.auto = False
        else:
            self.space = False
            self.auto = False

        # move with arrows, wads, or mouse
        arrows = None  # default to None
        if args[5] == 0:
            arrows = True
        elif args[5] == 1:
            arrows = False
        else:
            self.mouse = True

        # Initialize pygame
        py.init()

        self.manager = gui.UIManager((self.SW, self.SH))  # create UI manager

        # Create a custom event for adding a new enemy/clouds
        self.ADDENEMY = py.USEREVENT + 1
        py.time.set_timer(self.ADDENEMY, 500)
        self.ADDCLOUD = py.USEREVENT + 2
        py.time.set_timer(self.ADDCLOUD, 5000)

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        self.player = Player(arrows)
        self.bullets = py.sprite.LayeredDirty()
        self.enemyB = py.sprite.LayeredDirty()
        self.enemies = py.sprite.LayeredDirty()
        self.clouds = py.sprite.LayeredDirty()
        self.buffs = py.sprite.LayeredDirty()
        self.all_sprites = py.sprite.LayeredDirty()

        # Instantiate player.
        self.all_sprites.add(self.player)

    def run(self):

        clock = py.time.Clock()
        manual_start = 0
        auto_start = 0
        enemy_shoot_start = 0

        running = True

        score= 0
        won = False
        checker = True
        sBooster = 0
        customMouse = ()
        time_delta = 0

        hud = HUD(self.screen,self.manager, self.background,'Level 1')

        # Setup for sounds. Defaults are good.
        py.mixer.init()

        # Load and play background music
        #py.mixer.music.load("Media/game2.mp3")
        #py.mixer.music.set_volume(0.3)
        #py.mixer.music.play(loops=-1)

        while running:

            time_delta = clock.tick(60) / 1000.0

            if self.mouse:  # if user is moving with mouse
                py.mouse.set_pos(960, 540)  # always center mouse

            # for loop through the event queue
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

                if event.type == py.KEYDOWN:
                    if event.key == K_p:
                        py.mixer.music.pause()
                        hud.pause()
                        py.mixer.music.unpause()

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_SPACE and self.space:
                        manual_timer = py.time.get_ticks() - manual_start
                        if manual_timer >= 600 - sBooster:
                            new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                            self.bullets.add(new_bullet)
                            self.all_sprites.add(new_bullet)
                            manual_start = py.time.get_ticks()

                if event.type == MOUSEMOTION and self.mouse:
                    currentP = py.mouse.get_pos()
                    customMouse = ((currentP[0] - 960) * 0.3, (currentP[1] - 540)*0.3)
                    self.player.rect.move_ip(customMouse)

                if event.type == py.MOUSEBUTTONDOWN and event.button == 1 and self.space is not True and self.auto is not True:
                    manual_timer = py.time.get_ticks() - manual_start
                    if manual_timer >= 600 - sBooster:
                        new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                        self.bullets.add(new_bullet)
                        self.all_sprites.add(new_bullet)
                        manual_start = py.time.get_ticks()

                # Check for QUIT event. If QUIT, then set running to false.
                if event.type == QUIT:
                    running = False
                    won = False

                if event.type == self.ADDENEMY:
                    new_enemy = BlueJet()
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)

                # Add a new cloud?
                if event.type == self.ADDCLOUD:
                    # Create the new cloud and add it to sprite groups
                    new_cloud = Cloud()
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)

                if event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == hud.pause_button:
                            py.mixer.music.pause()
                            hud.pause()
                            py.mixer.music.unpause()

                self.manager.process_events(event)

            auto_timer = py.time.get_ticks() - auto_start

            # auto shoot mechanics
            if auto_timer >= 600 - sBooster and self.auto:
                new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed + 5)
                self.bullets.add(new_bullet)
                self.all_sprites.add(new_bullet)
                auto_start = py.time.get_ticks()

            # enemy and bullets colliding
            hits = py.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullet_list in hits.items():
                for bullet in bullet_list:
                    enemy.health -= bullet.damage
                    # self.collision_sound.play()
                    if enemy.health <= 0:
                        score += 1

            if score % 5 == 0 and checker and score != 0:  # spawn a new buff
                num = random.randint(1, 100)
                if num in range(0, 51):
                    new_buff = HealthBuff()
                elif num in range(50, 76):
                    new_buff = DamageBuff()
                else:
                    new_buff = BulletBuff()
                self.buffs.add(new_buff)
                self.all_sprites.add(new_buff)
                checker = False

            elif score % 5 != 0 and score != 0:  # clear spawn queue
                checker = True

            if score >= 50:  # won
                running = False
                won = True

            # Check if any enemies have collided with the player
            hit = py.sprite.spritecollideany(self.player, self.enemies)
            if hit != None:
                self.player.health -= hit.damage
                print("you got hit!")
                hit.kill()

            # collide with power up
            hit = py.sprite.spritecollideany(self.player, self.buffs)
            if hit != None:
                if hit.__class__ == HealthBuff:
                    if not self.player.health >= self.player.maxHealth:
                        self.player.health += hit.power
                elif hit.__class__ == DamageBuff:
                    self.player.damage += hit.power
                else:
                    if sBooster <= 300:
                        sBooster += hit.power
                print("power up!")
                hit.kill()

            # check player still has lives
            if self.player.lives <= 0:
                won = False
                running = False
                print("you died!")

            self.screen.blit(self.background, (0, 0))

            # Get the set of keys pressed and check for user input
            pressed_keys = py.key.get_pressed()

            # Update the player sprite based on user keypresses
            self.player.update(pressed_keys)

            # Update positions
            self.enemies.update()
            self.enemyB.update()
            self.clouds.update()
            self.bullets.update()
            self.buffs.update()

            # Draw all sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            hud.update(1,1,score,50,self.player.health,self.player.maxHealth,self.player.lives,self.player.damage,
                       int(self.player.damage / (0.6 - (sBooster / 1000))),self.player.bspeed)

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            py.display.update()

        # All done! Stop and quit the mixer.
        #py.mixer.music.stop()
        #py.mixer.quit()

        py.mouse.set_visible(True)

        return won, score