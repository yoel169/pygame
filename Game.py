 # Import the pygame module
import pygame

from Players import (
    Player,
    Bullet,
    Enemy,
    Cloud
)

from Messages import points_update

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("game.mp3")
pygame.mixer.music.play(loops=-1)

# Load all sound files
# move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
# move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
death_sound = pygame.mixer.Sound("BadHitSound.ogg")
collision_sound = pygame.mixer.Sound("HitSound.ogg")

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy/clouds
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
player = Player()
bullets = pygame.sprite.LayeredDirty()
enemies = pygame.sprite.LayeredDirty()
clouds = pygame.sprite.LayeredDirty()
all_sprites = pygame.sprite.LayeredDirty()

# Instantiate player. Right now, this is just a rectangle.
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
start_time = 0

score = 0

pause = False

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            time_since_enter = pygame.time.get_ticks() - start_time
            # If the Esc key is pressed, then exit the main loop
            if (event.key == K_ESCAPE):
                running = False
            if event.key == K_SPACE and time_since_enter >= 300:
                new_bullet = Bullet(player.rect.center)
                bullets.add(new_bullet)
                all_sprites.add(new_bullet)
                start_time = pygame.time.get_ticks()
                #print(str(start_time))

        # Check for QUIT event. If QUIT, then set running to false.
        if event.type == QUIT:
            running = False

        # Add a new enemy?
        if event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        if event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update enemy position
    enemies.update()
    clouds.update()
    bullets.update()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((135, 206, 250))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # hits is a dict. The enemies are the keys and bullets the values.
    hits = pygame.sprite.groupcollide(enemies, bullets, False, True)
    for enemy, bullet_list in hits.items():
        for bullet in bullet_list:
            enemy.health -= bullet.damage
            collision_sound.play()
            if enemy.health <= 0:
                  death_sound.play()
                  score +=1

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()

        # Stop any moving sounds and play the collision sound
        #move_up_sound.stop()
        #move_down_sound.stop()
        collision_sound.play()

        running = False

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

    points_update(score, screen)

    # Update the display
    pygame.display.flip()

# All done! Stop and quit the mixer.
pygame.mixer.music.stop()
pygame.mixer.quit()