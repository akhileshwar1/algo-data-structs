# uses python 3
# i is index, and j is the denominations
def dp_money(m, c):
    k = len(c)
    matrix = [[0]*k for _ in range(m+1)]
    # print(matrix)
    for i in range(1, m+1):
        for j in range(0, k):
            # run the greedy algorithm and find the coins for a particular d.
            # breakpoint()
            m1 = i
            f = m1//c[j]
            m1 = m1-f*c[j]
            if(m1 > 0):
                if(f == 0):
                    matrix[i][j] = matrix[i][j-1]
                else:
                    matrix[i][j] = matrix[m1][j]+f
            else:
                matrix[i][j] = f

        # m = amt
    print(matrix)


m = int(input())
dp_money(m, [1, 3, 4])
