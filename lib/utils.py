import itertools
import random


def get_tiles() -> list:
    return [
        "124",
        "123",
        "128",
        "164",
        "163",
        "168",
        "174",
        "173",
        "178",
        "524",
        "523",
        "528",
        "564",
        "563",
        "568",
        "574",
        "573",
        "578",
        "924",
        "923",
        "928",
        "964",
        "963",
        "968",
        "974",
        "973",
        "978",
    ]


def get_take_it_easy_tiles():
    """Return the 27 different tiles of the game Take It Easy
	"""

    # create list of pions
    pions = [[1, 5, 9], [2, 6, 7], [4, 3, 8]]

    pions = list(itertools.product(*pions))

    pions = ["".join([str(a) for a in z]) for z in pions]

    random.shuffle(pions)

    return pions


v_lines = [(0, 1, 2), (3, 4, 5, 6), (7, 8, 9, 10, 11), (12, 13, 14, 15), (16, 17, 18)]

d_lines_1 = [(0, 3, 7), (1, 4, 8, 12), (2, 5, 9, 13, 16), (6, 10, 14, 17), (11, 15, 18)]

d_lines_2 = [(7, 12, 16), (3, 8, 13, 17), (0, 4, 9, 14, 18), (1, 5, 10, 15), (2, 6, 11)]


def get_vertical_lines():
    return v_lines


def get_diagonal_lines_1():
    return d_lines_1


def get_diagonal_lines_2():
    return d_lines_2


def get_lines(
    position: int,
):
    """return the intercept lines of the position `position`

	position: int. 0 <= position <= 18
	"""
    if position == 0:
        return [v_lines[0], d_lines_1[0], d_lines_2[2]]
    if position == 1:
        return [v_lines[0], d_lines_1[1], d_lines_2[3]]
    if position == 2:
        return [v_lines[0], d_lines_1[2], d_lines_2[4]]
    if position == 3:
        return [v_lines[1], d_lines_1[0], d_lines_2[1]]
    if position == 4:
        return [v_lines[1], d_lines_1[1], d_lines_2[2]]
    if position == 5:
        return [v_lines[1], d_lines_1[2], d_lines_2[3]]
    if position == 6:
        return [v_lines[1], d_lines_1[3], d_lines_2[4]]
    if position == 7:
        return [v_lines[2], d_lines_1[0], d_lines_2[0]]
    if position == 8:
        return [v_lines[2], d_lines_1[1], d_lines_2[1]]
    if position == 9:
        return [v_lines[2], d_lines_1[2], d_lines_2[2]]
    if position == 10:
        return [v_lines[2], d_lines_1[3], d_lines_2[3]]
    if position == 11:
        return [v_lines[2], d_lines_1[4], d_lines_2[4]]
    if position == 12:
        return [v_lines[3], d_lines_1[1], d_lines_2[0]]
    if position == 13:
        return [v_lines[3], d_lines_1[2], d_lines_2[1]]
    if position == 14:
        return [v_lines[3], d_lines_1[3], d_lines_2[2]]
    if position == 15:
        return [v_lines[3], d_lines_1[4], d_lines_2[3]]
    if position == 16:
        return [v_lines[4], d_lines_1[2], d_lines_2[0]]
    if position == 17:
        return [v_lines[4], d_lines_1[3], d_lines_2[1]]
    if position == 18:
        return [v_lines[4], d_lines_1[4], d_lines_2[2]]
