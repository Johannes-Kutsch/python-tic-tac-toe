import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

import time
import sys
import argparse

from SoundManager import SoundManager
from Utils import Utils
from GameManager import GameManager

class Main:
    def __init__(self):
        self.sound_manager = SoundManager()
        Utils.clear_console()

        self.sound_manager.play("Background.wav", 0.3, -1)

    def game_loop(self):
        game_manager = GameManager(self.sound_manager)

        while True:
            game_manager.run_game()
            if not game_manager.ask_for_restart():
                break

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
        self.typewriter("Nazila", blue, delay=0.04)
        self.typewriter("Nate", blue, delay=0.04)
        self.typewriter("Patricya", blue, delay=0.04)
        self.typewriter("Johannes", blue, delay=0.04)
        self.typewriter("and the other Johannes", blue, delay=0.04)

        print()
        time.sleep(0.4)

        self.typewriter("Rules:")
        time.sleep(0.2)
        self.typewriter("- 2 Players take turns putting their marks (X or O) in empty squares on a 3x3 grid", delay=0.02)
        time.sleep(0.2)
        self.typewriter("- The first player to get 3 of their marks in a row (horizontally, vertically or diagonally) is the winner", delay=0.02)
        time.sleep(0.2)
        self.typewriter("- When all 9 squares are full, the game ends with a tie", delay=0.02)
        time.sleep(0.2)
        self.typewriter("- Name a player \"AI\" to let a min-max algorithm take over", delay=0.02)
        time.sleep(0.2)
        print()



parser = argparse.ArgumentParser(
    description="Starts the game and provides optional command-line flags."
)

parser.add_argument(
    "--skip-welcome",
    action="store_true",
    help="Skips the welcome message"
)

args = parser.parse_args()

main = Main()

if not args.skip_welcome:
    main.welcome_message()

main.game_loop()