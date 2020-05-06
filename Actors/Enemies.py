import pygame
import random
from Other.Constants import Constants
from pygame.locals import (
    RLEACCEL
)

# Define constants for the screen width and height
SCREEN_WIDTH , SCREEN_HEIGHT = Constants.screenSize


class EnenemyJet(pygame.sprite.DirtySprite):
    def __init__(self, type):
        super(EnenemyJet, self).__init__()
        self.type = type
        #  initialize based on enemy type, B, B+, G
        if type == 0:
            self.surf = pygame.image.load("Media/bluejet.png").convert()
            self.speed = random.randint(4, 8)
            self.damage = 10
            self.health = 10
            self.points = 1
            self.xp = 3
            self.money = 1
        elif type == 1:
            self.surf = pygame.image.load("Media/bluejetplus.png").convert()
            self.speed = random.randint(6, 10)
            self.damage = 12
            self.health = 20
            self.points = 2
            self.xp = 9
            self.money = 3
        elif type ==2:
            self.surf = pygame.image.load("Media/greenjet.png").convert()
            self.speed = random.randint(4, 8)
            self.damage = 20
            self.health = 30
            self.points = 3
            self.xp = 6
            self.money = 2
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(180, SCREEN_HEIGHT - 100),
            )
        )
        self._layer = 1

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        if self.health <= 0:
            self.kill()


class EBullet(pygame.sprite.DirtySprite):
    def __init__(self, position, power, speed):
        super(EBullet, self).__init__()
        self.surf = pygame.image.load("Media/ebullet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
        self._layer = 2
        self.damage = power
        self.speed = speed

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.rect.move_ip( - self.speed, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()