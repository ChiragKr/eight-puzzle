1. Implement the usual A* for 8-Puzzle, with the Expand function taking a “depth” parameter- the depth to which each expand call expands.
* refer to solver.py, solvable.py and expand.py


2. Implement both the usual heuristics: tile mismatch count and manhattan distance.1
* refer to heuristic.py


3. In the main function, read the depth parameter as input, get the InitialState, and call the A* solver twice for each heuristic: once with the input depth parameter, and then again with the parameter being 1 (which is the usual Expand). Thus the total number of times that the puzzle will be solved by A* is 4.
* refer to main.py


4. Compare the results of all the four calls for at least 10 randomly generated initial states for optimality. Make sure this is done in the program itself.
* refer to random_test.txt (after running main.py)


5. Compare the computational costs (number of nodes generated and the maximum length of the
fringe throughout) of all the four calls for the different initial states.
* refer to analyse.py


for more details : https://github.com/ChiragKr/modified-astar