import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    initial = [i + 1 for i in range(len(q))]
    i = len(q) - 1
    count = 0
    while i > 0:
        if(initial == q):
            return count
        elif(initial[i] == q[i-1]):
            initial = swap(initial, q, i, 1)
            count = count + 1
            i = i - (1+1)
        elif(initial[i] == q[i-2]):
            initial = swap(initial, q, i, 2)
            count = count + 2
            i = i - 3
        else:
            return 'Too chaotic'
    return count


def swap(initial, q, i, j):
    for k in range(1, j+1):
        temp = initial[i-1]
        initial[i-1] = initial[i]
        initial[i] = temp
        i = i - 1
    return initial


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

