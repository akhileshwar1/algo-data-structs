def countways(bills, amount):
    pass

mem = {}
# overcounts and is top down memoized
def coin_change(bills, amount):
    if (amount <= 0):
        mem[amount] = 1
        return mem[amount]
    else:
        total = []
        for i in range(len(bills)):
            if(amount - bills[i]) >= 0:
                if((amount - bills[i]) in mem):
                    total.append(mem[amount - bills[i]])
                else:
                    total.append(coin_change(bills, amount - bills[i]))
        mem[amount] = sum(total)
        return mem[amount]


def countways_(bills, amount, index):
    if amount == 0:     # base case 1
        return 1
    if amount < 0 or index >= len(bills):      # base case 2
        return 0
    # count the number of ways to make amount by including bills[index] and excluding bills[index]
    return countways_(bills, amount - bills[index], index) + countways_(bills, amount, index+1)


def countways(bills, amount):
    return countways_(bills, amount, 0)


def countways_mem(bills, amount):
    length = len(bills)
    dp = [[1 for i in range(length)] for j in range(amount + 1)]
    for amt in range(1, amount + 1):
        for j in range(length):
            bill = bills[j]
            if amt - bill >= 0:
                x = dp[amt - bill][j]
            else:
                x = 0
            if j >= 1:
                y = dp[amt][j-1]
            else:
                y = 0
            dp[amt][j] = x + y
    return dp[amount][len(bills) - 1]


if __name__ == '__main__':
    # print(coin_change([10, 20], 100054))
    # print(countways([10, 20], 100054))
    print(countways_mem([10, 20], 300000))

