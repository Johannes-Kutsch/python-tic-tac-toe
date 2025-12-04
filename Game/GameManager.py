from Board import Board
from PlayerManager import PlayerManager


class GameManager:
    def __init__(self):
        player_1_name = input("Player 1, please enter your name: ")
        player_2_name = input("Player 2, please enter your name: ")

        self.playerManager = PlayerManager(player_1_name, player_2_name)
        self.board = Board()

    def run_game(self):
        print(f"\n {self.playerManager.get_active_player_name()} starts the game!")
        print(repr(self.board))

        while self.board.moves_left() > 0:
            self.make_move()
            print(repr(self.board))

            win_state = self.board.evaluate_win_state()
            if win_state != 0:
                print(self.playerManager.get_player_name(win_state) + " won")
                return

            self.playerManager.switch_active_player()

        print("Its a Draw")

    def make_move(self):
        while True:
            player_input = self.get_valid_input()

            if self.board.try_make_move(int(player_input[0])-1, int(player_input[-1])-1, self.playerManager.get_active_player_id()):
                print(f"\n{self.playerManager.get_active_player_name()} is making a move...")
                break
            else:
                print("Invalid position / this cell is already taken. Try again.")

    def get_valid_input(self):
        input_prompt = self.playerManager.get_active_player_name() + " to make a move, please enter cell and row (e.g. 1 2): "

        while True:
            string_input = (input(input_prompt)
                            .replace(" ", "")
                            .replace(":", "")
                            .replace("-", ""))
            if self.is_input_valid(string_input):
                return string_input

            print("Invalid input! Enter two numbers between 1 and 3, e.g. '1 3'.")

    def ask_for_restart(self):
        while True:
            input_string = input("Do you want to restart? (y/n)")

            if input_string == "y":
                self.board = Board()
                return True
            elif input_string == "n":
                return False

    @staticmethod
    def is_input_valid(string_input):
        valid_inputs = ["1", "2", "3"]
        return len(string_input) == 2 and string_input[0] in valid_inputs and string_input[-1] in valid_inputs