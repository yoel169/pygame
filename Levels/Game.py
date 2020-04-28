import pygame
import random
from Actors.Players import Player
from Actors.Neutrals import Cloud, Bullet1, HealthBuff, DamageBuff, BulletBuff
from Actors.Enemies import BlueJet, GreenJet
from Other.Messages import text_update

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
    MOUSEMOTION,
)


class Game():
    def __init__(self, width, height, screen, option, option2):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.screen = screen
        self.auto = True  # default auto to on
        self.space = False  # default space shooting to off
        self.mouse = False  # default mouse movement to off

        #shoot auto, with space or with mouse
        if option == 0:
            self.auto = True
        elif option == 1:
            self.space = True
            self.auto = False
        else:
            self.space = False
            self.auto = False

       #move with arrows, wads, or mouse
        arrows = None  # default to None
        if option2 == 0:
           arrows = True
        elif option2 == 1:
            arrows = False
        else:
            self.mouse = True

        # Setup for sounds. Defaults are good.
        pygame.mixer.init()

        # Load and play background music
        pygame.mixer.music.load("Media/game2.mp3")
        pygame.mixer.music.play(loops=-1)

        # Load all sound files
        # move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
        # move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
        #self.death_sound = pygame.mixer.Sound("BadHitSound.ogg")
        #self.collision_sound = pygame.mixer.Sound("HitSound.ogg")

        # Initialize pygame
        pygame.init()

        # Create a custom event for adding a new enemy/clouds
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 1000)
        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 5000)

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        self.player = Player(arrows)
        self.bullets = pygame.sprite.LayeredDirty()
        self.enemies = pygame.sprite.LayeredDirty()
        self.clouds = pygame.sprite.LayeredDirty()
        self.buffs = pygame.sprite.LayeredDirty()
        self.all_sprites = pygame.sprite.LayeredDirty()

        # Instantiate player.
        self.all_sprites.add(self.player)

    def run(self):
        # Variable to keep the main loop running
        running = True

        # Setup the clock for a decent framerate
        clock = pygame.time.Clock()
        manual_start = 0
        auto_start = 0

        score = 0
        won = False
        checker = True
        sBooster = 0
        exit = False
        customMouse = ()
        pygame.mouse.set_visible(False)

        # ====================================================================================
        #                       First Main loop (First Wave)
        # ====================================================================================
        while running:

            if self.mouse:  # if user is moving with mouse
                pygame.mouse.set_pos(960, 540)  # always center mouse

            # for loop through the event queue
            for event in pygame.event.get():
                # Check for KEYDOWN event
                if event.type == KEYDOWN:
                    # If the Esc key is pressed, then exit the main loop
                    if event.key == K_ESCAPE:
                        running = False
                        exit = True
                        won = False

                    if event.key == K_SPACE and self.space:
                        manual_timer = pygame.time.get_ticks() - manual_start
                        if manual_timer >= 600 - sBooster:
                            new_bullet = Bullet1(self.player.rect.center, self.player.damage)
                            self.bullets.add(new_bullet)
                            self.all_sprites.add(new_bullet)
                            manual_start = pygame.time.get_ticks()

                if event.type == MOUSEMOTION and self.mouse:
                    currentP = pygame.mouse.get_pos()
                    customMouse = ((currentP[0] - 960) * 0.3, (currentP[1] - 540)*0.3)
                    self.player.rect.move_ip(customMouse)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.space is not True and self.auto is not True:
                    manual_timer = pygame.time.get_ticks() - manual_start
                    if manual_timer >= 600 - sBooster:
                        new_bullet = Bullet1(self.player.rect.center, self.player.damage)
                        self.bullets.add(new_bullet)
                        self.all_sprites.add(new_bullet)
                        manual_start = pygame.time.get_ticks()

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

            auto_timer = pygame.time.get_ticks() - auto_start

            if auto_timer >= 600 - sBooster and self.auto:
                new_bullet = Bullet1(self.player.rect.center, self.player.damage, self.player.bspeed + 5)
                self.bullets.add(new_bullet)
                self.all_sprites.add(new_bullet)
                auto_start = pygame.time.get_ticks()

            # hits is a dict. The enemies are the keys and bullets the values.
            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullet_list in hits.items():
                for bullet in bullet_list:
                    enemy.health -= bullet.damage
                    #self.collision_sound.play()
                    if enemy.health <= 0:
                        if enemy.__class__ == BlueJet:
                            score += 1
                        else:
                            score += 3

            if score % 20 == 0 and checker and score != 0:  # spawn a new buff
                num = random.randint(1, 100)
                if num in range(0,51):
                    new_buff = HealthBuff()
                elif num in range(50,76):
                    new_buff = DamageBuff()
                else:
                    new_buff = BulletBuff()
                self.buffs.add(new_buff)
                self.all_sprites.add(new_buff)
                checker = False

            elif score % 20 != 0 and score != 0:  # clear spawn queue
                checker = True

            if score >= 100:  # move to wave 2
                running = False

            # Check if any enemies have collided with the player
            hit = pygame.sprite.spritecollideany(self.player, self.enemies)
            if hit != None:
                self.player.health -= hit.damage
                print("you got hit!")
                hit.kill()

            # collide with power up
            hit = pygame.sprite.spritecollideany(self.player, self.buffs)
            if hit != None:
                if hit.__class__ == HealthBuff:
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

            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()

            # Update the player sprite based on user keypresses
            self.player.update(pressed_keys)

            # Update positions
            self.enemies.update()
            self.clouds.update()
            self.bullets.update()
            self.buffs.update()

            # Fill the screen with blue
            self.screen.fill((135, 206, 250))

            # Draw all sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            text_update(score, self.player.health, self.player.lives, self.screen)
            pygame.draw.line(self.screen, (0, 0, 0), (0, 110), (self.SCREEN_WIDTH, 110), 3)

            # Ensure program maintains a rate of 60 frames per second
            clock.tick(60)

            # Update the display
            pygame.display.flip()

        if not exit:
            running = True

        # =======================================================================================================
        #                                   Second Main loop (Second Wave)
        # =======================================================================================================

        while running:

            if self.mouse:  # if user is moving with mouse
                pygame.mouse.set_pos(960, 540)  # always center mouse

            # for loop through the event queue
            for event in pygame.event.get():
                # Check for KEYDOWN event
                if event.type == KEYDOWN:
                    # If the Esc key is pressed, then exit the main loop
                    if event.key == K_ESCAPE:
                        exit = True
                        running = False
                        won = False

                    if event.key == K_SPACE and self.space:
                        manual_timer = pygame.time.get_ticks() - manual_start
                        if manual_timer >= 600 - sBooster:
                            new_bullet = Bullet1(self.player.rect.center, self.player.damage)
                            self.bullets.add(new_bullet)
                            self.all_sprites.add(new_bullet)
                            manual_start = pygame.time.get_ticks()

                # Check for QUIT event. If QUIT, then set running to false.
                if event.type == QUIT:
                    running = False
                    won = False

                if event.type == MOUSEMOTION and self.mouse:
                    currentP = pygame.mouse.get_pos()
                    customMouse = ((currentP[0] - 960) * 0.3, (currentP[1] - 540)*0.3)
                    self.player.rect.move_ip(customMouse)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.space is not True and self.auto is not True:
                    manual_timer = pygame.time.get_ticks() - manual_start
                    if manual_timer >= 600 - sBooster:
                        new_bullet = Bullet1(self.player.rect.center, self.player.damage)
                        self.bullets.add(new_bullet)
                        self.all_sprites.add(new_bullet)
                        manual_start = pygame.time.get_ticks()

                # Add a new enemy?
                if event.type == self.ADDENEMY:
                    num = random.randint(1, 10)
                    if num in range(1, 6):
                        new_enemy = BlueJet()
                        self.enemies.add(new_enemy)
                        self.all_sprites.add(new_enemy)
                    else:
                        new_enemy = GreenJet()
                        self.enemies.add(new_enemy)
                        self.all_sprites.add(new_enemy)

                # Add a new cloud?
                if event.type == self.ADDCLOUD:
                     # Create the new cloud and add it to sprite groups
                    new_cloud = Cloud()
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)

            auto_timer = pygame.time.get_ticks() - auto_start

            if auto_timer >= 600 - sBooster and self.auto:
                new_bullet = Bullet1(self.player.rect.center, self.player.damage)
                self.bullets.add(new_bullet)
                self.all_sprites.add(new_bullet)
                auto_start = pygame.time.get_ticks()

            # hits is a dict. The enemies are the keys and bullets the values.
            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullet_list in hits.items():
                for bullet in bullet_list:
                    enemy.health -= bullet.damage
                    # self.collision_sound.play()
                    if enemy.health <= 0:
                        if enemy.__class__ == BlueJet:
                            score += 1
                        else:
                            score += 3

            if score % 40 == 0 and checker and score != 0:  # spawn a new buff
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

            elif score % 40 != 0 and score != 0:
                checker = True

            if score >= 300:
                won = True
                running = False

            # Check if any enemies have collided with the player
            hit = pygame.sprite.spritecollideany(self.player, self.enemies)
            if hit != None:
                self.player.health -= hit.damage
                print("you got hit!")
                hit.kill()

            # collide with power up
            hit = pygame.sprite.spritecollideany(self.player, self.buffs)
            if hit != None:
                if hit.__class__ == HealthBuff:
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

            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()

            # Update the player sprite based on user keypresses
            self.player.update(pressed_keys)

            # Update positions
            self.enemies.update()
            self.clouds.update()
            self.bullets.update()
            self.buffs.update()

            # Fill the screen with blue
            self.screen.fill((135, 206, 250))

            # Draw all sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            text_update(score, self.player.health, self.player.lives, self.screen)
            pygame.draw.line(self.screen, (0, 0, 0), (0, 110), (self.SCREEN_WIDTH, 110), 3)

            # Ensure program maintains a rate of 60 frames per second
            clock.tick(60)

            # Update the display
            pygame.display.flip()

        # All done! Stop and quit the mixer.
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        pygame.mouse.set_visible(True)

        return won, score
