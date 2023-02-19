from lib.strategy import Strategy
from lib.board import Board
import copy
from multiprocessing import Pool
import os

def _simulate(strategie: Strategy, plateau: Board = None, verbose=False):
    if not plateau:
        plateau = Board()
    plateau = copy.deepcopy(plateau)
    # random.shuffle(plateau.pions)
    while plateau.get_empty_positions():
        random_pion = plateau.pop_tile()

        position = strategie.get_move(plateau, random_pion)

        if verbose:
            print(random_pion, "=>", position)

        plateau.set_tile(random_pion, position)

        if verbose:
            print()

    if verbose:
        plateau.print()

    score = plateau.get_points()

    if verbose:
        print("SCORE:", score)

    return score


def simulate(
    strategie: Strategy,
    plateau: Board = None,
    iteration_nb: int = 1,
    verbose: bool = True,
    verbose_loop=True,
):
    scores = []
    for i in range(iteration_nb):
        if verbose_loop:
            print(i / iteration_nb)

        res = _simulate(strategie, plateau, verbose)

        scores.append(res)

    return scores


def simulate_processes(
    strategie: Strategy,
    plateau: Board = None,
    iteration_nb: int = 1,
    verbose: bool = False,
    verbose_loop: bool=False,
):
    tasks = [(strategie, plateau, int(iteration_nb / os.cpu_count()), verbose, verbose_loop)] * os.cpu_count()
    with Pool() as p:
        scores = p.starmap(simulate, tasks)
        return [item for sublist in scores for item in sublist]