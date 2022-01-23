# uses python 3

def edit_min(A, B):
    n = len(A)
    m = len(B)
    edit_mtx = [[0]*(m+1) for _ in range(n+1)]

    for i in range(m+1):
        edit_mtx[0][i] = i

    for i in range(n+1):
        edit_mtx[i][0] = i

    # going for column wise, not row wise
    for i in range(1, m+1):

        for j in range(1, n+1):
            # insertion
            insertion = edit_mtx[i][j-1]+1
            deletion = edit_mtx[i-1][j]+1
            matchmis = edit_mtx[i-1][j-1]
            if(A[i-1] == B[j-1]):
                edit_mtx[i][j] = min(insertion, deletion, matchmis)
            else:
                edit_mtx[i][j] = min(insertion, deletion, matchmis+1)
    print(edit_mtx)
    return edit_mtx[n][m]


print(edit_min(['e', 'd', 'i', '-', 't', 'i', 'n', 'g', '-'],
      ['-', 'd', 'i', 's', 't', 'a', 'n', 'c', 'e']))
