import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from heuristic import *
from solver import solver
from solvable import solvable

def analyse(initial_state, depth):

	analyse_heuristic(initial_state, depth, manhattan_distance, "manhattan")
	analyse_heuristic(initial_state, depth, tile_mismatch, "tile_mismatch")
	analyse_heuristic(initial_state, depth, lambda x:0, "no_heuristic")
	analyse_depth(initial_state)

def analyse_depth(initial_state, dlimit=30):
	print("creating frigesize_vs_depth.png...")
	print("creating iterations_vs_depth.png...")
	print("creating visited_vs_depth.png...")
	
	# Data for plotting
	depth = np.arange(1, dlimit)
	max_fringe_manhatten = []
	iteration_manhatten = []
	visited_manhatten = []
	max_fringe_tile_mismatch = []
	iteration_tile_mismatch = []
	visited_tile_mismatch = []

	for i in range(1, dlimit):
	    sl = solver()
	    path = sl.modified_astar(initial_state, manhattan_distance, i)
	    max_fringe_manhatten.append(sl.max_fringe_size)
	    iteration_manhatten.append(sl.interations)
	    visited_manhatten.append(len(sl.visited))
	    
	    sl = solver()
	    path = sl.modified_astar(initial_state, tile_mismatch, i)
	    max_fringe_tile_mismatch.append(sl.max_fringe_size)
	    iteration_tile_mismatch.append(sl.interations )
	    visited_tile_mismatch.append(len(sl.visited))

	# Fringe size vs depth	
	fig, ax = plt.subplots()
	ax.plot(depth, max_fringe_manhatten, label="manhatten")
	ax.plot(depth, max_fringe_tile_mismatch, label="tile mismatch")
	ax.set(xlabel='depth', ylabel='fringe size',
	       title=f'max fringe size for different depths (initial state = {initial_state})')
	ax.grid()
	ax.legend()
	fig.savefig("frigesize_vs_depth.png")
	print("...saved frigesize_vs_depth.png")
	# plt.show()

	# Number of Iterations vs depth
	fig, ax = plt.subplots()
	ax.plot(depth, iteration_manhatten, label="manhatten")
	ax.plot(depth, iteration_tile_mismatch, label="tile mismatch")
	ax.set(xlabel='depth', ylabel='fringe size',
	       title=f'number of iteration for different depths (initial state = {initial_state})')
	ax.grid()
	ax.legend()
	fig.savefig("iterations_vs_depth.png")
	print("...saved iterations_vs_depth.png")
	# plt.show()

	# Number of nodes visited vs depth
	fig, ax = plt.subplots()
	ax.plot(depth, visited_manhatten, label="manhatten")
	ax.plot(depth, visited_tile_mismatch, label="tile mismatch")
	ax.set(xlabel='depth', ylabel='number of nodes visited',
	       title=f'number of nodes visited for different depths (initial state = {initial_state})')
	ax.grid()
	ax.legend()
	fig.savefig("visited_vs_depth.png")
	print("...saved visited_vs_depth.png")
	# plt.show()

def analyse_heuristic(initial_state, depth, heuristic, str):
	print(f"creating {str}_depth_cmp.png...")
	# A* using prescribed heuristic
	solver11 = solver()
	solver11.modified_astar(initial_state, heuristic, depth)
	s11 = solver11.fringe_growth
	solver12 = solver()
	solver12.modified_astar(initial_state, heuristic, 1)
	s12 = solver12.fringe_growth

	# Data for plotting
	x = min(solver11.interations, solver12.interations)
	t = np.arange(x)
	fig, ax = plt.subplots()
	ax.plot(t, s11[0:x], label=f'depth = {depth}')
	ax.plot(t, s12[0:x], label='depth = 1') 
	ax.set(xlabel='interations', ylabel='fringe size',
	       title=f'Growth of fringe with {str} heuristic')
	ax.grid()
	ax.legend()
	fig.savefig(f"{str}_depth_cmp.png")
	print(f"...saved {str}_depth_cmp.png")
	# plt.show()


if __name__ == '__main__':
	print("analyse.py : computation cost analysis")
	print("(with respect to a given initial state)")
	print("... TILE LAYOUT & INPUT FORMAT ...")
	print("       0 2 5")
	print("NOTE : 6 7 1 = 025671834")
	print("       8 3 4")
	initial_state = input("enter initial state (eg. 025671834): ")
	print("       0 1 2")
	print("GOAL = 3 4 5 = 012345678")
	print("       6 7 8")
	depth = (int)(input("enter depth : "))
	analyse(initial_state, depth)