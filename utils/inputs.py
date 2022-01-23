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


