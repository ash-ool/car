import pygame
from pygame import mixer


class SoundManager:
    def __init__(self):
        mixer.init()
        self.ss = {
            'turn': mixer.Sound("sounds/turn-1.mp3"),
            'powerUp': mixer.Sound("sounds/turn-2.mp3"),
            'click': mixer.Sound("sounds/clickBtn.wav"),
        }
        self.effectVolume = 1

    def playMusic(self):
        mixer.music.load("sounds/background-music.mp3")
        mixer.music.play(-1)

    def stopMusic(self):
        mixer.music.stop()

    def playGameOverMusic(self):
        mixer.music.load("sounds/gameover-music.mp3")
        mixer.music.play(-1)

    def play(self, key):
        self.ss[key].set_volume(self.effectVolume)
        mixer.Sound.play(self.ss[key])

    def setMusicVolume(self,volume):
        pygame.mixer.music.set_volume(volume)
    def setEffectVolume(self,volume):
        self.effectVolume = volume

    def getEffectVolume(self):
        return self.effectVolume

    def getMusicVolume(self):
        return pygame.mixer.music.get_volume()



soundManager = SoundManager()