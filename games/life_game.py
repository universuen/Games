from games._play_board import PlayBoard

import numpy as np


class LifeGame(PlayBoard):
    def __init__(self, board: np.ndarray, ):
        super().__init__(board)
        assert self._board_validity is True, "The value in the board should only be 0 or 1."

    @property
    def _board_validity(self) -> bool:
        for row in self.board:
            for value in row:
                if value not in (0, 1):
                    return False
        return True

    def _get_neighbour_num(self, i: int, j: int) -> int:
        return self.board[i - 1:i + 2, j - 1:j + 2].sum() - self.board[i][j]

    def _step(self):
        board = self.board.copy()
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                neighbour_num = self._get_neighbour_num(i, j)
                if neighbour_num < 2 or neighbour_num > 3:
                    board[i][j] = 0
                elif neighbour_num == 3:
                    board[i][j] = 1
        self.board = board
