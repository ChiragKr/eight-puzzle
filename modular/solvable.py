'''
It is not possible to solve an instance 
of 8 puzzle if number of inversions is 
odd in the input state, s.
'''

def get_inv_count(arr):
    inv_count = 0
    for i in range(9-1):
        for j in range(i+1,9):
            # Value 0 is used for empty space
            if (arr[j] and arr[i] and arr[i]>arr[j]):
                inv_count += 1
    return inv_count
  
# returns true if given 8 puzzle is solvable. 
def solvable(state):
    puzzle = [int(ch) for ch in state];
    # Count inversions in given 8 puzzle 
    inv_count = get_inv_count(puzzle); 
    return (inv_count%2==0); 
  
if __name__ == '__main__':
    state = "612305847"
    if solvable(state):
        print("Solvable")
    else :
        print("Not Solvable")