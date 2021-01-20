import numpy as np
import matplotlib.pyplot as plt
import abc


class PlayBoard:
    def __init__(self, height, width, rate):
        self._play_board = np.random.choice([1, 0], [height, width], p=[rate, 1 - rate])

    @abc.abstractmethod
    def _update(self, *args, **kwargs):
        """
        Overwrite this method!
        """
        pass

    def show(self, *args, **kwargs):
        plt.ion()
        while True:
            self._update(*args, **kwargs)
            plt.axis("off")
            plt.imshow(self._play_board)
            plt.pause(0.01)
            plt.figure(1).clear()


class LifeGame(PlayBoard):
    def __init__(self, height=100, width=200, rate=0.5):
        super().__init__(height, width, rate)

    def _update(self):
        sub_board = self._play_board.copy()
        for i in range(self._play_board.shape[0]):
            for j in range(self._play_board.shape[1]):
                up = (i - 1) % self._play_board.shape[0]
                down = (i + 1) % self._play_board.shape[0]
                left = (j - 1) % self._play_board.shape[1]
                right = (j + 1) % self._play_board.shape[1]
                count = sum([
                    self._play_board[up][left],
                    self._play_board[up][j],
                    self._play_board[up][right],
                    self._play_board[i][left],
                    self._play_board[i][right],
                    self._play_board[down][left],
                    self._play_board[down][j],
                    self._play_board[down][right]
                ])
                if self._play_board[i][j] == 0:
                    if count == 3:
                        sub_board[i][j] = 1
                else:
                    if count < 2 or count > 3:
                        sub_board[i][j] = 0
        self._play_board = sub_board


class LangDonAnt(PlayBoard):
    def __init__(self, height=50, width=100, rate=0, position=None, direction=0):
        super().__init__(height, width, rate)
        if position is None:
            position = [int(height / 2), int(width / 2)]
        self._direction = direction
        self._position = position
        self._data_board = self._play_board.copy()
        self._play_board[self._position[0]][self._position[1]] = 2

    def _update(self):
        position = self._data_board[self._position[0]][self._position[1]]
        if position == 0:
            self._direction = (self._direction + 1) % 4
            self._data_board[self._position[0]][self._position[1]] = 1
        else:
            self._direction = (self._direction - 1) % 4
            self._data_board[self._position[0]][self._position[1]] = 0
        self._move()
        self._play_board = self._data_board.copy()
        self._play_board[self._position[0]][self._position[1]] = 2

    def _move(self):
        if self._direction == 0:
            self._position[0] = (self._position[0] - 1) % self._play_board.shape[0]
        elif self._direction == 1:
            self._position[1] = (self._position[1] + 1) % self._play_board.shape[1]
        elif self._direction == 2:
            self._position[0] = (self._position[0] + 1) % self._play_board.shape[0]
        else:
            self._position[1] = (self._position[1] - 1) % self._play_board.shape[1]


class WireWorld(PlayBoard):
    def __init__(self, diagram):
        super().__init__(diagram.shape[0], diagram.shape[1], 0)
        self._play_board = diagram

    def _update(self):
        sub_board = self._play_board.copy()
        for i in range(self._play_board.shape[0]):
            for j in range(self._play_board.shape[1]):
                if self._play_board[i][j] in (1, 2):
                    sub_board[i][j] += 1
                elif self._play_board[i][j] == 3:
                    up = (i - 1) % self._play_board.shape[0]
                    down = (i + 1) % self._play_board.shape[0]
                    left = (j - 1) % self._play_board.shape[1]
                    right = (j + 1) % self._play_board.shape[1]
                    around = sum(
                            [
                                self._play_board[up][left] == 1,
                                self._play_board[up][j] == 1,
                                self._play_board[up][right] == 1,
                                self._play_board[i][left] == 1,
                                self._play_board[i][right] == 1,
                                self._play_board[down][left] == 1,
                                self._play_board[down][j] == 1,
                                self._play_board[down][right] == 1
                            ]
                    )
                    if around == 1 or around == 2:
                        sub_board[i][j] = 1
        self._play_board = sub_board
