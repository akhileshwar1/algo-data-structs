def findParent(no):
    def layer(x, lst):
        n_list = []
        for i in range(len(lst)):
            for j in range(lst[i]):
                x = x + 1
                n_list.append(x)
            if(no in n_list):
                return lst[i]
        return layer(x, n_list)
    print(layer(1, [1]))


if __name__ == '__main__':
    findParent(6)
