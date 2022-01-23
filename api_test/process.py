def process(no):
    def tree(n, parent):
        if(n == no):
            return parent
        else:
            for i in range(1, n+1):
                x = tree(n + i, parent)

