# This is WRONG, just did to experiment pure recursive style.
def combinations(lst, k, index, combs):
    if(len(lst) == index):
        return combs
    else:
        combs.append(interior_loop(index + 1, k - 1, lst, [], [lst[index]], k - 1, [lst[index]]))
        print(combs)
#        for i in range(index + 1, len(lst)):
#            temp = [lst[index]]
#            if((i + k - 1) <= len(lst)):
#                for j in range(i, i + k - 1):
#                    temp.append(lst[j])
#                combs.append(temp)
#            else:
#                continue
        return combinations(lst, k, index + 1, combs)


def interior_loop(start, k, lst, combs, temp, const, const_temp):
    if(start == len(lst)):
        return combs
    else:
        if(k == 0):
            combs.append(temp)
            return interior_loop(start + 1, const, lst, combs, const_temp, const, const_temp)
        # interior_loop(start, k - 1, combs.append(temp), const_temp, const, const_temp)
        elif(start + k) >= len(lst):
            return interior_loop(start + 1, const, lst, combs, const_temp, const, const_temp)
        # interior_loop(start, k - 1, combs, temp.append(lst[start]), const, const_temp)
        else:
            temp.append(lst[start + (const - k)])
            return interior_loop(start, k - 1, lst, combs, temp, const, const_temp)



if __name__ == '__main__':
    print(combinations([1, 2, 3, 4, 5], 2, 0, []))
