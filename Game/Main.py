from GameManager import GameManager


gameManager = GameManager()

while True:
    gameManager.run_game()
    if not gameManager.ask_for_restart():
        break