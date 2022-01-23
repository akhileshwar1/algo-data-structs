class Stack():
    def __init__(self, size):
        print("in here")
        self.size = size
        self.lst = [None]*self.size
        self.index = -1

    def push(self, data):
        if(self.index + 1 < self.size):
            self.lst[self.index + 1] = data
        else:
            self.size = self.size + 10
            self.lst[self.index + 1] = data
        self.index = self.index + 1

    def pop(self):
        x = self.lst[self.index]
        self.index = self.index - 1
        return x


class Editor(Stack):
    def __init__(self, size, s):
        super().__init__(size)
        self.l_index = -1
        super().push([s, None, None])

    def pop(self):
        return self.lst[self.index]

    def pop_undo(self):
        return self.lst[self.l_index]

    def modify(self, lst):
        self.lst[self.index] = lst

    def modify_undo(self, lst):
        self.lst[self.l_index] = lst

    def append(self, c):
        lst = self.pop()
        print(lst)
        s = lst[0] + c
        print(s)
        result = [lst[0], c, 1]
        self.modify(result)
        super().push([s, None, None])
        self.l_index = self.l_index + 1

    def delete(self, k):
        S = ""
        lst = self.pop()
        for i in range(len(lst[0]) - k):
            S[i] = lst[0][i]
        self.modify([lst[0], k, 2])
        super().push([S, None, None])
        self.l_index = self.l_index + 1

    def print(self, k):
        lst = self.pop()
        print(lst)
        for i in range(len(lst[0])):
            print(len(lst[0]))
            if(i == (k - 1)):
                print("printing")
                print(lst[0][i])
        self.modify([lst[0], k, 3])
        super().push([lst[0], None, None])

    def undo(self):
        lst = self.pop_undo()
        lst1 = self.pop()
        result = [lst1[0], None, 4]
        self.modify(result)
        super().push([lst[0], None, None])
        while self.lst[self.l_index][2] != 2 or self.lst[self.l_index][2] != 1:
            self.l_index = self.l_index - 1


if __name__ == "__main__":
    q = int(input())
    editor = Editor(10, "")
    for i in range(q):
        t = int(input())
        if(t == 1):
            s = input()
            editor.append(s)

        elif(t == 2):
            k = int(input())
            editor.delete(k)

        elif(t == 3):
            k = int(input())
            editor.print(k)

        elif(t == 4):
            editor.undo()







