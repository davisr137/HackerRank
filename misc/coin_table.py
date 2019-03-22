import sys

# https://www.hackerrank.com/challenges/coin-on-the-table
  
directions = set(['L','R','U','D'])

# make move on board
def make_move(r,c,move):
    if move == 'D':
        r += 1
    elif move == 'U':
        r -= 1
    elif move == 'R':
        c += 1
    elif move == 'L':
        c -= 1
    out = [r,c]
    return(out)
    
# print the current state of the board as strings
def print_board(reach):
    for i in range(len(reach)):
        line = ''.join(str(x) for x in reach[i])
        print(line)
    
# iteratively search board 
# determine for each location the minimum number of operations needed for the 
# coin to reach the location
def search(board):
    # initialize arrays for operations, time, and visitation
    reach = [[0 for i in range(M)] for i in range(N)]
    reacht = [[0 for i in range(M)] for i in range(N)]
    visited = [[0 for i in range(M)] for i in range(N)]
    next_visit_list = list()
    total_visited = 0
    k = 0
    r = 0
    c = 0
    t = 0
    reach[r][c] = 0 
    reacht[r][c] = t
    visited[r][c] = 1
    move = board[r][c]
    next_visit_list.append(tuple([r,c]))
    [r,c] = make_move(r,c,move)
    traverse = True
    # start with top left location
    while traverse:
        t += 1
        # make sure the new location is on the board
        if r < 0  or c >= N:
            traverse = False
            continue
        if c < 0  or c >= M:
            traverse = False
            continue
        move = board[r][c]
        # do not re-visit location on first traversal
        if visited[r][c]:
            traverse = False
            continue
        reach[r][c] = k 
        reacht[r][c] = t
        visited[r][c] = 1
        total_visited += 1
        next_visit_list.append(tuple([r,c]))
        [r,c] = make_move(r,c,move)
        
    # make sure we visit all locations on the board
    while total_visited < M*N - 1:
        # increment k
        k += 1
        this_visit_list = next_visit_list
        next_visit_list = list()
        while len(this_visit_list) > 0:
            start = this_visit_list.pop()
            r = start[0]
            c = start[1]
            board_move = board[r][c]
            # enumerate possible "other" directions
            possible_moves = [x for x in directions if x not in board_move]
            for i in range(3):
                r = start[0]
                c = start[1]
                move = possible_moves[i]
                [r,c] = make_move(r,c,move)
                traverse = True
                while traverse:
                    # make sure the new location is on the board
                    if r < 0  or r >= N:
                        traverse = False
                        continue
                    if c < 0  or c >= M:
                        traverse = False
                        continue
                    move = board[r][c]
                    # check if we have visited the location before
                    if visited[r][c]:
                        if k < reach[r][c]:
                            # better solution found
                            reach[r][c] = k
                        traverse = False
                        continue
                    t = reacht[r][c] + 1
                    reach[r][c] = k 
                    reacht[r][c] = k 
                    visited[r][c] = 1
                    total_visited += 1
                    next_visit_list.append(tuple([r,c]))
                    [r,c] = make_move(r,c,move)
    # get solution
    val = reach[r_star][c_star]
    valt = reacht[r_star][c_star]
    
    if valt > K:
        if val > K:
            out1 = -1
        else: 
            out1 = 1
    else:
        out1 = val
    
    out = [val,valt]
    return(out1)
    
# parse input parameters
N,M,K = [int(q_temp) for q_temp in input().strip().split(' ')]

# initialize board
board = list()

# parse lines
for i in range(N):
    line = input().strip()
    board.append(line)
    if line.find('*') > -1:
        # found '*'
        r_star = i
        c_star = line.find('*') 

out = search(board)
print(out)
        
        
        
        
    
    
    
    
     
    