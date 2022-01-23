import math
from utils.inputs import input_single, input_multiple


def invert(lst):
    if(len(lst) == 1):
        return [0, lst]
    else:
        mid = math.floor(((len(lst) - 1) - 0)/2)
        left = invert(lst[0: mid + 1])
        right = invert(lst[mid + 1: len(lst)])
        return check(left, right)


def check(left, right):
    count = 0
    for i in range(len(left[1])):
        for j in range(len(right[1])):
            if(left[1][i] >= right[1][j]):
                count = count + 1
    return [left[0] + right[0], left[1] + right[1]]


if __name__ == '__main__':
    n = input_single(1, 10**5)
    lst = input_multiple(n, 1, 10**9)
    print(invert(lst))
