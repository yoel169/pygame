import pygame
import random
from pygame.locals import (
    RLEACCEL
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Cloud(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("Media/cloud.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 0
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(90, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Bullet1(pygame.sprite.DirtySprite):
    def __init__(self, position):
        super(Bullet1, self).__init__()
        self.surf = pygame.image.load("Media/bullet.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
        self.pos = pygame.math.Vector2(position)
        self.vel = pygame.math.Vector2(0, -450)
        self._layer = 1
        self.damage = 10

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.rect.move_ip(10, 0)
        if self.rect.bottom <= 0:
            self.kill()


class Carrot(pygame.sprite.DirtySprite):
    def __init__(self, position):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load("Media/carrot.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
        self.pos = pygame.math.Vector2(position)
        self.vel = pygame.math.Vector2(0, -450)
        self._layer = 1
        self.damage = 10

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.rect.move_ip(5, 0)
        if self.rect.bottom <= 0:
            self.kill()


class PowerUp1(pygame.sprite.DirtySprite):
    def __init__(self):
        super(PowerUp1, self).__init__()
        self.surf = pygame.image.load("Media/cloud.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 0
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()