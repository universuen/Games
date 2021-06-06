from games.mutated_life_game import MutatedLifeGame
from games.utils import generate_random_board

if __name__ == '__main__':
    MutatedLifeGame(
        generate_random_board(90, 160, 0.6),
        0.1,
    ).run(
        interval=30
    )
