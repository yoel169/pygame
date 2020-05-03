import json
import pygame
from os import listdir, path
import datetime

class PlayerHandler():
    def __init__(self):
        self.saveFile, self.player, self.playerInfo, self.dates, self.settings = {}, None, {}, [], {}

    def save(self, player, info, dates, settings):
        self.player, self.playerInfo, self.dates, self.settings = player, info, dates, settings

        self.saveFile = {'name': self.player, 'playerinfo': self.playerinfo, 'dates': self.dates,
                         'settings': self.settings}

        string = str(info['name']) + '.save'

        with open(string, 'w') as f:
            json.dump(self.saveFile, f, indent=3)

    def getSaves(self):
        names = []
        for file in listdir('Saves/'):
            if file.endswith('.sf'):
                names.append(path.splitext(file)[0])
        return names

    def loadSave(self, filename):
        string = 'Saves/' + filename + '.sf'
        with open(string, 'r') as f:
            self.saveFile = json.load(f)
        return self.saveFile
