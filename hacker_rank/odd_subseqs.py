def odd_subs(lst):
    odd_lst = []
    for i in range(len(lst)):
        if(lst[i] % 2 != 0):
            odd_lst.append(lst[i])
    k = 1
    n = len(odd_lst)
    count = 0
    while k <= n:
        count = count + fact(n)/(fact(n-k)*fact(k))
        k = k + 2
    return count


def fact(x):
    if(x == 0):
        return 1
    elif(x == 1):
        return 1
    else:
        return x*fact(x-1)


if __name__ == "__main__":
    lst = [4, 1, 3, 5]
    print(odd_subs(lst))
