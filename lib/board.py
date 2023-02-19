import random
from lib.utils import (
    get_tiles,
    get_lines,
    get_vertical_lines,
    get_diagonal_lines_1,
    get_diagonal_lines_2,
)
# from scipy.stats import binom


class Board:
    """build a Take It Easy board, ready to use.

    Several getter and setter are provided to update the board according to the Take It Easy rules.
    Useful functions are provided, for example to count the points of the board.
    """
    def __init__(self) -> None:

        self.tiles = get_tiles()  # get all 27 tiles of the game

        self.board = [
            ("000")
        ] * 19  # There are 19 positions on a Take It Easy board, of course. `000` means "empty position"

    ######################################################################
    # Tiles management

    def get_tiles(self) -> list:
        """return the remaining tiles from `self.tiles`
		"""
        return self.tiles

    def set_tile(self, tile: str, position: int) -> None:
        """set tile `tile` on position `position`

		If `position` is already taken, put `tile` on the first empty position
		"""
        if tile in self.tiles:
            self.tiles.remove(tile)
        if self.board[position] == "000":
            self.board[position] = tile
        else:
            self.board[self.get_empty_position()] = tile

    def pop_tile(self) -> str:
        """pop a random tile from `self.tiles`
		"""
        random_item_index = random.randint(0, len(self.tiles) - 1)
        return self.tiles.pop(random_item_index)

    ######################################################################
    # Board management

    def get_empty_position(self):
        """return the first empty position
		"""
        return self.board.index("000")

    def get_count_empty_positions(self):
        """count number of empty position left
		"""
        return all([elem == "000" for elem in self.board])
    
    def is_full(self):
        return not any([elem == "000" for elem in self.board])

    def get_empty_positions(self) -> list:
        """return all empty positions on `self.board`
		"""
        return [i for i in range(len(self.board)) if self.board[i] == "000"]

    def will_create_unique_dependency(self, tile: str, position: int) -> bool:
        """return true if the tile `tile` on the position `position` will create a unique dependency

		Will we create a hard dependency by putting `tile` on `position` ?
		"""
        # hard to calculate... ToDo
        return False

    def get_informations(self, tile: str, position: int, line: int = None):
        """return informations if you put the tile `tile` on position `position`
		"""

        lines = []
        for line, _line in enumerate(get_lines(position)):
            empty = 0
            same = 0
            different = 0
            for _tile in _line:
                if self.board[_tile] == "000":
                    empty += 1
                elif self.board[_tile][line] == tile[line]:
                    same += 1
                else:
                    different += 1
            lines.append([empty, same, different])

        return lines

    def print(self, verbose: bool = True) -> None:
        """print the CURRENT board
		"""
        if verbose:
            print("BOARD:")
        if verbose:
            print("---------------")
        print("      " + self.board[7])
        print("   " + self.board[3] + "   " + self.board[12])
        print(self.board[0] + "   " + self.board[8] + "   " + self.board[16])
        print("   " + self.board[4] + "   " + self.board[13])
        print(self.board[1] + "   " + self.board[9] + "   " + self.board[17])
        print("   " + self.board[5] + "   " + self.board[14])
        print(self.board[2] + "   " + self.board[10] + "   " + self.board[18])
        print("   " + self.board[6] + "   " + self.board[15])
        print("      " + self.board[11])
        if verbose:
            print("---------------")

    def get_points(self) -> int:
        """return total points of the CURRENT board
		"""

        def _points_on_line(elem, nb):
            total = 0
            c = [self.board[i] for i in elem]
            a = set.intersection(*map(set, c))
            if nb in a:
                total += len(elem) * int(nb)
            return total

        reward = 0
        for nb in ["1", "5", "9"]:
            reward += sum([_points_on_line(elem, nb) for elem in get_vertical_lines()])
        for nb in ["2", "6", "7"]:
            reward += sum(
                [_points_on_line(elem, nb) for elem in get_diagonal_lines_1()]
            )
        for nb in ["3", "4", "8"]:
            reward += sum(
                [_points_on_line(elem, nb) for elem in get_diagonal_lines_2()]
            )

        return reward

    ######################################################################
    # Probabilities calculation. In development

    def probability_to_get_number(self, number: str):
        """return probability to get this number

		number: str. Can be composed of 1, 2 or 3 digit.
		"""
        tot = 0
        number = number.split()

        for pion in self.pions:
            tot += all([digit in pion] for digit in number)
        return tot / len(self.pions)

    # def chance_of_having_at_least_n_time_this_number(self, i, n):
    #     tot = 0
    #     for pion in self.pions:
    #         if str(i) in pion:
    #             tot += 1

    #     coup_restant = 19 - len(self.pions)

    #     if tot == 0 or n > coup_restant:
    #         return 0

    #     return binom.cdf(n, coup_restant, self.chances_of_tirer_this_number(i))
