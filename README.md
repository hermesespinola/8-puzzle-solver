# 8 puzzle solver

## Description
The 8-puzzle is a square board with 9 positions, filled by 8 numbered tiles and one gap. At any point, a tile adjacent to the gap can be moved into the gap, creating a new gap position. In other words the gap can be swapped with an adjacent (horizontally and vertically) tile. The objective in the game is to begin with an arbitrary configuration of tiles, and move them so as to get the numbered tiles arranged in ascending order either running around the perimeter of the board or ordered from left to right, with 1 in the top left-hand position.

This program takes a board configuration and prints to stdout:
- The **cost** of the path to the solution (number of moves).
- The **moves** made to get to the solution.
- **Number of visited** nodes at the end.
- **Running time** in seconds.
- Used **memory** (assuming each node requires only 72 bytes).

## Instructions
Here's a copy of *help* command `./8_puzzle.py -h`:
```
usage: 8_puzzle.py [-h] [-f FILE | -b BOARD] [-s SEPARATOR] [-m METHOD] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  set input file path
  -b BOARD, --board BOARD
                        set board input text
  -s SEPARATOR, --separator SEPARATOR
                        set separator for each element of board input
  -m METHOD, --method METHOD
                        'bfs', 'dfs', or 'a_star'
  -d, --debug           enable debugging logs
```

Execute the python script, by default it reads a file named `board.txt`. You can change
the file name by providing it with the `-f` flag, or, set the input directly by using
the flag `-b`.

#### Input
The input must be a list of 9 numbers, separated by a space (or the separator indicated by the -s parameter). The input should include a `0`, which indicates the gap of the puzzle.

Some examples:

`python3 8_puzzle.py -b '7 2 4 5 0 6 8 3 1'`

`python3 8_puzzle.py -f ./inputs/other_board.txt -s ';'`

`python3 8_puzzle.py -s ',' -b '7, 2, 4, 5, 0, 6, 8, 3, 1' -m 'a_star'`

## Test
```bash
➜ python3 8_puzzle.py -f ./board.txt -m a_star
Cost of path: 20
Path to goal: down, right, up, left, left, up, right, right, down, left, down, left, up, right, up, left, down, right, right, down
# visited nodes: 282
Running time (seconds): 0.01112909
Used memory: If each node requires only 72 bytes, 53712
```
