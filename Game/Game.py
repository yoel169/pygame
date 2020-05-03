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
from Actors.Enemies import EnenmyJet, EBullet
from Game.GamePackUnpacker import Unpacker

# ============================= Updated wave pack reader and game maker using script =================================


class Game:
    def __init__(self, ls, stagename, pack, pl):
        args = ls  # width, height, bg, screen
        self.screen = args[3]
        self.background = args[2]
        self.SW = args[0]
        self.SH = args[1]
        self.title = stagename
        self.player = pl
        # --------------- REAL UNPACK HOURS -----------------
        newUnpacker = Unpacker(pack)
        self.levels = newUnpacker.getLevels()

    # get part: args are user options, index is part #, and sc is score
    def getPart(self, args, index, sc):

        # ---------------- REALEST UNPACK HOURS -------------------
        level = self.levels[index]
        levelTitle = self.title
        maxWaves = len(level)
        # ---------------------------------------------------------

        # INIT TIME VARIABLES
        clock = py.time.Clock()  # time handler for game
        manual_start = 0  # shooting with space time handler if turned on
        auto_start = 0  # auto shooting time handler
        time_delta = 0  # time handler for manager
        score = sc  # player score
        time = 0  # game time

        # INIT GAME VARIABLES
        won = False  # if user won
        checker = True  # for spawning single buffs
        checker2 = True # spawning single enemies
        customMouse = ()  # custom mouse position if movement with mouse is on
        exit = False  # exit game
        auto = True  # default auto to on
        space = False  # default space shooting to off
        mouse = False  # default mouse movement to off
        counter = 0  # counter for looping through arguments

        # ======================================== SHOOTING AND MOVEMENT SETUP ==================================
        option = args  # SHOOTING AND MOVEMENT

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

        # SPRITE GROUPS
        clouds = py.sprite.LayeredDirty()
        bullets = py.sprite.LayeredDirty()
        enemies = py.sprite.LayeredDirty()
        buffs = py.sprite.LayeredDirty()
        all_sprites = py.sprite.LayeredDirty()

        # ADD PLAYER IN ALL SPRITES GROUP
        all_sprites.add(self.player)

        # INITIALIZE GAME
        py.init()

        # CREATE GUI MANAGER
        manager = gui.UIManager((self.SW, self.SH))

        # INIT  HUD WITH SCREEN SIZE, BACKGROUND, LEVEL NAME AND # OF WAVES
        hud = HUD(self.screen, manager, self.background, levelTitle, index + 1, len(self.levels), maxWaves)

        # TIMER EVENTS FOR SPAWNING CLOUDS AND ENEMIES
        ADDCLOUD = py.USEREVENT + 1
        py.time.set_timer(ADDCLOUD, 5000)

        # ====================================== START WAVE LOOP  ==========================================
        for currentWave, wave in enumerate(level,1):

            maxScore = wave[0]
            enemyL = wave[1]
            buffL = wave[2]

            TIMERS, ENEMIES, BUFFS, buffScoreChecker, enemyScoreChecker = [], [], [], [], []

            events = 2

            running = True  # game loop

            # 1 for enemies, 2 for buffs, 3 for both. Spawning enemies or/and buffs
            randCheck = 0
            scoreCheck = 0

            # ENEMY CREATOR  FOR DIFFERENT SPAWN TYPES
            for count, x in enumerate(enemyL, 0):
                if x[1] == 'time':
                    ENEMIES.append(py.USEREVENT + events)
                    TIMERS.append(py.time.set_timer(ENEMIES[count], int(x[2])))
                    events += 1
                    print("timer event for an enemy created")
                elif x[1] == 'random':
                    randCheck = 1
                    print("random event for an enemy created")
                elif x[1] == 'score':
                    if x[0] == 'group':
                        enemyScoreChecker.append(True)
                    scoreCheck = 1
                    print("score event for an enemy created")

            # BUFF CREATOR FOR DIFFERENT SPAWN TYPES
            for count, x in enumerate(buffL, 0):
                if x[1] == 'time':
                    BUFFS.append(py.USEREVENT + events)
                    TIMERS.append(py.time.set_timer(BUFFS[count], int(x[2])))
                    events += 1
                    print("timer event for a buff created")
                elif x[1] == 'random':
                    if randCheck == 1:
                        randCheck = 3
                    else:
                        randCheck = 2
                    print("random event for a buff created")
                elif x[1] == 'score':
                    print("score event for a buff created")
                    if x[0] == 'group':
                        buffScoreChecker.append(True)
                    if scoreCheck == 1:
                        scoreCheck = 3
                    else:
                        scoreCheck = 2

            # ==================================== START  GAME LOOP =========================================
            while running:

                # UPDATE MANAGER
                manager.update(time_delta)

                # WIN BASED ON LAST ARGUMENT
                if score >= maxScore and currentWave == maxWaves:
                    won = True
                    exit = True
                    running = False
                    print("you won!")

                # ELSE NEXT WAVE
                elif score >= maxScore and currentWave != maxWaves:
                    running = False
                    print("next wave!")

                # LOSE ARGUMENT
                if self.player.health <= 0:
                    won = False
                    self.player.health = self.player.maxHealth
                    self.player.lives -= 1
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
                        print("quit called")

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
                            print("escape key called")

                        # SPACE IF TURNED ON
                        if event.key == K_SPACE and space:
                            manual_timer = py.time.get_ticks() - manual_start
                            if manual_timer >= self.player.bps:
                                new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                                bullets.add(new_bullet)
                                all_sprites.add(new_bullet)
                                manual_start = py.time.get_ticks()

                    # -------------------------------- FINISHED CHECKING KEYS ---------------------------------------

                    # MOUSE MOTION EVENT IF TURNED ON
                    elif event.type == MOUSEMOTION and mouse:
                        currentP = py.mouse.get_pos()
                        customMouse = ((currentP[0] - 960) * 0.3, (currentP[1] - 540) * 0.3)
                        self.player.rect.move_ip(customMouse)

                    # MOUSE BUTTON EVENT IF TURNED ON
                    elif event.type == py.MOUSEBUTTONDOWN and event.button == 1 and space is not True and \
                            auto is not True:
                        manual_timer = py.time.get_ticks() - manual_start
                        if manual_timer >= self.player.bps:
                            new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                            bullets.add(new_bullet)
                            all_sprites.add(new_bullet)
                            manual_start = py.time.get_ticks()

                    # ENEMY TIMED SPAWN EVENT
                    elif event.type in ENEMIES:
                        for x in enemyL:
                            if x[1] == 'time':
                                if x[0] == 'single':
                                    new_enemy = EnenmyJet(int(x[3]))
                                    enemies.add(new_enemy)
                                    all_sprites.add(new_enemy)
                                    print("spawned single enemy from timer")
                                elif x[0] == 'group':
                                    num = random.randint(1, 100)
                                    acc = 0
                                    dc = x[3]
                                    for index, x in enumerate(dc['chance'], 0):
                                        acc += int(x)
                                        if num < acc:
                                            new_enemy = EnenmyJet(int(dc['type'][index]))
                                            enemies.add(new_enemy)
                                            all_sprites.add(new_enemy)
                                            print("spawned an enemy from group timer")
                                            break

                    # BUFF TIMED SPAWN EVENT
                    elif event.type in BUFFS:
                        for x in buffL:
                            if x[1] == 'time':
                                print("buff created from timer")
                                if x[0] == 'single':
                                    new_buff = Buff(int(x[3]))
                                    buffs.add(new_buff)
                                    all_sprites.add(new_buff)
                                elif x[0] == 'group':
                                    num = random.randint(1, 100)
                                    acc = 0
                                    dc = x[3]
                                    for index, x in enumerate(dc['chance'], 0):
                                        acc += int(x)
                                        if num < acc:
                                            new_buff = Buff(int(dc['type'][index]))
                                            buffs.add(new_buff)
                                            all_sprites.add(new_buff)
                                            break

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
                if auto_timer >= self.player.bps and auto:
                    new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed)
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)
                    auto_start = py.time.get_ticks()

                # SPAWNING ENEMY BULLETS
                for enemy in enemies:
                    if random.randint(1,100) == 1:
                        if enemy.type == 1:
                            new_bullet = EBullet(enemy.rect.center, enemy.damage, enemy.pspeed + 5)
                            bullets.add(new_bullet)
                            all_sprites.add(new_bullet)

                # ============================= SPAWNING BUFFS AND ENEMIES FROM SCORE =========================

                # BUFF SPAWN FROM SCORE
                if scoreCheck == 2 or scoreCheck == 3:
                    for pos, x in enumerate(buffL, 0):
                        if x[1] == 'score':
                            if x[0] == 'single' and score % int(x[2]) == 0 and checker2 and score != 0:
                                new_buff = Buff(int(x[3]))
                                buffs.add(new_buff)
                                all_sprites.add(new_buff)
                                checker2 = False
                                print("buff spawned at score " + str(score))
                            elif x[0] == 'group' and score % int(x[2]) == 0 and buffScoreChecker[pos] and score != 0:
                                    num = random.randint(1, 100)
                                    acc = 0
                                    dc = x[3]
                                    for index, x in enumerate(dc['chance'], 0):
                                        acc += int(x)
                                        if num < acc:
                                            new_buff = Buff(int(dc['type'][index]))
                                            buffs.add(new_buff)
                                            all_sprites.add(new_buff)
                                            buffScoreChecker[pos] = False
                                            print("buff spawned at score " + str(score))
                                            break

                # RESET BUFF SPAWN QUEUE
                if scoreCheck == 2 or scoreCheck == 3:
                    for pos, x in enumerate(buffL, 0):
                        if x[1] == 'score':
                            if x[0] == 'single' and score % int(x[2]) != 0 and score !=0 and not checker:
                                checker2 = True
                            elif x[0] == 'group' and score % int(x[2]) != 0 and score !=0 and not buffScoreChecker[pos]:
                                buffScoreChecker[pos] = True
                                print("group buff reset")

                # SPAWN ENEMY FROM SCORE
                if scoreCheck == 1 or scoreCheck == 3:
                    for pos, x in enumerate(enemyL, 0):
                        if x[1] == 'score':
                            if x[0] == 'single' and score % int(x[2]) == 0 and checker2 and score != 0:

                                new_enemy = EnenmyJet(int(x[3]))
                                enemies.add(new_enemy)
                                all_sprites.add(new_enemy)
                                checker2 = False
                                print("enemy spawned at score " + str(score))

                            elif x[0] == 'group' and score % int(x[2]) == 0 and enemyScoreChecker[pos] and score != 0:
                                num = random.randint(1, 100)
                                acc = 0
                                dc = x[3]
                                for index, x in enumerate(dc['chance'], 0):
                                    acc += int(x)
                                    if num < acc:
                                        new_enemy = Buff(int(dc['type'][index]))
                                        enemies.add(new_enemy)
                                        all_sprites.add(new_enemy)
                                        enemyScoreChecker[pos] = False
                                        print("enemy spawned at score " + str(score))
                                        break

                # RESET ENEMY SPAWN QUEUE
                if scoreCheck == 1 or scoreCheck == 3:
                    for pos, x in enumerate(enemyL, 0):
                        if x[1] == 'score':
                            if x[0] == 'single' and score % int(x[2]) != 0 and score !=0:
                                checker2 = True
                            elif x[1] == 'group' and score % int(x[2]) != 0 and score !=0:
                                enemyScoreChecker[pos] = True

                # ============================= SPAWNING BUFFS AND ENEMIES FROM RANDOM =========================
                # BUFF
                if randCheck == 2 or randCheck == 3:
                    for pos, x in enumerate(buffL, 0):
                        if x[1] == 'random':
                            y = random.randint(1, 6000)
                            if y in range(1, int(x[2]) + 1):
                                print("buff created from random #", y, int(x[2]))
                                if x[0] == 'single':
                                    new_buff = Buff(int(x[3]))
                                    buffs.add(new_buff)
                                    all_sprites.add(new_buff)
                                elif x[0] == 'group':
                                    num = random.randint(1, 100)
                                    acc = 0
                                    dc = x[3]
                                    for index, x in enumerate(dc['chance'], 0):
                                        acc += int(x)
                                        if num < acc:
                                            new_buff = Buff(int(dc['type'][index]))
                                            buffs.add(new_buff)
                                            all_sprites.add(new_buff)
                                            break
                # ENEMY
                if randCheck == 1 or randCheck == 3:
                    for pos, x in enumerate(enemyL, 0):
                        if x[1] == 'random':
                            y = random.randint(1, 6000)
                            if y in range(1, int(x[2]) + 1):
                                print("enemy created from random #", y, int(x[2]))
                                if x[0] == 'single':
                                    new_enemy = EnenmyJet(int(x[3]))
                                    enemies.add(new_enemy)
                                    all_sprites.add(new_enemy)
                                elif x[0] == 'group':
                                    num = random.randint(1, 100)
                                    acc = 0
                                    dc = x[3]
                                    for index, x in enumerate(dc['chance'], 0):
                                        acc += int(x)
                                        if num < acc:
                                            new_enemy = EnenmyJet(int(dc['type'][index]))
                                            enemies.add(new_enemy)
                                            all_sprites.add(new_enemy)
                                            break

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
                hit = py.sprite.spritecollideany(self.player, bullets)
                if hit.__class__ == EBullet and hit != None:
                    self.player.health -= hit.damage
                    print("you got hit by enemy bullet!")
                    hit.kill()

                # PLAYER AND BUFF COLLISION
                hit = py.sprite.spritecollideany(self.player, buffs)
                if hit != None:
                    if hit.type == 0:
                        if self.player.health <= self.player.maxHealth:
                            self.player.health += hit.power
                    elif hit.type == 1:
                        self.player.damage += hit.power
                    else:
                        if not self.player.bps <= self.player.bpsMax:
                            self.player.bps - hit.power
                    print("power up!")
                    hit.kill()

                # ENEMY AND PLAYER COLLISION
                hit = py.sprite.spritecollideany(self.player, enemies)
                if hit != None:
                    self.player.health -= hit.damage
                    print("you got hit!")
                    hit.kill()

                # ======================================== END COLLISION DETECTION =================================

                # GET KEYS AND UPDATE PLAYER POSITION
                pressed_keys = py.key.get_pressed()
                self.player.update(pressed_keys)

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

                time += 1

                # UPDATE HUD AND DRAW IT
                hud.update(currentWave, score, maxScore, self.player.health, self.player.maxHealth, self.player.lives,
                           self.player.damage, self.player.bps, self.player.bspeed, 0, int(time /60))  # todo money variable
                manager.draw_ui(self.screen)

                # UPDATE SCREEN AND TICK CLOCK
                py.display.update()
                clock.tick(60)

                # ========================================= END GAME LOOP  ===========================================
            if exit:
                print("exited")
                return won, score, self.player

        return won, score, self.player