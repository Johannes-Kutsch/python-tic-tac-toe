import math
import random
from typing import List, Tuple, Optional

class AIManager:
    @staticmethod
    def get_next_move(board: List[List[int]], player: int) -> Tuple[int, int]:
        opponent = -player
        best_score = -math.inf
        best_moves = []

        for r in range(3):
            for c in range(3):
                if board[r][c] == 0:
                    board[r][c] = player
                    score = AIManager._minimax(board, player, opponent, False, -math.inf, math.inf)
                    board[r][c] = 0

                    if score > best_score:
                        best_score = score
                        best_moves = [(r, c)]
                    elif score == best_score:
                        best_moves.append((r, c))

        return random.choice(best_moves)

    @staticmethod
    def _minimax(board, player, opponent, is_maximizing, alpha, beta):
        winner = AIManager._check_winner(board, player, opponent)
        if winner is not None:
            return winner

        if AIManager._is_full(board):
            return 0

        if is_maximizing:
            best = -math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = player
                        best = max(best, AIManager._minimax(board, player, opponent, False, alpha, beta))
                        board[r][c] = 0
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            return best
            return best
        else:
            best = math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = opponent
                        best = min(best, AIManager._minimax(board, player, opponent, True, alpha, beta))
                        board[r][c] = 0
                        beta = min(beta, best)
                        if beta <= alpha:
                            return best
            return best

    @staticmethod
    def _check_winner(board, player, opponent) -> Optional[int]:
        lines = []

        lines.extend(board)
        lines.extend([[board[r][c] for r in range(3)] for c in range(3)])

        lines.append([board[i][i] for i in range(3)])
        lines.append([board[i][2 - i] for i in range(3)])

        for line in lines:
            if sum(line) == 3 * player:
                return 10
            if sum(line) == 3 * opponent:
                return -10

        return None

    @staticmethod
    def _is_full(board) -> bool:
        return all(board[r][c] != 0 for r in range(3) for c in range(3))