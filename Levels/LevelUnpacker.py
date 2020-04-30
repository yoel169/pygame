import json

# =================================== UNPACK A LEVEL PACK ===================================


class Unpacker:
    def __init__(self, pack):

        with open(pack, 'r') as f:
            self.data = json.load(f)

    def get(self):
        for level in self.data:
            print("level")
            for waves in level:
                for x in waves.values():
                    print(waves, x)


me = Unpacker('levels.json')
me.get()