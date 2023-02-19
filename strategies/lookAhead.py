from lib.board import Board
from lib.strategy import Strategy
from strategies.baseline import Baseline
from strategies.others import Johnny
import copy
from lib.simulation import simulate_processes, simulate

"""Strategy who simulate the futur

The gain, for a tile on a position, is the average of n parties if we set the tile on this position.
This is a simulation of n possible futures.
"""


class Cassis(Strategy):
    def __init__(self, nb_simulation_futur: int = 1000):
        Strategy.__init__(self)
        self.baseline_strategy = Baseline()
        self.nb_simulation_futur = nb_simulation_futur

    def gain(self, board: Board, tile: str, position: int) -> list:
        board = copy.deepcopy(board)

        board.set_tile(tile, position)

        scores = simulate_processes(self.baseline_strategy, board, self.nb_simulation_futur)
        
        return sum(scores) / len(scores) if scores else 0
