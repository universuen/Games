from games._play_board import PlayBoard

import numpy as np


class LifeGame(PlayBoard):
    def __init__(self,board: np.ndarray,):
        super().__init__(board)
        assert self._board_validity is True, "The value in the board should only be 0 or 1."

    @property
    def _board_validity(self) -> bool:
        for row in self.board:
            for value in row:
                if value not in (0, 1):
                    return False
        return True

    def _get_neighbour_num(self, i, j):
        up = (i - 1) % self.board.shape[0]
        down = (i + 1) % self.board.shape[0]
        left = (j - 1) % self.board.shape[1]
        right = (j + 1) % self.board.shape[1]
        return sum([
            self.board[up][left],
            self.board[up][j],
            self.board[up][right],
            self.board[i][left],
            self.board[i][right],
            self.board[down][left],
            self.board[down][j],
            self.board[down][right]
        ])

    def _step(self):
        board = self.board.copy()
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                neighbour_num = self._get_neighbour_num(i, j)
                if neighbour_num < 2 or neighbour_num > 3:
                    board[i][j] = 0
                elif neighbour_num == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = value
        self.board = board
