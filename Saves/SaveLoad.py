from os import listdir, path
from pickle import dump, load
import datetime
from Actors.Players import Player


class PlayerHandler():
    def __init__(self):
        self.saveFile = {}

    def save(self, db):

        string = 'Saves/' +str(db['name']) + '.sf'

        with open(string, 'bw') as f:
            dump(db, f)

    def getSaves(self):
        names = []
        for file in listdir('Saves/'):
            if file.endswith('.sf'):
                names.append(path.splitext(file)[0])
        return names

    def loadSave(self, filename):
        string = 'Saves/' + filename + '.sf'
        with open(string, 'rb') as f:
            self.saveFile = load(f)
        return self.saveFile

    def launch(self, name1, name2, opt1, opt2):

        time2 = datetime.datetime.now()
        time2 = time2.strftime("%m-%d-%y %I:%M:%S %p")

        if name1 is not None:
            player_save = self.loadSave(name1)

            return player_save

        else:
            if len(name2) != 0:
                name = name2
            else:
                name = 'player'
            db = {'name': name, 'player': Player(False).getInfo(), 'times': [time2, time2],
                  'settings': [opt1, opt2], 'stage': [0, 0]}

            self.save(db)

            return db



