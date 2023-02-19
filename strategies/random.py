from lib.board import Board
from lib.strategy import Strategy

"""Random strategy

A totally random strategy
"""


class Random(Strategy):
    def __init__(self):
        Strategy.__init__(self)

    def gain(self, board: Board, tile: str, position: int) -> list:
        return 0
