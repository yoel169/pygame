import pygame
import random
from pygame.locals import (
    RLEACCEL
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

cloud = pygame.image.load("Media/cloud.png")
bullet1 = pygame.image.load("Media/bullet.png")
carrot = pygame.image.load("Media/carrot.png")
healthbuff = pygame.image.load("Media/healthbuff.png")
damagebuff = pygame.image.load("Media/damagebuff.png")
bulletbuff = pygame.image.load("Media/bulletbuff.png")
ebullet = pygame.image.load("Media/ebullet.png")

images = [cloud,bullet1, ebullet, carrot,healthbuff,damagebuff,bulletbuff]


class Cloud(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = images[0].convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 0
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 200, SCREEN_WIDTH + 300),
                random.randint(130, SCREEN_HEIGHT - 50),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()


class Bullet1(pygame.sprite.DirtySprite):
    def __init__(self, flag, position, power, speed):
        super(Bullet1, self).__init__()
        self.surf = images[1].convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self._layer = 1
        self.damage = power
        self.speed = speed
        self.bad = flag
        if flag:  # if bullet called by enemy flip direction of bullet and ceneter
            self.rect = self.surf.get_rect(center=position)
        else:
            self.rect = self.surf.get_rect(center=(position[0], position[1] + 25))

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.rect.move_ip( - self.speed, 0)
        if not self.bad and self.rect.left > SCREEN_WIDTH:
            self.kill()
        elif self.bad and self.right < 0:
            self.kill()


class EBullet(pygame.sprite.DirtySprite):
    def __init__(self, position, power, speed):
        super(EBullet, self).__init__()
        self.surf = images[2].convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
        self._layer = 1
        self.damage = power
        self.speed = speed

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.rect.move_ip( self.speed, 0)
        if self.right < 0:
            self.kill()


class Carrot(pygame.sprite.DirtySprite):
    def __init__(self, position):
        super(Carrot, self).__init__()
        self.surf = images[3].convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
        self.pos = pygame.math.Vector2(position)
        self.vel = pygame.math.Vector2(0, -450)
        self._layer = 1
        self.damage = 10

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.rect.move_ip(5, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


# ===================================== BUFFS =========================================================


class HealthBuff(pygame.sprite.DirtySprite):
    def __init__(self):
        super(HealthBuff, self).__init__()
        self.surf = images[4].convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 1
        self.power = 25
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(90, SCREEN_HEIGHT - 50),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class DamageBuff(pygame.sprite.DirtySprite):
    def __init__(self):
        super(DamageBuff, self).__init__()
        self.surf = images[5].convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 1
        self.power = 5
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(90, SCREEN_HEIGHT - 50),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

class BulletBuff(pygame.sprite.DirtySprite):
    def __init__(self):
        super(BulletBuff, self).__init__()
        self.surf = images[6].convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self._layer = 1
        self.power = 60  # ms
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(90, SCREEN_HEIGHT - 50),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()