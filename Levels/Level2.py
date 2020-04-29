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
from Actors.Neutrals import Cloud, Bullet1, Buff
from Actors.Enemies import EnenmyJet


class Level2:
    def __init__(self, ls):  # width, height, bg, screen, option, option2
        args = ls  # width, height, bg, screen, option, option2
        self.screen = args[3]
        self.background = args[2]
        self.SW = args[0]
        self.SH = args[1]
        self.auto = True  # default auto to on
        self.space = False  # default space shooting to off
        self.mouse = False  # default mouse movement to off

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

        self.player = Player(arrows)

    def run(self):

        # SPRITE GROUPS
        self.bullets = py.sprite.LayeredDirty()
        self.enemies = py.sprite.LayeredDirty()
        self.clouds = py.sprite.LayeredDirty()
        self.buffs = py.sprite.LayeredDirty()
        self.all_sprites = py.sprite.LayeredDirty()

        # Instantiate player.
        self.all_sprites.add(self.player)

        # Initialize pygame
        py.init()

        # create UI manager
        self.manager = gui.UIManager((self.SW, self.SH))

        # time variables
        clock = py.time.Clock()  # time handler for game
        manual_start = 0  # shooting with space time handler if turned on
        auto_start = 0  # auto shooting time handler
        enemy_shoot_start = 0  # enemy bullet handler
        sBooster = 0  # for auto shooting time control
        time_delta = 0  # time handler for manager

        # game variables
        running = True  # game loop
        exit = False  # skipping any other loops and exit game
        score = 0  # player score
        won = False  # if user won
        checker = True  # for spawning buffs
        customMouse = ()  # custom mouse position if movement with mouse is on

        # ========================================== SETTERS ====================================================
        maxWaves = 2
        levelTitle = 'Level 2'

        # ================================== MUTABLE GAME VARIABLES ===============================================
        buffSpawn = 10
        maxScore = 50
        currentWave = 1

        # initialize HUD WITH SCREEN SIZE, BACKGROUND, LEVEL NAME AND # OF WAVES
        hud = HUD(self.screen, self.manager, self.background, levelTitle, maxWaves)

        # Setup for sounds. Defaults are good.
        # py.mixer.init()

        # Load and play background music
        # py.mixer.music.load("Media/game2.mp3")
        # py.mixer.music.set_volume(0.3)
        # py.mixer.music.play(loops=-1)

        # TIMER EVENTS FOR SPAWNING CLOUDS AND ENEMIES
        self.ADDENEMY = py.USEREVENT + 1
        py.time.set_timer(self.ADDENEMY, 1000)
        self.ADDCLOUD = py.USEREVENT + 2
        py.time.set_timer(self.ADDCLOUD, 5000)

        # =================================== WAVE 1 =============================================
        while running:

            # UPDATE MANAGER
            self.manager.update(time_delta)

            # WIN ARGUMENT/ NEXT WAVE
            if score >= maxScore:
                running = False
                print("next level!")

            # LOSE ARGUMENT
            if self.player.lives <= 0:
                won = False
                running = False
                exit = True
                print("you died!")

            # MOUSE SET IF MOVEMENT IS WITH MOUSE
            if self.mouse:
                py.mouse.set_pos(960, 540)

            # ============================== CHECK ALL EVENTS START ====================================
            for event in py.event.get():
                # QUIT EVENT
                if event.type == py.QUIT or event.type == QUIT:
                    running = False
                    won = False
                    exit = True

                # --------------------------------- PRESSED KEY EVENTS --------------------------------
                elif event.type == py.KEYDOWN:

                    # P PAUSE
                    if event.key == K_p:
                        py.mixer.music.pause()
                        hud.pause()
                        py.mixer.music.unpause()

                    # ESC
                    if event.key == K_ESCAPE:
                        running = False
                        won = False
                        exit = True

                    # SPACE IF TURNED ON
                    if event.key == K_SPACE and self.space:
                        manual_timer = py.time.get_ticks() - manual_start
                        if manual_timer >= 600 - sBooster:
                            new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                            self.bullets.add(new_bullet)
                            self.all_sprites.add(new_bullet)
                            manual_start = py.time.get_ticks()

                # -------------------------------- FINISHED CHECKING KEYS ---------------------------------------

                # MOUSE MOTION EVENT IF TURNED ON
                elif event.type == MOUSEMOTION and self.mouse:
                    currentP = py.mouse.get_pos()
                    customMouse = ((currentP[0] - 960) * 0.3, (currentP[1] - 540) * 0.3)
                    self.player.rect.move_ip(customMouse)

                # MOUSE BUTTON EVENT IF TURNED ON
                elif event.type == py.MOUSEBUTTONDOWN and event.button == 1 and self.space is not True and self.auto is not True:
                    manual_timer = py.time.get_ticks() - manual_start
                    if manual_timer >= 600 - sBooster:
                        new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                        self.bullets.add(new_bullet)
                        self.all_sprites.add(new_bullet)
                        manual_start = py.time.get_ticks()

                # ENEMY SPAWN EVENT
                elif event.type == self.ADDENEMY:
                    new_enemy = EnenmyJet(0)
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)

                # CLOUD SPAWN EVENT
                elif event.type == self.ADDCLOUD:
                    # Create the new cloud and add it to sprite groups
                    new_cloud = Cloud()
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)

                # PAUSE BUTTON USER EVENT FROM HUD
                elif event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == hud.pause_button:
                            py.mixer.music.pause()
                            hud.pause()
                            py.mixer.music.unpause()

                # MANAGER PROCESS HUD GUI EVENTS
                self.manager.process_events(event)

            # =================================== EVENT CHECK LOOP FINISHED ============================================

            # SPAWN PLAYER BULLETS IF AUTO SHOOT IS ON
            auto_timer = py.time.get_ticks() - auto_start
            if auto_timer >= 600 - sBooster and self.auto:
                new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                self.bullets.add(new_bullet)
                self.all_sprites.add(new_bullet)
                auto_start = py.time.get_ticks()

            # SPAWNING BUFFS
            if score % buffSpawn == 0 and checker and score != 0:  # spawn a new buff
                num = random.randint(1, 100)
                if num in range(0, 51):
                    type = 0
                elif num in range(50, 76):
                    type = 1
                else:
                    type = 2
                new_buff = Buff(type)
                self.buffs.add(new_buff)
                self.all_sprites.add(new_buff)
                checker = False

            # CLEAR BUFF SPAWN CHECK
            elif score % buffSpawn != 0 and score != 0:
                checker = True

            # ================================== SPRITE COLLISION DETECTION ====================================

            # PLAYER BULLETS AND ENEMY COLLISION
            hits = py.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullet_list in hits.items():
                for bullet in bullet_list:
                    enemy.health -= bullet.damage
                    # self.collision_sound.play()
                    if enemy.health <= 0:
                        score += enemy.points

            # PLAYER AND BUFF COLLISION
            hit = py.sprite.spritecollideany(self.player, self.buffs)
            if hit != None:
                if hit.type == 0:
                    if not self.player.health >= self.player.maxHealth:
                        self.player.health += hit.power
                elif hit.type == 1:
                    self.player.damage += hit.power
                else:
                    if sBooster <= 300:
                        sBooster += hit.power
                print("power up!")
                hit.kill()

            # ENEMY AND PLAYER COLLISION
            hit = py.sprite.spritecollideany(self.player, self.enemies)
            if hit != None:
                self.player.health -= hit.damage
                print("you got hit!")
                hit.kill()

            # ======================================== END COLLISION DETECTION ========================================

            # GET KEYS AND UPDATE PLAYER POSITION
            pressed_keys = py.key.get_pressed()
            self.player.update(pressed_keys)

            # UPDATE REST OF SPRITES POSITIONS
            self.enemies.update()
            self.clouds.update()
            self.bullets.update()
            self.buffs.update()

            # REDRAW BACKGROUND
            self.screen.blit(self.background, (0, 0))

            # DRAW ALL SPRITES
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            # UPDATE HUD AND DRAW IT DONT FORGET TO CHANGE WAVE # AND MAX SCORE
            hud.update(currentWave, score, maxScore, self.player.health, self.player.maxHealth, self.player.lives, self.player.damage,
                       600 - sBooster, self.player.bspeed)
            self.manager.draw_ui(self.screen)

            # UPDATE SCREEN AND TICK CLOCK
            py.display.update()
            clock.tick(60)

        # ========================================= GAME LOOP DONE ==============================================

        if not exit:
            running = True

        # =================================================================================================
        #                                                SECOND WAVE
        # ==================================================================================================

        buffSpawn += 5
        currentWave +=1
        maxScore += 50

        while running:

            # UPDATE MANAGER
            self.manager.update(time_delta)

            # WIN ARGUMENT/ NEXT WAVE
            if score >= maxScore:
                won = True
                running = False
                print("you won!")

            # LOSE ARGUMENT
            if self.player.lives <= 0:
                won = False
                running = False
                exit = True
                print("you died!")

            # MOUSE SET IF MOVEMENT IS WITH MOUSE
            if self.mouse:
                py.mouse.set_pos(960, 540)

            # ============================== CHECK ALL EVENTS START ====================================
            for event in py.event.get():
                # QUIT EVENT
                if event.type == py.QUIT or event.type == QUIT:
                    running = False
                    won = False
                    exit = True

                # --------------------------------- PRESSED KEY EVENTS --------------------------------
                elif event.type == py.KEYDOWN:

                    # P PAUSE
                    if event.key == K_p:
                        py.mixer.music.pause()
                        hud.pause()
                        py.mixer.music.unpause()

                    # ESC
                    if event.key == K_ESCAPE:
                        running = False
                        won = False
                        exit = True

                    # SPACE IF TURNED ON
                    if event.key == K_SPACE and self.space:
                        manual_timer = py.time.get_ticks() - manual_start
                        if manual_timer >= 600 - sBooster:
                            new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                            self.bullets.add(new_bullet)
                            self.all_sprites.add(new_bullet)
                            manual_start = py.time.get_ticks()

                # -------------------------------- FINISHED CHECKING KEYS ---------------------------------------

                # MOUSE MOTION EVENT IF TURNED ON
                elif event.type == MOUSEMOTION and self.mouse:
                    currentP = py.mouse.get_pos()
                    customMouse = ((currentP[0] - 960) * 0.3, (currentP[1] - 540) * 0.3)
                    self.player.rect.move_ip(customMouse)

                # MOUSE BUTTON EVENT IF TURNED ON
                elif event.type == py.MOUSEBUTTONDOWN and event.button == 1 and self.space is not True and self.auto is not True:
                    manual_timer = py.time.get_ticks() - manual_start
                    if manual_timer >= 600 - sBooster:
                        new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                        self.bullets.add(new_bullet)
                        self.all_sprites.add(new_bullet)
                        manual_start = py.time.get_ticks()

                # ENEMY SPAWN EVENT
                elif event.type == self.ADDENEMY:
                    num = random.randint(1, 10)
                    if num in range(1, 8):
                        new_enemy = EnenmyJet(0)
                        self.enemies.add(new_enemy)
                        self.all_sprites.add(new_enemy)
                    else:
                        new_enemy = EnenmyJet(2)
                        self.enemies.add(new_enemy)
                        self.all_sprites.add(new_enemy)

                # CLOUD SPAWN EVENT
                elif event.type == self.ADDCLOUD:
                    # Create the new cloud and add it to sprite groups
                    new_cloud = Cloud()
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)

                # PAUSE BUTTON USER EVENT FROM HUD
                elif event.type == py.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == hud.pause_button:
                            py.mixer.music.pause()
                            hud.pause()
                            py.mixer.music.unpause()

                # MANAGER PROCESS HUD GUI EVENTS
                self.manager.process_events(event)

            # =================================== EVENT CHECK LOOP FINISHED ============================================

            # SPAWN PLAYER BULLETS IF AUTO SHOOT IS ON
            auto_timer = py.time.get_ticks() - auto_start
            if auto_timer >= 600 - sBooster and self.auto:
                new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                self.bullets.add(new_bullet)
                self.all_sprites.add(new_bullet)
                auto_start = py.time.get_ticks()

            # SPAWNING BUFFS UPDATE BOTH NUMBERS
            if score % buffSpawn == 0 and checker and score != 0:  # spawn a new buff
                num = random.randint(1, 100)
                if num in range(0, 51):
                    type = 0
                elif num in range(50, 76):
                    type = 1
                else:
                    type = 2
                new_buff = Buff(type)
                self.buffs.add(new_buff)
                self.all_sprites.add(new_buff)
                checker = False

            # CLEAR BUFF SPAWN CHECK
            elif score % buffSpawn != 0 and score != 0:
                checker = True

            # ================================== SPRITE COLLISION DETECTION ====================================

            # PLAYER BULLETS AND ENEMY COLLISION
            hits = py.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullet_list in hits.items():
                for bullet in bullet_list:
                    enemy.health -= bullet.damage
                    # self.collision_sound.play()
                    if enemy.health <= 0:
                        score += enemy.points

            # PLAYER AND BUFF COLLISION
            hit = py.sprite.spritecollideany(self.player, self.buffs)
            if hit != None:
                if hit.type == 0:
                    if not self.player.health >= self.player.maxHealth:
                        self.player.health += hit.power
                elif hit.type == 1:
                    self.player.damage += hit.power
                else:
                    if sBooster <= 300:
                        sBooster += hit.power
                print("power up!")
                hit.kill()

            # ENEMY AND PLAYER COLLISION
            hit = py.sprite.spritecollideany(self.player, self.enemies)
            if hit != None:
                self.player.health -= hit.damage
                print("you got hit!")
                hit.kill()

            # ======================================== END COLLISION DETECTION ========================================

            # GET KEYS AND UPDATE PLAYER POSITION
            pressed_keys = py.key.get_pressed()
            self.player.update(pressed_keys)

            # UPDATE REST OF SPRITES POSITIONS
            self.enemies.update()
            self.clouds.update()
            self.bullets.update()
            self.buffs.update()

            # REDRAW BACKGROUND
            self.screen.blit(self.background, (0, 0))

            # DRAW ALL SPRITES
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            # UPDATE HUD AND DRAW IT
            hud.update(currentWave, score, maxScore, self.player.health, self.player.maxHealth, self.player.lives, self.player.damage,
                       600 - sBooster, self.player.bspeed)
            self.manager.draw_ui(self.screen)

            # UPDATE SCREEN AND TICK CLOCK
            py.display.update()
            clock.tick(60)

        # ========================================= GAME LOOP DONE ==============================================

        # All done! Stop and quit the mixer.
        #py.mixer.music.stop()
        #py.mixer.quit()

        return won, score
