#!/bin/python3

import os
import sys

memo_reachable = {}
memo_not_reachable = {}

def is_reachable2(start_city, curr_city, fuel, N, C, a, b):
    fuel = min(fuel+a[curr_city], C)
    if b[curr_city] > fuel:
        return 0
    next_city = (curr_city + 1) % N
    if next_city == start_city:
        return 1
    remaining_fuel = fuel - b[curr_city]
    if curr_city in memo_reachable:
        if fuel > memo_reachable[curr_city]:
            return 1
    if curr_city in memo_not_reachable:
        if fuel < memo_not_reachable[curr_city]:
            return 0
    reach = is_reachable(start_city, next_city, remaining_fuel, N, C, a, b)
    if reach:
        memo_reachable[curr_city] = fuel
        return 1
    else:
        memo_not_reachable[curr_city] = fuel
        return 0


def lookup_memo(curr_city, fuel):

    if curr_city in memo_reachable:
        if fuel > memo_reachable[curr_city]:
            return 1
    if curr_city in memo_not_reachable:
        if fuel < memo_not_reachable[curr_city]:
            return 0
    return None


def is_reachable(start_city, curr_city, fuel, N, C, a, b):

    # Record amount of fuel in tank at each city
    fuel_dict = dict()
    found_memo = False
    while True:
        memo_val = lookup_memo(curr_city, fuel)
        if memo_val is not None:
            found_memo = True
            return_val = 0
            break
        fuel_dict[curr_city] = fuel
        # Fill up tank with fuel
        fuel = min(fuel+a[curr_city], C)
        # Not enough fuel to go to next city; exit loop
        if b[curr_city] > fuel:
            return_val = 0
            break
        # Index for next city
        next_city = (curr_city + 1) % N
        # We made it back to the beginning!
        if next_city == start_city:
            return_val = 1
            break
        # Use remaining fuel to get to next city
        fuel = fuel - b[curr_city]
        curr_city = next_city

    # Update memoization dictionary with fuel values
    if not found_memo:
        if return_val:
            memo_reachable.update(fuel_dict)
        else:
            memo_not_reachable.update(fuel_dict)

    return return_val


def read_input_file(filename):
    with open(filename, 'r') as f:
        arr = f.readlines()
    arr = [list(map(int, x.rstrip().split())) for x in arr]
    [N, C] = arr[0]
    a = arr[1]
    b = arr[2]
    return [N, C, a, b]

#
# Complete the travelAroundTheWorld function below.
#
def travelAroundTheWorld(a, b, c):
    #
    # Write your code here.
    #
    print(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nc = input().split()
    n = int(nc[0])
    c = int(nc[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = travelAroundTheWorld(a, b, c)
    fptr.write(str(result) + '\n')
    fptr.close()

