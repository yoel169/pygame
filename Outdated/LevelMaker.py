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
from Actors.Enemies import EnenemyJet, EBullet

# ================================================ OUTED LEVEL MAKER ==================================================


class LevelMaker:
    def __init__(self, ls):
        args = ls  # width, height, bg, screen
        self.screen = args[3]
        self.background = args[2]
        self.SW = args[0]
        self.SH = args[1]

    def makeStage(self, args, args2):

        # INIT TIME VARIABLES
        clock = py.time.Clock()  # time handler for game
        manual_start = 0  # shooting with space time handler if turned on
        auto_start = 0  # auto shooting time handler
        sBooster = 0  # for auto shooting time control
        time_delta = 0  # time handler for manager

        # INIT GAME VARIABLES
        running = True  # game loop
        score = 0  # player score
        won = False  # if user won
        checker = True  # for spawning buffs
        customMouse = ()  # custom mouse position if movement with mouse is on
        exit = False  # exit game
        auto = True  # default auto to on
        space = False  # default space shooting to off
        mouse = False  # default mouse movement to off
        currentWave = 1  # wave number to loop through
        counter = 0  # counter for looping through arguments

        # ================================= INIT GAME ARGUMENTS THAT WERE PASSED =====================================

        option = args # SHOOTING AND MOVEMENT
        levelTitle, maxWaves, buffSpawn, maxScore, eTypes, enemyTimers = args2  # GAME ARGUMENTS

        # ======================================== SHOOTING AND MOVEMENT SETUP =======================================
        # shoot auto, with space or with mouse
        if option[0] == 0:
            auto = True
        elif option[0] == 1:
            space = True
            auto = False
        else:
            space = False
            auto = False

        # move with arrows, wads, or mouse
        arrows = None  # default to None
        if option[1] == 0:
            arrows = True
        elif option[1] == 1:
            arrows = False
        else:
            mouse = True
        # ===================================== END SHOOTING AND MOVEMENT SETUP ===================================

        # CREATE PLAYER
        player = Player(arrows)

        # SPRITE GROUPS
        clouds = py.sprite.LayeredDirty()
        bullets = py.sprite.LayeredDirty()
        enemies = py.sprite.LayeredDirty()
        buffs = py.sprite.LayeredDirty()
        all_sprites = py.sprite.LayeredDirty()

        # ADD PLAYER IN ALL SPRITES GROUP
        all_sprites.add(player)

        # INITIALIZE GAME
        py.init()

        # CREATE GUI MANAGER
        manager = gui.UIManager((self.SW, self.SH))

        # INIT  HUD WITH SCREEN SIZE, BACKGROUND, LEVEL NAME AND # OF WAVES
        hud = HUD(self.screen, manager, self.background, levelTitle, maxWaves)

        # TIMER EVENTS FOR SPAWNING CLOUDS AND ENEMIES
        ADDCLOUD = py.USEREVENT + 1
        ADDENEMY = py.USEREVENT + 2
        py.time.set_timer(ADDCLOUD, 5000)

        while not exit:

            # CHANGE ENEMY TIMER BASED ON ARGUMENT
            py.time.set_timer(ADDENEMY, enemyTimers[counter])

            while running:

                # UPDATE MANAGER
                manager.update(time_delta)

                # WIN BASED ON LAST ARGUMENT
                if score >= maxScore[maxWaves - 1]:
                    won = True
                    exit = True
                    running = False
                    print("you won!")

                # ELSE NEXT WAVE
                elif score >= maxScore[counter]:
                    running = False
                    print("next wave!")

                # LOSE ARGUMENT
                if player.lives <= 0:
                    won = False
                    running = False
                    exit = True
                    print("you died!")

                # MOUSE SET IF MOVEMENT IS WITH MOUSE
                if mouse:
                    py.mouse.set_pos(960, 540)

                # ============================== EVENTS CHECK START ====================================
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
                        if event.key == K_SPACE and space:
                            manual_timer = py.time.get_ticks() - manual_start
                            if manual_timer >= 600 - sBooster:
                                new_bullet = Bullet1(player.rect.center, player.damage, player.bspeed)
                                bullets.add(new_bullet)
                                all_sprites.add(new_bullet)
                                manual_start = py.time.get_ticks()

                    # -------------------------------- FINISHED CHECKING KEYS ---------------------------------------

                    # MOUSE MOTION EVENT IF TURNED ON
                    elif event.type == MOUSEMOTION and mouse:
                        currentP = py.mouse.get_pos()
                        customMouse = ((currentP[0] - 960) * 0.3, (currentP[1] - 540) * 0.3)
                        player.rect.move_ip(customMouse)

                    # MOUSE BUTTON EVENT IF TURNED ON
                    elif event.type == py.MOUSEBUTTONDOWN and event.button == 1 and space is not True and \
                            auto is not True:
                        manual_timer = py.time.get_ticks() - manual_start
                        if manual_timer >= 600 - sBooster:
                            new_bullet = Bullet1(player.rect.center, player.damage, player.bspeed)
                            bullets.add(new_bullet)
                            all_sprites.add(new_bullet)
                            manual_start = py.time.get_ticks()

                    # ENEMY SPAWN EVENT
                    elif event.type == ADDENEMY:
                        new_enemy = EnenemyJet(eTypes[counter])
                        enemies.add(new_enemy)
                        all_sprites.add(new_enemy)

                    # CLOUD SPAWN EVENT
                    elif event.type == ADDCLOUD:
                        # Create the new cloud and add it to sprite groups
                        new_cloud = Cloud()
                        clouds.add(new_cloud)
                        all_sprites.add(new_cloud)

                    # PAUSE BUTTON USER EVENT FROM HUD
                    elif event.type == py.USEREVENT:
                        if event.user_type == gui.UI_BUTTON_PRESSED:
                            if event.ui_element == hud.pause_button:
                                py.mixer.music.pause()
                                hud.pause()
                                py.mixer.music.unpause()

                    # MANAGER PROCESS HUD GUI EVENTS
                    manager.process_events(event)

                # =================================== END EVENT CHECK ===========================================

                # SPAWN PLAYER BULLETS IF AUTO SHOOT IS ON
                auto_timer = py.time.get_ticks() - auto_start
                if auto_timer >= 600 - sBooster and auto:
                    new_bullet = Bullet1(player.rect.center, player.damage, player.bspeed)
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)
                    auto_start = py.time.get_ticks()

                # SPAWNING ENEMY BULLETS
                for enemy in enemies:
                    if random.randint(0,100) == 0:
                        if enemy.type == 1:
                            new_bullet = EBullet(enemy.rect.center, enemy.damage, enemy.pspeed + 5)
                            bullets.add(new_bullet)
                            all_sprites.add(new_bullet)

                # SPAWNING BUFFS
                if score % buffSpawn[counter] == 0 and checker and score != 0:  # spawn a new buff
                    num = random.randint(1, 100)
                    if num in range(0, 51):
                        type = 0
                    elif num in range(50, 76):
                        type = 1
                    else:
                        type = 2
                    new_buff = Buff(type)
                    buffs.add(new_buff)
                    all_sprites.add(new_buff)
                    checker = False

                # CLEAR BUFF SPAWN CHECK
                elif score % buffSpawn[counter] != 0 and score != 0:
                    checker = True

                # ================================== SPRITE COLLISION DETECTION ====================================

                # PLAYER BULLETS AND ENEMY COLLISION
                hits = py.sprite.groupcollide(enemies, bullets, False, False)
                for enemy, bullet_list in hits.items():
                    for bullet in bullet_list:
                        if bullet.__class__ == Bullet1:
                            enemy.health -= bullet.damage
                            # self.collision_sound.play()
                            bullet.kill()
                            if enemy.health <= 0:
                                score += enemy.points

                # PLAYER AND ENEMY BULLET
                hit = py.sprite.spritecollideany(player, bullets)
                if hit.__class__ == EBullet and hit != None:
                    player.health -= hit.damage
                    print("you got hit by enemy bullet!")
                    hit.kill()

                # PLAYER AND BUFF COLLISION
                hit = py.sprite.spritecollideany(player, buffs)
                if hit != None:
                    if hit.type == 0:
                        if not player.health >= player.maxHealth:
                            player.health += hit.power
                    elif hit.type == 1:
                        player.damage += hit.power
                    else:
                        if sBooster <= 300:
                            sBooster += hit.power
                    print("power up!")
                    hit.kill()

                # ENEMY AND PLAYER COLLISION
                hit = py.sprite.spritecollideany(player, enemies)
                if hit != None:
                    player.health -= hit.damage
                    print("you got hit!")
                    hit.kill()

                # ======================================== END COLLISION DETECTION =================================

                # GET KEYS AND UPDATE PLAYER POSITION
                pressed_keys = py.key.get_pressed()
                player.update(pressed_keys)

                # UPDATE REST OF SPRITES POSITIONS
                enemies.update()
                clouds.update()
                bullets.update()
                buffs.update()

                # REDRAW BACKGROUND
                self.screen.blit(self.background, (0, 0))

                # DRAW ALL SPRITES
                for entity in all_sprites:
                    self.screen.blit(entity.surf, entity.rect)

                # UPDATE HUD AND DRAW IT
                hud.update(currentWave, score, maxScore[counter], player.health, player.maxHealth, player.lives,
                           player.damage, 600 - sBooster, player.bspeed)
                manager.draw_ui(self.screen)

                # UPDATE SCREEN AND TICK CLOCK
                py.display.update()
                clock.tick(60)

                # ========================================= END GAME LOOP  ===========================================

            # INCREASE COUNTERS AND RESET LOOP
            counter += 1
            currentWave += 1
            running = True

        return won, score