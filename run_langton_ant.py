from games.langton_ant import LangtonAnt
from games.utils import generate_random_board

if __name__ == '__main__':
    LangtonAnt(
        generate_random_board(512, 1024, 0),
    ).fast_run(
        interval=30
    )
