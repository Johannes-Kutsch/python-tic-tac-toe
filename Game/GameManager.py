import time
import sys

from colorama import Fore
from colorama import Style

from ColorManager import ColorManager
from AIManager import AIManager
from Utils import Utils
from Board import Board
from PlayerManager import PlayerManager


class GameManager:
    def __init__(self, sound_manager):
        player_1_name = input(f"{ColorManager.get_player_color(1)}Player 1{Style.RESET_ALL}, please enter your name: ")
        player_2_name = input(f"{ColorManager.get_player_color(-1)}Player 2{Style.RESET_ALL}, please enter your name: ")
        Utils.clear_console()

        self.sound_manager = sound_manager
        self.playerManager = PlayerManager(player_1_name, player_2_name)
        self.board = Board()

    def run_game(self):
        print(f"\n{self.playerManager.get_active_player_name()} starts the game!\n")
        self.print_colored_board()

        while self.board.moves_left() > 0:
            if self.playerManager.is_active_player_ai():
                self.make_ai_move()
            else:
                self.make_move()
            self.print_colored_board()

            win_state = self.board.evaluate_win_state()
            if win_state != 0:
                self.print_win_message(win_state)
                return

            self.playerManager.switch_active_player()

        self.print_draw_message()

    def print_colored_board(self):
        print(self.board.get_board_string(ColorManager.get_player_color(1),
              ColorManager.get_player_color(-1)))

    def make_move(self):
        while True:
            player_input = self.get_valid_input()

            if self.board.try_make_move(int(player_input[0])-1, int(player_input[-1])-1, self.playerManager.get_active_player_id()):
                Utils.clear_console()
                self.sound_manager.play("Move.wav")
                print(f"\n{self.playerManager.get_active_player_color()}{self.playerManager.get_active_player_name()} is making a move to {player_input[0]}:{player_input[-1]}:...\n")
                break
            else:
                print(f"{ColorManager.get_error_color()}The cell {player_input[0]}:{player_input[-1]} is already taken. Try again.{Style.RESET_ALL}")

    def make_ai_move(self):
        sys.stdout.write(f"calculating move for {self.playerManager.get_active_player_name()}.")
        sys.stdout.flush()
        time.sleep(0.33)
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.33)

        while True:
            move = AIManager.get_next_move(self.board.board_state, self.playerManager.get_active_player_id())

            if self.board.try_make_move(move[0], move[1], self.playerManager.get_active_player_id()):
                Utils.clear_console()
                self.sound_manager.play("Move.wav")
                print(f"\n{self.playerManager.get_active_player_color()}{self.playerManager.get_active_player_name()} is making a move to {move[0]+1}:{move[1]+1}:...\n")
                break
            else:
                print(f"{ColorManager.get_error_color()}The cell {move[0]+1}:{move[1]+1} is already taken. Try again.{Style.RESET_ALL}")

    def get_valid_input(self):
        input_prompt = self.playerManager.get_active_player_name() + " to make a move, please enter cell and row (e.g. 1 2): "

        while True:
            string_input = (input(input_prompt).strip().lower()
                            .replace(" ", "")
                            .replace(":", "")
                            .replace("-", ""))
            if self.is_input_valid(string_input):
                return string_input

            self.print_error_message("Invalid input! Enter two numbers between 1 and 3, e.g. '1 3'.")

    def ask_for_restart(self):
        while True:
            input_string = input("\n🔁 Do you want to restart the game? (y/n): ").strip().lower()

            if input_string == "y":
                self.board = Board()
                Utils.clear_console()
                return True
            elif input_string == "n":
                return False

            self.print_error_message("Invalid input. Try again.")

    def print_win_message(self, win_state):
        self.sound_manager.play("Win.ogg")
        win_message = f"   {self.playerManager.get_player_name(win_state, False)} WINS!   "
        print(ColorManager.get_player_color(win_state) + "╔" + "═" * len(win_message) + "╗")
        print(f"║{win_message}║")
        print("╚" + "═" * len(win_message) + f"╝{Style.RESET_ALL}")

    def print_draw_message(self):
        self.sound_manager.play("Win.ogg")
        print(f"{Fore.YELLOW}╔═══════════════════╗")
        print(f"║   IT'S A DRAW!    ║")
        print(f"╚═══════════════════╝{Style.RESET_ALL}")

    def print_error_message(self, message):
        self.sound_manager.play("Error.wav")
        print(f"{ColorManager.get_error_color()}" + message + Style.RESET_ALL)

    @staticmethod
    def is_input_valid(string_input):
        valid_inputs = ["1", "2", "3"]
        return len(string_input) == 2 and string_input[0] in valid_inputs and string_input[-1] in valid_inputs