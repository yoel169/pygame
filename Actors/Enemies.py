import pygame
import random
from pygame.locals import (
    RLEACCEL
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class BlueJet(pygame.sprite.DirtySprite):
    def __init__(self):
        super(BlueJet, self).__init__()
        self.surf = pygame.image.load("Media/bluejet.jpg").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(90, SCREEN_HEIGHT),
            )
        )
        self._layer = 1
        self.speed = random.randint(3, 8)
        self.damage = 10
        self.health = 10

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        elif self.health <= 0:
            self.kill()
            # death_sound.play()


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class PufferFish(pygame.sprite.DirtySprite):
    def __init__(self):
        super(PufferFish, self).__init__()
        self.surf = pygame.image.load("Media/pf.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self._layer = 1
        self.speed = random.randint(5, 20)
        self.damage = 15
        self.health = 10

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        elif self.health <= 0:
            self.kill()