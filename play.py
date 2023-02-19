from lib.board import Board
from strategies.others import Groseille

##################################################################
"""
Remainder of the board representation:

		7
	3		12
0		8		16
	4		13
1		9		17
	5		14
2		10		18
	6		15
		11

Strategies: Random() < Baseline() < Groseille() < Cassis()
"""
##################################################################


##################################################################
# Variables
board = Board()
strat = Groseille()

##################################################################
# Game

print()
print("#--------------------------------------#")
print("# Take It Easy boardgame, coded by L-D #")
print("#--------------------------------------#")
print()

print("Rules: write the tile to place.")
print("Help can be obtained by typing `help`")
print()

print("Available tiles:", ", ".join(board.get_tiles()))
print()

while True:
    # get user input
    user_entry = input("> ")

    # print board if asked
    if user_entry == "board":
        board.print()
        continue

    # print available tiles if asked
    if user_entry == "tiles":
        print(", ".join(board.get_tiles()))
        continue

    # print help if asked
    if user_entry == "help":
        print("\tWrite a number or one of the recognized command, then press <ENTER>.")
        print("\tAvailable commands:")
        print("\t\tboard : print current board")
        print("\t\ttiles : print available tiles")
        continue

    # check if the user input is valid
    if user_entry not in board.get_tiles():
        print("\tError in tile. Please try again.")
        continue

    # get best move according to the strategy
    position = strat.get_move(board, user_entry)

    print("\tBest position:", position)
    print()

    # set tile at position
    board.set_tile(user_entry, position)

    # if board is full, we end the game
    if not board.get_empty_positions():
        break


print("Finish!")
board.print()
print("Score:", board.get_points())
