from lib.board import Board
from lib.strategy import Strategy
from strategies.baseline import Baseline

"""Strategy based on other tiles

We compare a tile to others, and take the position where the tile is relatively the best.

Algo:
- for each position:
    - calculate score of a tile
    - calculate the average score of the rest of the tiles
    - return the difference
"""


class Groseille(Strategy):
    def __init__(self):
        Strategy.__init__(self)
        self.baseline_strategy = Baseline()

    def gain(self, board: Board, tile: str, position: int) -> list:
        score_this_tile = self.baseline_strategy.gain(board, tile, position)

        score_other_tiles = [self.baseline_strategy.gain(board, p, position) for p in board.tiles]

        score_other_tiles_mean = (
            sum(score_other_tiles) / len(score_other_tiles) if score_other_tiles else self.default_score
        )

        return score_this_tile - score_other_tiles_mean
