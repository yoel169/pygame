import pygame
from Other.Constants import Constants

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
SCREEN_WIDTH, SCREEN_HEIGHT = Constants.screenSize
halfh = int(SCREEN_HEIGHT / 2)


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.DirtySprite):
    def __init__(self, option):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Media/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(20, halfh))
        self._layer = 1

        # do not set variables above here
        self.arrows = option

        # point store
        self.point_store = [[0, 0, 0], [0, 0, 0]]  # [speed, dam]  [bullet, stat, points spent]
        self.current_track = 0  # 0 speed, 1 damage

        # defaults
        self.base_damage = None
        self.damage_max = None
        self.base_pspeed = None
        self.pspeed_max = None
        self.base_bps = None
        self.bps_max = None
        self.base_lives = None
        self.base_bspeed = None

        # player current stats that can change through game
        self.health = None
        self.lives = None
        self.pspeed = None
        self.damage = None
        self.bspeed = None
        self.bps = None
        self.buffs = [0, 0, 0, 0]  # dam, bps, bspeed, pspeed

        # init player based on track (point store)
        self.set_track()

        # player starting stats that can change from store
        self.base_xp = 500
        self.base_xp_multiplier = 2
        self.xp_gain_multiplier = 1
        self.money_gain_multiplier = 1
        self.support_buff_multiplier = 1
        self.offensive_buff_multiplier = 1

        self.store = [False, 0, 0, 0, 0, 0, 0, 0]  # first 4 not used, offense buffs, support buffs, xp, money

        # player collectibles
        self.score = 0
        self.xp = 0
        self.level = 1
        self.money = 0
        self.time = 0
        self.player_points = 0
        self.stages_beat = []

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if self.arrows:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, (-self.pspeed))
                # move_up_sound.play()
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.pspeed)
                # move_down_sound.play()
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(- self.pspeed, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.pspeed, 0)

        elif self.arrows is False:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -self.pspeed)
                # move_up_sound.play()
            if pressed_keys[K_s]:
                self.rect.move_ip(0, self.pspeed)
                # move_down_sound.play()
            if pressed_keys[K_a]:
                self.rect.move_ip(- self.pspeed, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(self.pspeed, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 110:
            self.rect.top = 110
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # if player goes under/over max make it equal max
        if self.bps < self.bps_max:
            self.bps = self.bps_max

        if self.health > self.maxHealth:
            self.health = self.maxHealth

        if self.damage > self.damage_max:
            self.damage = self.damage_max

        if self.pspeed > self.pspeed_max:
            self.pspeed = self.pspeed_max

        # if player reaches xp for the level increase level, special case for level 1
        if self.level == 1 and self.xp >= self.base_xp * self.level:
            self.level += 1
            self.player_points += 1
        elif self.xp >= self.base_xp * (self.level - 1) * self.base_xp_multiplier:
            self.level += 1
            self.player_points += 1

    def getInfo(self):
        return dict(list(self.__dict__.items())[8:])

    def setInfo(self, db):
        for key, value in db.items():
            setattr(self, key, value)

    # reset user back to defaults
    def reset(self):
        self.health = self.base_hp
        self.lives = self.base_lives
        self.pspeed = self.base_pspeed
        self.damage = self.base_damage
        self.bspeed = self.base_bspeed
        self.bps = self.base_bps
        self.buffs = [0, 0, 0, 0]

    # updating user stats based on track selected
    def set_track(self):

        # defaults reset just in case track was changed
        self.base_damage = 10
        self.damage_max = 30
        self.base_pspeed = 5
        self.pspeed_max = 5
        self.base_bps = 600
        self.bps_max = 300
        self.base_lives = 2
        self.base_hp = 100
        self.maxHealth = 100
        self.base_bspeed = 10

        # speed track
        if self.current_track == 0 and self.point_store[0][1] != 0:

            x = range(1, self.point_store[0][1] + 1)

            for n in x:
                if n % 2 == 0:
                    self.base_pspeed += 1
                    self.pspeed_max += 2
                    self.base_lives += 1
                else:
                    self.base_bps -= 100
                    self.base_hp += 50
                    self.maxHealth += 100

            if self.point_store[0][1] >= 3:
                self.bps_max = 250
            elif self.point_store[0][1] == 5:
                self.bps_max = 200
                self.base_hp = 300
                self.maxHealth = 300

            # multiplying the damage based on how many bullets
            self.base_damage *= self.point_store[0][0] + 1
            self.damage_max *= self.point_store[0][0] + 1

        # dam track
        elif self.point_store[1][1] != 0 and self.current_track == 1:

            x = range(1, self.point_store[1][1] + 1)

            for n in x:
                self.base_damage = 30 * self.point_store[1][1]
                self.damage_max = 60 + (30 * self.point_store[1][1] - 1)

                if n % 2 == 0:
                    self.base_lives += 1
                else:
                    self.base_hp += 50
                    self.maxHealth += 100

                if self.point_store[1][1] == 5:
                    self.base_hp = 300
                    self.maxHealth = 300

        # update the player stats again
        self.health += 100 - self.base_hp
        self.lives += 2 - self.base_lives
        self.pspeed = self.base_pspeed + self.buffs[3]
        self.damage = self.base_damage + self.buffs[0]
        self.bspeed = self.base_bspeed + self.buffs[2]
        self.bps = self.base_bps - self.buffs[1]
