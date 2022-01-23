dict = {}
def sum_in(W, i, weights):
    if(i == len(weights) or W <= 0):
        return 0
    else:
        if(tuple([W, i]) in dict):
            return dict[tuple([W, i])]
        else:
            s = weights[i] + sum_in(W - weights[i], i + 1, weights)
            e = 0 + sum_in(W, i + 1, weights)
            if(s <= W and e <= W):
                if(s > e):
                    dict[tuple([W, i])] = s
                    return s
                else:
                    dict[tuple([W, i])] = e
                    return e
            elif(s > W and e <= W):
                dict[tuple([W, i])] = e
                return e
            elif(e > W and s <= W):
                dict[tuple([W, i])] = s
                return s
            else:
                dict[tuple([W, i])] = 0
                return 0


def sum_inn(W, i, weights):
    if(i == len(weights) or W <= 0):
        return 0
    else:
        if(tuple([W, i]) in dict):
            return dict[tuple([W, i])]
        else:
            s = weights[i] + sum_inn(W - weights[i], i + 1, weights)
            e = 0 + sum_inn(W, i + 1, weights)
            if(s >= e and s <= W):
                dict[tuple([W, i])] = s
                return s
            elif(e >= s and e <= W):
                dict[tuple([W, i])] = e
                return e
            else:
                return 0



if __name__ == "__main__":
    result = sum_inn(13, 0, [5, 2, 1, 4])
    print(result)
