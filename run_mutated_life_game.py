from games.mutated_life_game import MutatedLifeGame
from games.utils import generate_random_board

if __name__ == '__main__':
    MutatedLifeGame(
        generate_random_board(128, 256, 0.1),
        1e-5,
    ).run(
        interval=30
    )
