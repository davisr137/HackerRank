import sys

# https://www.hackerrank.com/challenges/play-game

# recurrence: choose between taking 1, 2, 3 bricks
def search(N,a):
    # total score for optimal strategy at index
    optimal_strat = [0]*N
    # optimal number of bricks to take at each step
    optimal_take = [0]*N
    max_index = len(a) - 1 
    index = max_index    
    while index >= 0:
        # at the end of the stack
        if index == max_index:
            optimal_strat[index] = a[index]
            optimal_take[index] =  1
        # one from the end of the stack
        elif index == max_index - 1:
            if a[index+1] > 0:
                optimal_strat[index] = sum(a[index:N])
                optimal_take[index] =  2
            else:
                optimal_strat[index] = a[index]
                optimal_take[index] =  1
        # two from the end of the stack
        elif index == max_index - 2:
            take1 = a[index]
            take2 = sum(a[index:index+2])
            take3 = sum(a[index:index+3])
            move = max(take1,take2,take3)
            optimal_strat[index] = move
            if move == take1:
                optimal_take[index] = 1
            elif move == take2:
                optimal_take[index] = 2
            elif move == take3:
                optimal_take[index] = 3
        # more than two from end of stack
        else:
            # take one
            best_strat = -1000000
            best_take = 0
            for jj in range(1,4):
                imm_score = sum(a[index:index+jj])
                next_move = index+jj+optimal_take[index+jj]
                if next_move > max_index:
                    future_score = 0
                else:
                    future_score = optimal_strat[next_move]
                total_score = imm_score + future_score
                if total_score > best_strat:
                    best_strat = total_score
                    best_take = jj
            optimal_strat[index] = best_strat
            optimal_take[index] = best_take
        # decrement index
        index -= 1
    # return result of best strategy
    return(optimal_strat[0])

# parse and process inputs
T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    a = [int(temp) for temp in input().strip().split(' ')]
    out = search(N,a)
    print(out)

 
        
        
        
        
        
        
    
    
    
    
    
    
    