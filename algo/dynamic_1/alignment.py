import copy


def align_score(matrix, i, length, sum):
    if(i == length):
        return sum
    else:
        d_matrix = copy.deepcopy(matrix)
        d_matrix[1].append('-')
        b_len = len(d_matrix[1])
        for j in range(b_len - 1, i, -1):
            d_matrix[1][j] = d_matrix[1][j-1]
        d_matrix[1][i] = '-'

        i_matrix = copy.deepcopy(matrix)
        i_matrix[0].append('-')
        i_len = len(i_matrix[0])
        for j in range(i_len - 1, i, -1):
            i_matrix[0][j] = i_matrix[0][j-1]
        i_matrix[0][i] = '-'

        if(matrix[0][i] == matrix[1][i]):
            m = align_score(matrix, i + 1, length, sum)
        else:
            m = align_score(matrix, i + 1, length, sum + 1)
        d = align_score(d_matrix, i + 1, length, sum + 1)
        n = align_score(i_matrix, i + 1, length, sum + 1)
        return min(m, d, n)


def test(matrix, i):
    d_matrix = copy.deepcopy(matrix)
    d_matrix[1].append('-')
    print(d_matrix)
    b_len = len(d_matrix[1])
    for j in range(b_len - 1, i, -1):
        d_matrix[1][j] = d_matrix[1][j-1]
    d_matrix[1][i] = '-'
    print(d_matrix)


if(__name__ == '__main__'):
    test([['s','h','o','r','t'], ['p','o','r','t','s']], 5)
    print(align_score([['e','d','i','t','i', 'n', 'g', '-'], ['d','i','s','t','a','n','c','e']], 0, 8, 0))
    print(align_score([['a', 'b'], ['a', 'b']], 0, 2, 0))
    print(align_score([['s', 'h', 'o', 'r', 't'], ['p', 'o', 'r', 't', 's']], 0, 5, 0))
    print(align_score([['2', '7', '8', '3'], ['5', '2', '8', '7']], 0, 4, 0))
