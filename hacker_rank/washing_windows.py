def washing(matrix, n, m):
    for x in range(1, n*m + 1):
        pass
    pass
n = 3
m = 4
def dirt(i, j, dp):
    if(i >= n - 1 or j >= m - 1):
        dp[i][j] = 0
        return dp
    else:
        dp[i - 1][j - 1] = 0
        dp[i - 1][j] = 0
        dp[i - 1][j + 1] = 0
        dp = dirt(i - 1, j - 1, dp)
        dp = dirt(i - 1, j, dp)
        dp = dirt(i - 1, j + 1, dp)
        return dp


dp = [[0 for _ in range(m)] for _ in range(n)]
print(dirt(0, 0, dp))
