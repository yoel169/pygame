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

        # player starting stats that can change from store
        self.base_hp = 75
        self.maxHealth = 100
        self.base_lives = 2
        self.base_pspeed = 5
        self.pspeed_max = 5
        self.base_damage = 10
        self.damage_max = 30
        self.base_bps = 600
        self.bpsMax = 300
        self.base_bspeed = 10
        self.base_xp = 500
        self.base_xp_multiplier = 2
        self.xp_gain_multiplier = 1
        self.money_gain_multiplier = 1
        self.support_buff_multiplier = 1
        self.offensive_buff_multiplier = 1
        self.store = [False, 0, 0, 0, 0, 0, 0, 0]  # Store, health, dam, speed, offense buffs, support buffs,  xp, money
        self.unlocks = [False, 0, 0, 0]  # unlock store for bullet trees

        # player current stats that can change through game
        self.health = self.base_hp
        self.lives = self.base_lives
        self.pspeed = self.base_pspeed
        self.damage = self.base_damage
        self.bspeed = self.base_bspeed
        self.bps = self.base_bps

        # player collectibles
        self.score = 0
        self.xp = 0
        self.level = 1
        self.money = 0
        self.time = 0
        self.player_points = 0
        self.stages_beat = []

        # point store
        self.point_store = [[0, 0, 0], [0, 0, 0]]  # [speed, dam]  [bullet, stat, points spent]
        self.current_track = 0  # 0 speed, 1 damage

        # dict for all the info
        # self.info = {"self.arrows": self.arrows,
        #         "self.health": self.health,
        #         "self.maxHealth": self.maxHealth,
        #         "self.lives": self.lives,
        #         "self.damage": self.damage,
        #         "self.pspeed": self.pspeed,
        #         "self.bspeed": self.bspeed,
        #         "self.bps": self.bps,
        #         "self.bpsMax": self.bpsMax,
        #         "self.score": self.score,
        #         "self.xp": self.xp,
        #         "self.level": self.level,
        #         "self.money": self.money,
        #         "self.time": self.time,
        #         "self.base_lives": self.base_lives,
        #         "self.base_pspeed": self.base_pspeed,
        #         "self.base_hp": self.base_hp,
        #         "self.base_bps": self.base_bps,
        #         "self.base_xp": self.base_xp,
        #         "self.base_xp_multiplier": self.base_xp_multiplier,
        #         "self.base_damage": self.base_damage,
        #         "self.player_points": self.player_points,
        #         "self.pspeed_max": self.pspeed_max,
        #         "self.money_gain_multiplier": self.money_gain_multiplier,
        #         "self.xp_gain_multiplier": self.xp_gain_multiplier,
        #         "self.offensive_buff_multiplier": self.offensive_buff_multiplier,
        #         "self.support_buff_multiplier": self.support_buff_multiplier,
        #         "self.store": self.store,
        #         "self.unlocks": self.unlocks,
        #         "self.damage_max": self.damage_max}

        # print(dict(list(self.__dict__.items())[8:]))

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
        if self.bps < self.bpsMax:
            self.bps = self.bpsMax

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
        # list = []
        # for x in self.info:
        #     list.append(self.info[x])
        # return tuple(list)
        return dict(list(self.__dict__.items())[8:])

    def setInfo(self, db):
        # counter = 0
        # for x in self.info:
        #     if counter >= len(db):
        #         break
        #     else:
        #          self.info[x] = db[counter]
        #          counter += 1
        for key, value in db.items():
            setattr(self, key, value)

        """
        self.arrows, self.health, self.maxHealth, self.lives, self.damage, self.pspeed, self.bspeed, self.bps, \
        self.bpsMax, self.score, self.xp, self.level, self.money, self.time, self.base_lives, self.base_pspeed, \
        self.base_hp, self.base_bps, self.base_xp, self.base_xp_multiplier, self.base_damage, self.player_points, \
        self.pspeed_max, self.money_gain_multiplier, self.xp_gain_multiplier, self.offensive_buff_multiplier, \
        self.support_buff_multiplier, self.store, self.unlocks, self.damage_max = db
        """

    # reset user back to defaults
    def reset(self):
        self.health = self.base_hp
        self.lives = self.base_lives
        self.pspeed = self.base_pspeed
        self.damage = self.base_damage
        self.bspeed = self.base_bspeed
        self.bps = self.base_bps
