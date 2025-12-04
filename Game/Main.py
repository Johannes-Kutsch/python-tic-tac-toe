import pygame
import time
import sys

from Utils import Utils
from GameManager import GameManager

class Main:
    def __init__(self):
        Utils.clear_console()

    @staticmethod
    def game_loop():
        game_manager = GameManager()

        while True:
            game_manager.run_game()
            if not game_manager.ask_for_restart():
                break
#pygame.mixer.init()
#sound = pygame.mixer.Sound("Error.wav")
#sound.play()

#sounds for: move, error, win, draw
#better messages for rules & errors

    @staticmethod
    def typewriter(text, color="", delay=0.03):
        for char in color + text + "\033[0m":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def welcome_message(self):
        orange = "\033[38;5;208m"
        blue = "\033[38;5;75m"
        red = "\033[38;5;196m"

        self.typewriter("Tic Tac Toe", orange)
        print()
        time.sleep(0.4)
        self.typewriter("by", blue)
        self.typewriter("Nazila", blue)
        self.typewriter("Nate", blue)
        self.typewriter("Patricya", blue)
        self.typewriter("Johannes", blue)
        self.typewriter("and the other Johannes", blue)

        print()
        time.sleep(0.4)

        self.typewriter("Rules:")
        self.typewriter("- 2 Players take turns putting their marks (X or O) in empty squares on a 3x3 grid")
        self.typewriter("- The first player to get 3 of their marks in a row (horizontally, vertically or diagonally) is the winner")
        self.typewriter("- When all 9 squares are full, the game ends with a tie")
        print()

main = Main()
main.welcome_message()
main.game_loop()