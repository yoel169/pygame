import json
import pygame as py
import random

# =================================== UNPACK A WAVE PACK ===================================


class Unpacker:
    def __init__(self, pack):

        with open(pack, 'r') as f:
            self.data = json.load(f)
            # print(self.data)

    def getPack(self):
        levels = []
        xp = []
        for level in self.data:  # parts
            waves= []
            for wave in level['waves']:  # waves
                maxscore = int(wave['maxScore'])
                enemies = wave['enemies']
                buffs = wave['buffs']
                waves.append([maxscore, enemies, buffs])
            levels.append(waves)
            xp.append(level['xp'])

        #print(levels)
        return levels, xp