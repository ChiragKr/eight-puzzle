# Eight Puzzle
The 8 puzzle problem is an instance of the more general [Sliding Puzzle](https://en.wikipedia.org/wiki/Sliding_puzzle) Problem.
This puzzle can be easily solved using the A* Search algorithm. However, here we attempt to improve over this by modifying the A* search algorithm to use a local, limited depth, Breadth First Search to boost search speeds. We further analyze the performance overhead of this in terms of the extra space needed to store the additional elements (found in the local BFS)

Refer to [this repository](https://github.com/ChiragKr/modified-astar) in order to better visualize how the "local" BFS combined with "global" A* can improve search efficiency.
