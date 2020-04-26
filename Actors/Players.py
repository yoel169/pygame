import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
halfh = int (SCREEN_HEIGHT/2)

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.DirtySprite):
    def __init__(self, option):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Media/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (20, halfh ))
        self._layer = 1
        self.health = 50
        self.lives = 2
        self.speed = 0
        self.damage = 1
        self.arrows = option

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if self.arrows:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5 - self.speed)
                # move_up_sound.play()
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5 + self.speed)
                # move_down_sound.play()
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5- self.speed, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5 + self.speed, 0)
        elif self.arrows is False:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -5 - self.speed)
                # move_up_sound.play()
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 5 + self.speed)
                # move_down_sound.play()
            if pressed_keys[K_a]:
                self.rect.move_ip(-5- self.speed, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(5 + self.speed, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 110:
            self.rect.top = 110
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # new life if health reaches 100
        if self.health >= 100:
            self.lives += 1
            self.health = 50

        # lose life if health is at 0
        if self.health <= 0:
            self.health = 30
            self.lives -= 1
