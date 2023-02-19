# Take It Easy

An implementation of the boardgame Take It Easy, with several intelligent algorithms implemented.

In this repository you will find:
- an environment to simulate the boargame Take It Easy
- several strategies that tries to achieve the best score


## The game

Take It Easy is an abstract strategy board game created by Peter Burley around 1983. You can find a description of the game on [Wikipedia](https://en.wikipedia.org/wiki/Take_It_Easy_(game)) or the rules [here](http://www.gamecabinet.com/rules/TakeItEasy.html).


## Demo

You can find an online demo on [replit](https://replit.com/@LeonDavidovski/CloseTrustworthyFacts#main.py).


## Usage/Examples

```python
from lib.board import Board
from strategies.baseline import Baseline

board = Board()
strategy = Baseline()

while not board.is_full():
    user_entry = input("> ")

    position = strategy.get_move(board, user_entry)

    board.set_tile(user_entry, position)

board.print()
print(f"Final score: {board.get_points()}")
```

## Benchmark

Benchmark of different implemented strategies.

| Strategy     |   Average score (+/- std)  | 
| :----------- |:--------------------------:|
| Random       | 11 (+/- 15)                |
| Baseline     | 130 (+/- 29)               |
| Groseille    | 144 (+/- 30)               |
| Cassis       | 170 (+/- 30)               |


## Documentation

### Environment

The `Board` class encapsulate all the logic of the boardgame, providing high level functions to focus just on your strategy.


### Strategy

Inherit from the class `Strategy` to start developping your strategy. Basically, you just have to override the `gain` function, which calculate the number of points for a given position.



## Fun facts

- The highest score possible is 307 points, and there are 16 different ways of achieving it.
- There are exactly 270.061.246.290.137.718.980.608 possible unique final position.
