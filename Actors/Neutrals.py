import pygame
import random
from Other.Constants import Constants
from pygame.locals import (
    RLEACCEL
)

# Define constants for the screen width and height
SCREEN_WIDTH, SCREEN_HEIGHT = Constants.screenSize


class Cloud(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("Media/cloud.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 0
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 200, SCREEN_WIDTH + 300),
                random.randint(150, SCREEN_HEIGHT - 50),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()


class Bullet1(pygame.sprite.DirtySprite):
    def __init__(self, position, power, speed, track, pos):
        super(Bullet1, self).__init__()
        names = ['bullet', 'big']
        self.surf = pygame.image.load(names[track] + str(pos + 1) + '.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self._layer = 1
        self.damage = power
        self.speed = speed
        self.rect = self.surf.get_rect(center=(position[0], position[1] + 25))

        # bullet health. yup that's a thing now too
        if track == 1 and pos >= 2:
            self.health = 2
        elif track == 1 and pos >= 4:
            self.health = 4
        else:
            self.health = 1

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


# class Carrot(pygame.sprite.DirtySprite):
#     def __init__(self, position):
#         super(Carrot, self).__init__()
#         self.surf = carrot = pygame.image.load("Media/carrot.png").convert()
#         self.surf.set_colorkey((0, 0, 0), RLEACCEL)
#         self.rect = self.surf.get_rect(center=position)
#         self.pos = pygame.math.Vector2(position)
#         self.vel = pygame.math.Vector2(0, -450)
#         self._layer = 1
#         self.damage = 10
#
#     def update(self):
#         # Add the velocity to the position vector to move the sprite.
#         self.rect.move_ip(5, 0)
#         if self.rect.left > SCREEN_WIDTH:
#             self.kill()


# ===================================== BUFFS =========================================================


class Buff(pygame.sprite.DirtySprite):
    def __init__(self, type):
        super(Buff, self).__init__()
        self.type = type  # health, damage, and bullet
        if type == 0:
            self.surf = pygame.image.load("Media/healthbuff.png").convert()
            self.power = 15
        elif type == 1:
            self.surf = pygame.image.load("Media/damagebuff.png").convert()
            self.power = 5
        else:
            self.surf = pygame.image.load("Media/bulletbuff.png").convert()
            self.power = 60  # ms

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 1
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(180, SCREEN_HEIGHT - 100),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()