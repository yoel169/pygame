import pygame
import pygame_gui
from Actors.Players import Player
from Actors.Neutrals import Cloud, Bullet1, PowerUp1
from Actors.Enemies import BlueJet
from Other.Messages import text_update

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)


class Game():
    def __init__(self, width, height, screen):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.screen = screen

        # Define constants for the screen width and height
        # SCREEN_WIDTH = 800
        # SCREEN_HEIGHT = 600

        # Setup for sounds. Defaults are good.
        pygame.mixer.init()

        # Load and play background music
        # Sound source: http://ccmixter.org/files/Apoxode/59262
        # License: https://creativecommons.org/licenses/by/3.0/
        pygame.mixer.music.load("Media/game.mp3")
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
        pygame.time.set_timer(self.ADDENEMY, 500)
        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1000)
        self.ADDPOWERUP1 = pygame.event.Event(pygame.USEREVENT, attr1='Event1')

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        self.player = Player()
        self.bullets = pygame.sprite.LayeredDirty()
        self.enemies = pygame.sprite.LayeredDirty()
        self.clouds = pygame.sprite.LayeredDirty()
        self.pwu = pygame.sprite.LayeredDirty()
        self.all_sprites = pygame.sprite.LayeredDirty()

        # Instantiate player.
        self.all_sprites.add(self.player)

    def run(self):
        # Variable to keep the main loop running
        running = True
        speedM = 0

        # Setup the clock for a decent framerate
        clock = pygame.time.Clock()
        start_time = 0

        score = 0
        won = False
        checker = True

        # Main loop
        while running:

            # for loop through the event queue
            for event in pygame.event.get():
                # Check for KEYDOWN event
                if event.type == KEYDOWN:
                    # If the Esc key is pressed, then exit the main loop
                    if event.key == K_ESCAPE:
                        running = False
                        won = False


                # Check for QUIT event. If QUIT, then set running to false.
                if event.type == QUIT:
                    running = False
                    won = False

                if pygame.time.get_ticks() >= 3000:
                    # Add a new enemy?
                    if event.type == self.ADDENEMY:
                        # Create the new enemy and add it to sprite groups
                        new_enemy = BlueJet()
                        self.enemies.add(new_enemy)
                        self.all_sprites.add(new_enemy)

                    # Add a new cloud?
                    if event.type == self.ADDCLOUD:
                        # Create the new cloud and add it to sprite groups
                        new_cloud = Cloud()
                        self.clouds.add(new_cloud)
                        self.all_sprites.add(new_cloud)

            time_since_enter = pygame.time.get_ticks() - start_time

            if time_since_enter >= 600 - speedM:
                new_bullet = Bullet1(self.player.rect.center, self.player.damage)
                self.bullets.add(new_bullet)
                self.all_sprites.add(new_bullet)
                start_time = pygame.time.get_ticks()

            # hits is a dict. The enemies are the keys and bullets the values.
            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullet_list in hits.items():
                for bullet in bullet_list:
                    enemy.health -= bullet.damage
                    #self.collision_sound.play()
                    if enemy.health <= 0:
                        score += 1

            if score % 15 == 0 and checker and score != 0:
                #pygame.event.post(self.ADDPOWERUP1)
                new_pwu = PowerUp1()
                self.pwu.add(new_pwu)
                self.all_sprites.add(new_pwu)
                checker = False

            elif score % 15 != 0 and score != 0:
                checker = True

            if score >= 100:
                won = True
                running = False

            # Check if any enemies have collided with the player
            hit = pygame.sprite.spritecollideany(self.player, self.enemies)
            if hit != None:
                self.player.health -= hit.damage
                print("you got hit!")
                hit.kill()

            # collide with power up
            hit = pygame.sprite.spritecollideany(self.player, self.pwu)
            if hit != None:
                self.player.speed += hit.power
                self.player.health += hit.power * 10
                self.player.damage += hit.power * 10
                if speedM < 300:
                    speedM += 100
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
            self.pwu.update()

            # Fill the screen with blue
            self.screen.fill((135, 206, 250))

            # Draw all sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            # Ensure program maintains a rate of 60 frames per second
            clock.tick(60)

            text_update(score, self.player.health, self.player.lives, self.screen)
            pygame.draw.line(self.screen,(0,0,0),(0,65),(self.SCREEN_WIDTH, 65),3)

            # Update the display
            pygame.display.flip()

        # All done! Stop and quit the mixer.
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        return won, score
