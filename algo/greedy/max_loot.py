#!usr/bin/python3
def best_item(tuples):
    best_index = 0
    best_vw = 0
    for index, tuple in enumerate(tuples):
        print(tuple)
        if(tuple[1] == 0):
            continue
        vw = tuple[0]/tuple[1]
        if(vw > best_vw):
            best_vw = vw
            best_index = index
    return best_index, best_vw


def maxloot(tuples, W, n):
    print("in here")
    lst = [0 for i in range(n)]
    value = 0
    for index in range(len(tuples)):
        if(W == 0):
            return (value, lst)
        best_index, best_vw = best_item(tuples)
        a = min(W, tuples[best_index][1])
        W = (W - a)
        value = value + best_vw*a
        tuples[best_index][1] = tuples[best_index][1] - a
        lst[index] = a
    return (value, lst)


flag = False
while flag is False:
    try:
        W, n = input("enter W and n").split()
        W = int(W)
        n = int(n)

        if((W >= 0 and W <= 2*(10**6)) and (n >= 1 and n <= (10**3))):
            flag = True
        else:
            flag = False
            raise ValueError
    except ValueError:
        print("Invalid input, try again")
tuples = [[0, 0] for i in range(n)]
flag = False
for i in range(n):
    while flag is False:
        try:
            v, w = input("enter v and w of ith item").split()
            v = int(v)
            w = int(w)
            if((v >= 0 and v <= 10**6) and (w >= 0 and w <= 10**6)):
                tuples[i] = [v, w]
                flag = True
            else:
                flag = False
                raise ValueError
        except ValueError:
            print("Invalid input, try again")

    flag = False
print(tuples)
print(maxloot(tuples, W, n))
