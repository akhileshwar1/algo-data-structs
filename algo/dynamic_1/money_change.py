# uses python3


def min(m, c, p, greedy, i):
    if(i in c):
        return 1
    else:
        amt = m
        c.reverse()
        for j in c:
            greedy = greedy + amt//j
            amt = int(amt % j)
        if(amt > 0 or greedy == 0):
            return p+1
        elif(greedy < p):
            return greedy
        else:
            return p+1


def money_change_dp(m, c, p, i):

    if(i == m+1):
        print(p+1)
    elif(i == 0):
        money_change_dp(m, c, 0, i+1)
    else:
        # breakpoint()
        # minimum of greedy and the previous one.
        minimum = min(m, c, p, 0, i)
        money_change_dp(m, c, minimum, i+1)


n = int(input())
print(34//3)
lst = [1, 3, 4]
money_change_dp(n, lst, 0, 0)
