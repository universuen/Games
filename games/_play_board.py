from abc import abstractmethod
from threading import Thread

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class PlayBoard:
    def __init__(self, board: np.ndarray):
        # validity check
        assert len(board.shape) == 2, "A 2-dimension array in required."
        self.board = board

    @abstractmethod
    def _step(self):
        """
        This method is used to update the play board.
        """
        pass

    def run(
            self,
            interval=200,
    ):
        fig, ax = plt.subplots()
        mat = ax.matshow(self.board)
        plt.axis('off')

        def update_plot(frame):
            self._step()
            mat.set_data(self.board)
            return mat,

        _ = animation.FuncAnimation(fig, update_plot, blit=True, interval=interval)
        plt.show()

    def fast_run(
            self,
            interval=200,
    ):

        def update_board():
            while True:
                self._step()

        fig, ax = plt.subplots()
        mat = ax.matshow(self.board)
        plt.axis('off')

        def update_plot(frame):
            mat.set_data(self.board)
            return mat,

        Thread(target=update_board, daemon=True).start()
        _ = animation.FuncAnimation(fig, update_plot, blit=True, interval=interval, cache_frame_data=False)
        plt.show()

