import math
# from ..utils import input_multiple, input_single


def major_final(lst):
    final = major(lst)
    if(final[0] > (len(lst)/2)):
        return 1
    else:
        return 0


def major(lst):
    if(len(lst) == 1):
        return [1, lst[0], lst]
    else:
        mid = math.floor(((len(lst) - 1) - 0)/2)
        left = major(lst[0: mid + 1])
        right = major(lst[mid + 1: len(lst)])
        return check(left, right)


def check(left, right):
    if(left[0] >= right[0]):
        count = 0
        for i in range(len(right[2])):
            if(left[1] == right[2][i]):
                count = count + 1
        return [count + left[0], left[1], left[2] + right[2]]
    else:
        count = 0
        for i in range(len(left[2])):
            if(right[1] == left[2][i]):
                count = count + 1
        return [count + right[0], right[1], right[2] + left[2]]


def input_multiple(n, e, h):
    try:
        lst = [0 for i in range(n)]
        for i in range(n):
            flag = False
            while flag is False:
                x = int(input())
                if(x >= e and x <= h):
                    lst[i] = x
                    flag = True
                else:
                    raise ValueError
        return lst
    except ValueError:
        print("please enter the value between {e} and {h}")


def input_single(e, h):
    try:
        flag = False
        while flag is False:
            x = int(input())
            if(x >= e and x <= h):
                flag = True
            else:
                raise ValueError
        return x
    except ValueError:
        print("please enter it between {e} and {h}")


if(__name__ == "__main__"):
    n = input_single(1, 10**5)
    lst = input_multiple(n, 0, 10**9)
    print(major_final(lst))
