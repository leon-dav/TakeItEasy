from lib.board import Board

DEFAULT_SCORE = -1000


class Strategy:
    """Interface to implement your own strategies.

    Basically, just inherit from this class and implement the 'gain' function to get started.
    """
    def __init__(self, default_score=DEFAULT_SCORE) -> None:
        self.default_score = default_score

    def gain(self, board: Board, tile: str, position: int) -> int:
        raise "Implement it yourself!"

    def get_move(self, board: Board, tile: str) -> int:
        gains = [self.default_score for _ in range(19)]
        for position in board.get_empty_positions():
            gains[position] = self.gain(board, tile, position)

        return gains.index(max(gains))
