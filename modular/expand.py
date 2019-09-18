import numpy as np

'''
Helper functions to help with expand()
(a) str_to_matrix()
(b) matrix_to_str()
(c) get_zero_index()
'''
def str_to_matrix(state):
    k = 0;
    mat = np.zeros((3, 3), dtype=np.int32)
    for i in range(3):
        for j in range(3):
            mat[i][j] = state[k]
            k += 1
    return mat

def matrix_to_str(mat):
    s = ""
    for t in mat.reshape(9,):
        s += (str)(t)
    return s

def get_zero_index(state):
    ind = 0
    for ch in state:
        if(ch=='0'):
            return ind
        ind += 1

'''
expands current state by sliding '0'
tile in all directions, if possible. 
'''
def expand(state):

    # neighbour configurations
    neighbours = []

    # create matrix
    mat = str_to_matrix(state)

    # find index of '0'
    index = get_zero_index(state)
    
    # row and col index of '0'
    i = (int)(index / 3) # row
    j = index % 3; # col

    # move up if possible
    if(i!=0):
        temp_mat = np.copy(mat)
        temp_mat[i][j] = temp_mat[i-1][j]
        temp_mat[i-1][j] = 0
        state = matrix_to_str(temp_mat)
        neighbours.append(state)

    # move down if possible
    if(i!=2):
        temp_mat = np.copy(mat)
        temp_mat[i][j] = temp_mat[i+1][j]
        temp_mat[i+1][j] = 0
        state = matrix_to_str(temp_mat)
        neighbours.append(state)

    # move left if possible
    if(j!=0):
        temp_mat = np.copy(mat)
        temp_mat[i][j] = temp_mat[i][j-1]
        temp_mat[i][j-1] = 0
        state = matrix_to_str(temp_mat)
        neighbours.append(state)

    # move right if possible
    if(j!=2):
        temp_mat = np.copy(mat)
        temp_mat[i][j] = temp_mat[i][j+1]
        temp_mat[i][j+1] = 0
        state = matrix_to_str(temp_mat)
        neighbours.append(state)

    return neighbours


if __name__ == '__main__':
    """ HELPER test """
    state = '852031764'
    print(f"original state = {state}")
    index = get_zero_index(state)
    print(f"index of zero = {index}")
    mat = str_to_matrix(state)
    print(mat)
    # moving 0 upwards
    mat[1][0], mat[0][0] = mat[0][0], mat[1][0],
    print("After moving 0 up")
    print(mat)
    new_state = matrix_to_str(mat)
    print(f"new state = {new_state}")

    """ EXPAND test """
    state = '852031764' 
    neighbours = expand(state)
    print(f"state = {state}")
    print(f"neighbours = ",neighbours)