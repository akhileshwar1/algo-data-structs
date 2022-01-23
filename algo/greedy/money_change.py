# uses python3
def money_change(n, divisors):
    total = 0
    while (n > 0):
        for i in reversed(divisors):
            if((n-i) >= 0):
                break
        n = n-i
        total = total + 1
    return total


n = int(input())
print(money_change(n, [1, 5, 10]))
