dict = {}
def parts_sum(even_value, i, lst):
    if(i == len(lst) or even_value <= 0):
        return [0, 0, 0]
    else:
        if(tuple([even_value, i]) in dict):
            return dict[tuple([even_value, i])]
        else:
            result = parts_sum(even_value - lst[i], i + 1, lst)
            a, m, e = result
            a, m, e = a + lst[i], m + lst[i], e + lst[i]





if __name__ == "__main__":
    result = parts_sum(36, 0, [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
    print(result)
    if(result == [36, 36, 36]):
        print(1)
    else:
        print(0)
