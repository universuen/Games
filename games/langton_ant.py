from typing import Optional

import numpy as np

from games._play_board import PlayBoard


class LangtonAnt(PlayBoard):
    def __init__(
            self,
            board: np.ndarray,
            init_position: Optional[list[int]] = None,
            init_direction=0
    ):
        super().__init__(board)
        if init_position is None:
            init_position = [int(board.shape[0] / 2), int(board.shape[1] / 2)]
        self._direction = init_direction
        self._position = init_position
        self._data_board = self.board.copy()
        self.board[self._position[0]][self._position[1]] = 2

    def _step(self):
        position = self._data_board[self._position[0]][self._position[1]]
        if position == 0:
            self._direction = (self._direction + 1) % 4
            self._data_board[self._position[0]][self._position[1]] = 1
        else:
            self._direction = (self._direction - 1) % 4
            self._data_board[self._position[0]][self._position[1]] = 0
        self._move()
        self.board = self._data_board.copy()
        self.board[self._position[0]][self._position[1]] = 2

    def _move(self):
        if self._direction == 0:
            self._position[0] = (self._position[0] - 1) % self.board.shape[0]
        elif self._direction == 1:
            self._position[1] = (self._position[1] + 1) % self.board.shape[1]
        elif self._direction == 2:
            self._position[0] = (self._position[0] + 1) % self.board.shape[0]
        else:
            self._position[1] = (self._position[1] - 1) % self.board.shape[1]
