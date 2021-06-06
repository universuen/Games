import numpy as np


def generate_random_board(height: int, width: int, rate_of_1: float):
    return np.random.choice([1, 0], [height, width], p=[rate_of_1, 1 - rate_of_1])