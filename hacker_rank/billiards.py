mem = {}
def ways(x, lst, total):
    if(x == 0):
        mem[x] = 1
        return mem[x]
    elif(x < min(lst)):
        mem[x] = 0
        return mem[x]
    else:
        og = total
        for i in range(len(lst)):
            if((x - lst[i]) in mem):
                total = total + mem[x - lst[i]]
            else:
                total = total + ways(x - lst[i], lst, og)
        mem[x] = total
        return mem[x]

def ways_opt(x, lst):
    dp = [1 for i in range(x + 1)]
    for i in range(1, len(dp)):
        total = 0
        for j in range(len(lst)):
            if(i - lst[j]) < 0:
                s = 0
            else:
                s = dp[i - lst[j]]
            total = total + s
        dp[i] = total
    print(dp)
    return dp[x]


if(__name__ == "__main__"):
    print((ways(2, [2, 3], 0)) % (10**9 + 9))
    print((ways_opt(5, [2, 3])) % (10**9 + 9))
