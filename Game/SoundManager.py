import os
import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sounds")
        print(self.base_dir)

    def play(self, name, volume=1.0, loops=0):
        sound = pygame.mixer.Sound(os.path.join(self.base_dir, name))
        sound.set_volume(volume)
        sound.play(loops)