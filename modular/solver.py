from collections import deque
from collections import defaultdict
from queue import PriorityQueue
from expand import expand
from solvable import solvable

class solver(object):
    
    def __init__(self):
        self.fringe = PriorityQueue()
        self.g = defaultdict(int)
        self.visited = defaultdict(bool)
        self.cameFrom = {}
        
        self.interations = 0
        self.max_fringe_size = -float('inf') 
        self.fringe_growth = []
        
    def stats(self):
        print("iterations : ", self.interations)
        print("final_fringe_size : ", self.fringe.qsize())
        print("max_fringe_size : ", self.max_fringe_size)
        print("total nodes visited : ", len(self.visited))
               
    def reconstruct_path(self, current):
        total_path = deque([current])
        while current in self.cameFrom.keys():
            current = self.cameFrom[current]
            total_path.appendleft(current)
        return total_path
    
    def modified_expand(self, S, depth):
        self.visited[S] = True  
        temp1 = deque([S])
        while depth > 0 :
            temp2 = []
            while len(temp1) :    
                C = temp1.popleft()

                if C == '012345678':
                    temp1.appendleft(C)
                    return temp1

                temp3 = filter(lambda x: not self.visited[x] 
                               or self.g[x]>self.g[C]+1, expand(C))
                temp3 = list(temp3)
                for t in temp3:
                    self.g[t] = self.g[C] + 1
                    self.cameFrom[t] = C
                    self.visited[t] = True
                temp2.extend(temp3)

            depth -= 1
            temp1 = deque(temp2)
        return temp1

    def modified_astar(self, I, h, depth, check=True):
        if(check and not solvable(I)):
            print("path does not exist")
            return []

        self.g[I] = 0  
        self.interations = 0
        S = I
        while S != "012345678" :
            temp = self.modified_expand(S, depth)
            for T in temp:
                f = self.g[T] + h(T)
                self.fringe.put((f, T)) 

            if self.fringe.qsize() > self.max_fringe_size :
                self.max_fringe_size = self.fringe.qsize()
                
            self.fringe_growth.append(self.fringe.qsize())
            
            if self.fringe.empty():
                return []

            S = self.fringe.get()[1]
            self.interations += 1

        return self.reconstruct_path("012345678")


if __name__ == '__main__':
    """ test without any heuristic """
    state = '852031764' 
    path_finder = solver()
    path = path_finder.modified_astar(state, lambda x:0, 1)
    path_finder.stats()
    print("PATH LENGTH : ", len(path)-1, "\nPATH : ", path, "\n")