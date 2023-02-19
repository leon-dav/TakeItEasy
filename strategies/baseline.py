from lib.board import Board
from lib.strategy import Strategy

"""Baseline

Algo :
    - for each available position, simulate the score if we put a tile on this position.
    - score: function of number of free/occupied positions for each of the three lines of the position.
"""


class Baseline(Strategy):
    def __init__(self):
        Strategy.__init__(self)

    def gain(self, board: Board, tile: str, position: int) -> list:
        score = self.default_score

        lines_stats = board.get_informations(tile, position)

        for i, elem in enumerate(lines_stats):
            # if not, then a different number is on the line, so score is zero.
            if elem[2] == 0:
                score += int(tile[i]) * (elem[0] + elem[1])

                # bonus if we continue an existing line
                score += int(tile[i]) * elem[1] * 3

        return score
