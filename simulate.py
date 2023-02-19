import statistics
from strategies.baseline import Baseline
from strategies.random import Random
from strategies.others import Groseille
from strategies.lookAhead import Cassis
from lib.simulation import simulate, simulate_processes


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
# functions


strategy = Baseline()


##### one party #####
# scores = simulate(strategy)


##### several parties #####
scores = simulate(strategy, iteration_nb=1000, verbose=False)
print(scores)
print("MEAN:", sum(scores) / len(scores))
print("STD:", statistics.stdev(scores))
