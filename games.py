import numpy as np
import matplotlib.pyplot as plt


class PlayBoard:
    def __init__(self, height, width, rate):
        self.play_board = np.random.choice([1, 0], [height, width], p=[rate, 1 - rate])

    def update(self, *args, **kwargs):
        pass

    def show(self):
        plt.ion()
        while True:
            self.update()
            plt.axis("off")
            plt.imshow(self.play_board)
            plt.pause(0.01)
            plt.figure(1).clear()


class LifeGame(PlayBoard):
    def __init__(self, height=100, width=200, rate=0.5):
        super().__init__(height, width, rate)

    def update(self):
        copy_board = self.play_board.copy()
        for i in range(self.play_board.shape[0]):
            for j in range(self.play_board.shape[1]):
                up = (i - 1) % self.play_board.shape[0]
                down = (i + 1) % self.play_board.shape[0]
                left = (j - 1) % self.play_board.shape[1]
                right = (j + 1) % self.play_board.shape[1]
                count = self.play_board[up][left] + self.play_board[up][j] + self.play_board[up][right] \
                        + self.play_board[i][left] + self.play_board[i][right] \
                        + self.play_board[down][left] + self.play_board[down][j] + self.play_board[down][right]
                if self.play_board[i][j] == 0:
                    if count == 3:
                        copy_board[i][j] = 1
                else:
                    if count < 2 or count > 3:
                        copy_board[i][j] = 0
        self.play_board = copy_board


class LangDonAnt(PlayBoard):
    def __init__(self, height=50, width=100, rate=0.1, position=None, direction=0):
        super().__init__(height, width, rate)
        if position is None:
            position = [int(height/2), int(width/2)]
        self.direction = direction
        self.position = position
        self.data_board = self.play_board.copy()
        self.play_board[self.position[0]][self.position[1]] = 2

    def update(self):
        position = self.data_board[self.position[0]][self.position[1]]
        if position == 0:
            self.direction = (self.direction + 1) % 4
            self.data_board[self.position[0]][self.position[1]] = 1
        else:
            self.direction = (self.direction - 1) % 4
            self.data_board[self.position[0]][self.position[1]] = 0
        self._move()
        self.play_board = self.data_board.copy()
        self.play_board[self.position[0]][self.position[1]] = 2

    def _move(self):
        if self.direction == 0:
            self.position[0] = (self.position[0] - 1) % self.play_board.shape[0]
        elif self.direction == 1:
            self.position[1] = (self.position[1] + 1) % self.play_board.shape[1]
        elif self.direction == 2:
            self.position[0] = (self.position[0] + 1) % self.play_board.shape[0]
        else:
            self.position[1] = (self.position[1] - 1) % self.play_board.shape[1]



