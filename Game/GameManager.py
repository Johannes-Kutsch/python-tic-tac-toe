from Game.Board import Board
from Game.PlayerManager import PlayerManager


class GameManager:
    def __init__(self):
        player_1_name = input("Player 1, please enter your name: ")
        player_2_name = input("Player 2, please enter your name: ")

        self.playerManager = PlayerManager(player_1_name, player_2_name)
        self.board = Board()

    def start_game(self):
        # print board state
        # get row/column input for active player
        # validate input format (if invalid display error + repeat last step)
        # try player move (if not possible display error + get new input)

        # switch player
        # repeat until win/draw

        print(repr(board))
        board.try_make_move(0, 0, -1)
        print(repr(board))
        board.try_make_move(0, 1, 1)
        print(repr(board))