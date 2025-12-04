from GameManager import GameManager
import pygame

gameManager = GameManager()

pygame.mixer.init()
sound = pygame.mixer.Sound("Error.wav")
sound.play()

while True:
    gameManager.run_game()
    if not gameManager.ask_for_restart():
        break