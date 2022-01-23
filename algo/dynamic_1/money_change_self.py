def money_change(money, denom):
    mini = 1000
    if(money == 0):
        return 0
    else:
        for i in range(len(denom)):
            if(money >= denom[i]):
                x = 1 + money_change(money - denom[i], denom)
                if(x < mini):
                    mini = x
            else:
                continue
        return mini


if __name__ == "__main__":
    print(money_change(6, [1, 3, 4]))
    print(money_change(34, [1, 3, 4]))
