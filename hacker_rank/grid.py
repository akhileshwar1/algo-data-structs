import math
import os
import random
import re
import sys


def gridChallenge(grid):
    for i in range(len(grid)):
        if(sorted(grid[i] == 0):
           grid[i] = insertion_sort(grid[i])

    for i in range(len(grid)):
        lst = [0 for i in range(len(grid))]
        for j in range(len(grid)):
            lst[i] = grid[j][i]
            res = sorted(lst)
            if(res == 0):
                return 'No'
    return 'Yes'



def insertion_sort(lst):
    for i in range(len(lst)):
        min = lst[i]
        index = i
        for j in range(i+1, len(lst)):
            if(lst[j] < min):
                min = lst[j]
                index = j
        temp = lst[i]
        lst[i] = min
        lst[index] = temp
    return lst


def sorted(lst):
    for i in range(len(lst)):
        if(lst[i+1] < lst[i]):
            return 0
    return 1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
