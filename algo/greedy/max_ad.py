import math


def MaxAd(ads, slots):
    revenue = 0
    ads = merge_sort(ads)
    slots = merge_sort(slots)
    for i in range(len(slots)):
        revenue = revenue + slots[i]*ads[i]
    return revenue


def merge_sort(lst):
    if(len(lst) == 1):
        return lst
    else:
        mid = math.floor(((len(lst) - 1) - 0)/2)
        left = merge_sort(lst[0: mid + 1])
        right = merge_sort(lst[mid + 1: len(lst)])
        return merge(left, right)


def merge(left, right):
    lst = [0 for i in range(len(left) + len(right))]
    e = 0
    r = 0
    for i in range(len(left) + len(right)):
        if(e >= len(left)):
            lst[i] = right[r]
            r = r + 1
        elif(r >= len(right)):
            lst[i] = left[e]
            e = e + 1
        elif(left[e] >= right[r]):
            lst[i] = left[e]
            e = e + 1
        else:
            lst[i] = right[r]
            r = r + 1
    return lst


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
    print(merge_sort([3, 1, 4, 2, 5]))
    n = input_single(1, 10**3)
    ads = input_multiple(n, -10**5, 10**5)
    slots = input_multiple(n, -10**5, 10**5)
    print(MaxAd(ads, slots))


