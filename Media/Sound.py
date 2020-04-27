import pygame


class Sound:
    def __init__(self, url, channel=0, volume=1):
        self.SOUND = pygame.mixer.Sound(url)
        self.CHANNEL = channel

        self.SOUND.set_volume(volume)

    def play(self, loops):
        pygame.mixer.Channel(self.CHANNEL).play(self.SOUND, loops=loops)

    def queue(self):
        isBusy = pygame.mixer.get_busy()
        if isBusy:
            pygame.mixer.Channel(self.CHANNEL).queue(self.SOUND)
        else:
            pygame.mixer.Channel(self.CHANNEL).play(self.SOUND)

    def stop(self):
        self.SOUND.stop()