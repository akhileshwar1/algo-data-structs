def edit_dist(i, j, a, b, summ):
    if(i == -1 and j == -1):
        return summ
    elif(i == -1 or j == -1):
        return summ + 1
    else:
        if(a[i] == b[j]):
            m = edit_dist(i - 1, j - 1, a, b, summ)
        else:
            m = edit_dist(i - 1, j - 1, a, b, summ + 1)

        d = edit_dist(i - 1, j, a, b, summ + 1)
        i = edit_dist(i, j - 1, a, b, summ + 1)
        return min(m, d, i)


if __name__ == "__main__":
    print(edit_dist(6, 7, ['e','d','i','t','i', 'n', 'g'], ['d','i','s','t','a','n','c','e'], 0))
    print(edit_dist(1, 1, ['a', 'b'], ['a', 'b'], 0))
    print(edit_dist(4, 4, ['s', 'h', 'o', 'r', 't'], ['p', 'o', 'r', 't', 's'], 0))
