from Board import Board
from PlayerManager import PlayerManager


class GameManager:
    def __init__(self):
        player_1_name = input("Player 1, please enter your name: ")
        player_2_name = input("Player 2, please enter your name: ")

        self.playerManager = PlayerManager(player_1_name, player_2_name)
        self.board = Board()

    def start_game(self):
        print(f"\n {self.playerManager.get_active_player_name()} starts the game!")
        print(repr(self.board))

        while True:
            print(f"\n{self.playerManager.get_active_player_name()} is making a move...")
            player_input = self.get_valid_input()
            if self.board.try_make_move(int(player_input[0])-1, int(player_input[-1])-1, self.playerManager.get_active_player_id()):
                # player Feedback invalid position
                print("Valid move!")
                break

        print(repr(self.board))
        print("Invalid position / this cell is already taken. Try again.")

        # switch player
        # repeat until win/draw



    def get_valid_input(self):
        input_prompt = self.playerManager.get_active_player_name() + " to make a move, please enter cell and row (e.g. 1 2): "

        while True:
            string_input = input(input_prompt)
            if self.is_input_valid(string_input):
                return string_input

            print("Invalid input! Enter two numbers between 1 and 3, e.g. '1 3'.")

    @staticmethod
    def is_input_valid(string_input):
        valid_inputs = ["1", "2", "3"]
        return len(string_input) > 1 and string_input[0] in valid_inputs and string_input[-1] in valid_inputs