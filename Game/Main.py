import pygame

from Utils import Utils
from GameManager import GameManager

Utils.clear_console()

gameManager = GameManager()

#pygame.mixer.init()
#sound = pygame.mixer.Sound("Error.wav")
#sound.play()

while True:
    gameManager.run_game()
    if not gameManager.ask_for_restart():
        break

