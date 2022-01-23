# greedy
def knapsack(w, p, capacity):
    pw = 0
    index = -1
    for i in range(len(w)):
        if(p[i]/w[i] > pw):
            index = i
            pw = p[i]/w[i]
            weight = w[i]
    temp_w = w.copy()
    temp_p = p.copy()
    del temp_w[index]
    del temp_p[index]
    if(capacity > weight):
        result = pw*weight
        capacity = capacity - weight
        return result + knapsack(temp_w, temp_p, capacity)
    else:
        result = pw*capacity
        return result

mem = {}
# top down memoized
def knapsack_recur(w, p, capacity, tp, current):
    if(capacity == 0 or len(w) == 0):
        t_current = current.copy()
        t_current.sort()
        mem[tuple(t_current)] = tp
        return (mem[tuple(t_current)], current)
    else:
        total = []
        for i in range(len(w)):
            if(capacity >= w[i]):
                weight = w[i]
                price = p[i]
            else:
                continue
            temp_w = w.copy()
            temp_current = current.copy()
            t_current = temp_current.copy()
            t_current.sort()
            if(tuple(t_current) in mem):
                total.append((mem[tuple(t_current)], temp_current))
            else:
                temp_current.append(w[i])
                temp_p = p.copy()
                temp_w.remove(w[i])
                temp_p.remove(p[i])
                total.append(knapsack_recur(temp_w, temp_p, capacity - weight, tp + price, temp_current))
        if(len(total) != 0):
            mx = 0
            index = -1
            for i in range(len(total)):
                if(total[i][0] > mx):
                    mx = total[i][0]
                    index = i
            return (mx, total[index][1])
        else:
            return (tp, current)


def knapsack_recurr(w, p, capacity, tp, current):
    if(capacity == 0 or len(w) == 0):
        t_current = current.copy()
        t_current.sort()
        return (tp, current)
    else:
        total = []
        for i in range(len(w)):
            if(capacity >= w[i]):
                weight = w[i]
                price = p[i]
            else:
                continue
            temp_w = w.copy()
            temp_current = current.copy()
            t_current = temp_current.copy()
            t_current.sort()
            temp_current.append(w[i])
            temp_p = p.copy()
            temp_w.remove(w[i])
            temp_p.remove(p[i])
            total.append(knapsack_recur(temp_w, temp_p, capacity - weight, tp + price, temp_current))
        if(len(total) != 0):
            mx = 0
            index = -1
            for i in range(len(total)):
                if(total[i][0] > mx):
                    mx = total[i][0]
                    index = i
            return (mx, total[index][1])
        else:
            return (tp, current)


def solveKnapsack(weights, prices, capacity, index, memo):
    # base case of when we have run out of capacity or objects
    if capacity <= 0 or index >= len(weights):
        return 0
    # check for solution in memo table
    if (capacity, index) in memo:
        return memo[(capacity, index)]
    # if weight at index-th position is greater than capacity, skip this object
    if weights[index] > capacity:
        # store result in memo table
        memo[(capacity, index)] = solveKnapsack(weights, prices, capacity, index + 1, memo)
        return memo[(capacity, index)]
    # recursive call, either we can include the index-th object or we cannot, we check both possibilities and return the most optimal one using max
    memo[(capacity, index)] = max(prices[index]+solveKnapsack(weights, prices, capacity - weights[index], index+1, memo),
            solveKnapsack(weights, prices, capacity, index + 1, memo))
    return memo[(capacity, index)]


def knapsack_out(weights, prices, capacity):
    # create a memo dictionary
    memo = {}
    return solveKnapsack(weights, prices, capacity, 0, memo)


if __name__ == "__main__":
    # print(knapsack([1, 2, 4, 6], [4, 2, 4, 7], 7))
    # print(knapsack_recur([1, 2, 4, 6], [4, 2, 4, 7], 7, 0, []))
    # print(knapsack_recur([10, 20, 30], [60, 100, 120], 50, 0, []))
    # print(knapsack_recur([2, 1, 1, 3], [2, 8, 1, 10], 4, 0, []))
    print(knapsack_recurr([2, 1, 1, 3], [2, 8, 1, 10], 4, 0, []))
    # print(knapsack_out([2, 1, 1, 3], [2, 8, 1, 10], 4))

