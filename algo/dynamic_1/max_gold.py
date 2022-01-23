import copy


def max_gold(W, weights):
    if(W == 0 or len(weights) == 0):
        return 0
    elif(W < min(weights)):
        return 0
    else:
        arr = []
        for i in range(len(weights)):
            n_w = copy.deepcopy(weights)
            if(W >= weights[i]):
                x = n_w[i]
                del n_w[i]
                w = x + max_gold(W - x, n_w)
                arr.append(w)
        return max(arr)


dict = {}
def max_dp(W, weights):
    if(W == 0 or len(weights) == 0):
        if(str([W, weights]) in dict):
            return dict[str([W, weights])]
        else:
            dict[str([W, weights])] = 0
            return 0
    elif(W < min(weights)):
        if(str([W, weights]) in dict):
            return dict[str([W, weights])]
        else:
            dict[str([W, weights])] = 0
            return 0
    else:
        arr = []
        if(str([W, weights]) in dict):
            return dict[str([W, weights])]
        else:
            for i in range(len(weights)):
                n_w = copy.deepcopy(weights)
                if(W >= weights[i]):
                    x = n_w[i]
                    del n_w[i]
                    w = x + max_dp(W - x, n_w)
                    arr.append(w)
            dict[str([W, weights])] = max(arr)
            return max(arr)

dict = {}
def max_gold_true(W, i, weights):
    if(i == len(weights) or W <= 0):
        return 0
    else:
        if(tuple([W, i]) in dict):
            return dict[tuple([W, i])]
        else:
            s = weights[i] + max_gold_true(W - weights[i], i + 1, weights)
            e = 0 + max_gold_true(W, i + 1, weights)
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


if __name__ == "__main__":
    print(max_gold(10, [1, 4, 8]))
    print(max_dp(10, [1, 4, 8]))
    print(max_gold_true(10, 0, [1, 4, 8]))
