class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        s = ""
        for i, row in enumerate(self.board):
            s += f" {row[0]} | {row[1]} | {row[2]} \n"
            if i < 2:
                s += "---+---+---\n"

        return s

    def evaluate_win_state(self) -> int:
        for line in self.get_lines():
            score = sum(line)
            if score == 3:
                return 1
            if score == -3:
                return -1

        return 0

    def get_lines(self):
        board = self.board

        for row in board:
            yield row

        for c in range(3):
            yield [board[r][c] for r in range(3)]

        yield [board[i][i] for i in range(3)]
        yield [board[i][2 - i] for i in range(3)]

    def is_draw(self) -> bool:
        return self.moves_left() == 0 and self.evaluate_win_state() == 0

    def moves_left(self):
        return sum(cell == 0 for row in self.board for cell in row)

    def try_make_move(self, row, col, player) -> bool:
        if self.board[row][col] == 0:
            self.board[row][col] = player
            return True

        return False

