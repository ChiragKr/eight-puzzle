import random
import sys
from heuristic import *
from solver import solver
from solvable import solvable
from analyse import analyse


def display_solution(initial_state, heuristic, depth) :
    path_finder = solver()
    path = path_finder.modified_astar(initial_state, heuristic, depth)
    path_finder.stats()
    print("PATH LENGTH : ", len(path)-1, "\nPATH : ", path, "\n")


def display_all(initial_state, depth):
    # A* using manhattan_distance heuristic
    print("RESULTS FROM USING MANHATTEN HEURISTIC WITH DEPTH = ", depth)
    display_solution(initial_state, manhattan_distance, depth)    
    print("RESULTS FROM USING MANHATTEN HEURISTIC WITH DEPTH = ", 1)
    display_solution(initial_state, manhattan_distance, 1)
     
    # A* using tile mis-match heuristic
    print("RESULTS FROM USING TILE MISMATCH HEURISTIC WITH DEPTH = ", depth)
    display_solution(initial_state, tile_mismatch, depth)
    print("RESULTS FROM USING TILE MISMATCH HEURISTIC WITH DEPTH = ", 1)
    display_solution(initial_state, tile_mismatch, 1)


def main():
    print("... TILE LAYOUT & INPUT FORMAT")
    print("       0 2 5")
    print("NOTE : 6 7 1 = 025671834")
    print("       8 3 4")
    initial_state = input("enter initial state (eg. 025671834): ")
    print("       0 1 2")
    print("GOAL = 3 4 5 = 012345678")
    print("       6 7 8")
    depth = (int)(input("enter depth : "))
    display_all(initial_state, depth)

    ''' deeper analysis of initial_state ''' 
    # if(solvable(initial_state)):
    #     analyse(initial_state, depth)

    
def random_initial_state():
    tiles = ['0','1','2','3','4','5','6','7','8']
    initial_state = ''
    window = 8
    for i in range(9):
        r = random.randint(0, window)
        initial_state += tiles[r]

        temp = tiles[window]
        tiles[window] = tiles[r]
        tiles[r] = temp

        window -= 1

    return initial_state


def random_test(sample_size=10, dlimit=10):
    initial_states = set()
    while len(initial_states) < sample_size :
        state = random_initial_state()
        if(solvable(state)):
            initial_states.add(state)
     
    for initial_state in initial_states:
        depth = random.randint(1, dlimit)
        print(f"INITIAL STATE : {initial_state}")
        print(f"DEPTH VALUE : {depth}\n")      
        display_all(initial_state, depth)     
        print("\n\n\n\n")


if __name__ == '__main__':
    print("main.py : get optimal path")
    print("(for given initial state and depth value)")
    """ user's initial state """
    main()

    """ random initial states """
    print("...GENERATING RESULTS...")
    print("...writing to file 'random_test.txt'...")
    terminal = sys.stdout 
    sys.stdout = open('random_test.txt', 'w')
    random_test(sample_size=10, dlimit=10)
    sys.stdout = terminal
    print("...COMPLETED...")