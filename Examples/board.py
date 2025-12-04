class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        s = ""
        for i, row in enumerate(self.board):
            s += f" {row[0]} | {row[1]} | {row[2]} \n"
            if i < 2:
                s += "---+---+---\n"

        s = s.replace("0", " ")
        s = s.replace("-1", "X")
        s = s.replace("1", "O")

        return s

    def evaluate_win_state(self) -> int:

    # def evaluate_win_state(self) -> int:
    #     for scoring_line in self.get_scoring_lines():
    #         score = sum(scoring_line)
    #         if score == 3:
    #             return 1
    #         if score == -3:
    #             return -1
    #
    #     return 0
    #
    # def get_scoring_lines(self):
    #     board = self.board
    #
    #     for row in board:
    #         yield row
    #
    #     for c in range(3):
    #         yield [board[r][c] for r in range(3)]
    #
    #     yield [board[i][i] for i in range(3)]
    #     yield [board[i][2 - i] for i in range(3)]

    def is_draw(self) -> bool:
        return self.moves_left() == 0 and self.evaluate_win_state() == 0

    def moves_left(self) -> int:
        return sum(cell == 0 for row in self.board for cell in row)

    def try_make_move(self, row, col, player) -> bool:
        if self.board[row][col] == 0:
            self.board[row][col] = player
            return True

        return False