import json
import pygame as py
import random
# =================================== UNPACK A LEVEL PACK ===================================


class Unpacker:
    def __init__(self, pack):

        with open(pack, 'r') as f:
            self.data = json.load(f)

    def getLevels(self):
        levels = []
        for level in self.data:  #levels
            for wave, value in level.items():  # waves
                waves = []
                for values in value:  # wave info
                    for a, b in values.items():
                        maxscore = int(values['maxScore'])
                        enemies = values['enemies']
                        buffs = values['buffs']
                    waves.append([maxscore,enemies,buffs])
            levels.append(waves)

        return levels
