from os import listdir, path
from pickle import dump, load


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