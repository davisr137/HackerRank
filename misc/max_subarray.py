import sys

# https://www.hackerrank.com/challenges/maxsubarray

def search(N,a):
    # find largest non-contiguous subarray
    pos_list = [x for x in a if x >= 0]
    if len(pos_list) > 0:
        sum_nc = sum(pos_list)
    else: # all zero or negative elements
        sum_nc = max(a)
    # find largest contiguous array
    sum_to = [0]*N 
    run_sum = 0
    for i in range(N):
        run_sum += a[i]
        sum_to[i] = run_sum
    # find largest contiguous array
    sum_to = [0] + sum_to
    a = [0] + a
    left = 0
    right = 1
    sum_c = sum(a[left:right+1])
    max_left = 0
    max_right = 0
    min_seen = 0
    while right < N-1:
        right+=1
        if sum_to[right] < min_seen:
            min_seen = sum_to[right]
            left = right
        if sum_to[right+1]-sum_to[left] > sum_c:
            max_left = left
            max_right = right
            sum_c = sum_to[right+1]-sum_to[left]
    # max subset is only last element
    if a[-1] > sum_c:
        sum_c = a[-1]
    out = [sum_nc,sum_c]
    return(out)


# parse and process inputs
T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    a = [int(temp) for temp in input().strip().split(' ')]
    out = search(N,a)
    print(str(out[1])+' '+str(out[0]))
    

    
    
        
        
        
        
        
        
    
    
    
    
    
    
    