# manhatten distance sum heuristic
def manhattan_distance(state):
    ij = [0 for i in range(9)]
    for index, ch in enumerate(state):      
        i = (int)(index / 3) # row
        j = index % 3; # col
        ij[(int)(ch)] = ((i,j))
    
    dist_sum = 0
    for index in range(1,9):
        i = (int)(index / 3) # row
        j = index % 3; # col
        dx = abs(i - ij[index][0])
        dy = abs(j - ij[index][1])
        dist = dx + dy      
        dist_sum += dist
    
    return dist_sum

# tile mismatch count heuristic
def tile_mismatch(state):
    mismatch = 0
    goal = "012345678"
    for i in range(9):
        if goal[i] != state[i]:
            mismatch += 1
    return mismatch


if __name__ == '__main__':
    state = '852031764'
    print(f"state = {state}")

    """ manhatten distance test """
    md = manhattan_distance(state)
    print(f"manhattan_distance({state}) = {md}")

    """ tile mismatch test """
    tm = tile_mismatch(state)
    print(f"tile_mismatch({state}) = {tm}")
    