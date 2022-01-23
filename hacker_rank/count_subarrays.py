def count(lst, index, sum):
    if(index == len(lst)):
        return sum + len(lst)
    else:
        start = index
        while (index <= (len(lst) - 2)):
            if(lst[index + 1] >= lst[index]):
                print(lst[index], lst[index + 1])
                sum = sum + 1
                index = index + 1
            else:
                index = start
                break
        return sum + count(lst, index + 1, 0)

# this is  right, just add len(lst) to the sum of the resulting array.
def count_opt(lst, index):
    if(index == len(lst) - 1):
        total = []
        total.append(0)
        return total
    else:
        if(lst[index] <= lst[index + 1]):
            total = count_opt(lst, index + 1)
            total.append(1 + total[len(total) - 1])
            return total
        else:
            total = count_opt(lst, index + 1)
            total.append(0)
            return total


if(__name__ == '__main__'):
    print(count_opt([1, 4, 5, 2, 3], 0))
