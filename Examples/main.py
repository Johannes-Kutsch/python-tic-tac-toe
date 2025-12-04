from Examples.board import Board

board = Board()
print(repr(board))
board.try_make_move(0, 0, -1)
print(repr(board))
board.try_make_move(0, 1, 1)
print(repr(board))