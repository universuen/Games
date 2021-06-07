import random

import numpy as np

from games.life_game import LifeGame


class MutatedLifeGame(LifeGame):
    def __init__(self, board: np.ndarray, mutation_rate: float):
        super().__init__(board)
        assert mutation_rate < 1, "Mutation rate must be less than 1"
        self.mutation_rate = mutation_rate

    def _step(self):
        board = self.board.copy()
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                neighbour_num = self._get_neighbour_num(i, j)
                if neighbour_num < 2 or neighbour_num > 3:
                    board[i][j] = 0
                elif neighbour_num == 3:
                    board[i][j] = 1
                if random.random() < self.mutation_rate and value == 0:
                    board[i][j] = 1
        self.board = board
