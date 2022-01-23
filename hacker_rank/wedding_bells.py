def wedding(a, b, times, current, perms):
    if(times == 0):
        perms.append(current)
        return perms
    else:
        for i in range(times):
            temp_current = current.copy()
            temp_current.append([a[0], b[i]])
            temp_b = b.copy()
            temp_b.remove(b[i])
            temp_a = a.copy()
            temp_a.remove(a[0])
            perms = wedding(temp_a, temp_b, times - 1, temp_current, perms)

        return perms


def perm(x, y):
    if(x == 1):
        return y - 1
    else:
        return y*perm(x - 1, y - 1)


def n_choose_k(a, k, times, perms, current):
    if(times == k - 1):
        temp = current.copy()
        perms.append(temp)
        return perms
    else:
        print(current)
        print(a)
        print(times)
        for i in range(times):
            print(i)
            temp_current = current.copy()
            temp_current.append(a[i])
            temp = a.copy()
            temp.remove(a[i])
            perms = n_choose_k(temp, k, times - 1, perms, temp_current)
        return perms

# not optimal way.
def n_choose_k_comb(a, k, times, perms, current):
    if(times == k - 1):
        temp = current.copy()
        # condition for checking if the perm is not a combination.
        perms.append(temp)
        return perms
    else:
        print(current)
        print(a)
        print(times)
        for i in range(times):
            print(i)
            temp_current = current.copy()
            temp_current.append(a[i])
            temp = a.copy()
            temp.remove(a[i])
            perms = n_choose_k(temp, k, times - 1, perms, temp_current)
        return perms


def n_choose_k_asc(a, k, times, perms, current, flag):
    if(times == k - 1):
        temp = current.copy()
        for i in range(len(temp) - 1):
            if(temp[i + 1] < temp[i]):
                flag = 0
                break
        if(flag == 1):
            perms.append(temp)
        return perms
    else:
        print(current)
        print(a)
        print(times)
        for i in range(times):
            print(i)
            temp_current = current.copy()
            temp_current.append(a[i])
            temp = a.copy()
            temp.remove(a[i])
            perms = n_choose_k_asc(temp, k, times - 1, perms, temp_current, 1)
        return perms


def n_choose_k_asc_optimised(a, k, times, perms, current):
    if(times == k - 1):
        temp = current.copy()
        perms.append(temp)
        return perms
    else:
        print(current)
        print(a)
        print(times)
        for i in range(times):
            print(i)
            if(len(current) != 0 and a[i] < current[len(current) - 1]):
                continue
            temp_current = current.copy()
            temp_current.append(a[i])
            temp = a.copy()
            temp.remove(a[i])
            perms = n_choose_k_asc_optimised(temp, k, times - 1, perms, temp_current)
        return perms


def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


if __name__ == '__main__':
    print(n_choose_k([1, 2, 3], 2, 3, [], []))
    print(n_choose_k([4, 5, 6], 2, 3, [], []))
    print(n_choose_k_asc([4, 5, 6], 2, 3, [], [], 1))
    print(n_choose_k_asc_optimised([4, 5, 6], 2, 3, [], []))
    print(wedding([1, 2, 3], [4, 5, 6], 3, [], []))
