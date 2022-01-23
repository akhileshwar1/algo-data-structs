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


class queue(Stack):
    def __init__(self, size):
        Stack.__init__(self, size)
        print(self.index)
        self.s_index = 0

    def enqueue(self, data):
        super().push(data)

    def __str__(self):
        return str(self.lst)

    def pop(self):
        x = self.lst[self.s_index]
        self.s_index = self.s_index + 1
        return x


class queue_stack():
    def __init__(self, size):
        self.stack_left = Stack(size)
        self.stack_right = Stack(size)

    def enqueue(self, data):
        left = self.stack_left
        right = self.stack_right
        if(left.index != -1):
            while left.index != -1:
                right.push(left.pop())
            right.push(data)
        else:
            right.push(data)

    def dequeue(self):
        left = self.stack_left
        right = self.stack_right
        if(right.index != -1):
            while right.index != -1:
                left.push(right.pop())
            return left.pop()
        else:
            return left.pop()


if(__name__ == '__main__'):
    q = queue(10)
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(7)
    print(q.__str__())
    print(q.pop())
    q.pop()
    print('the second queue stack starts here')
    qs = queue_stack(10)
    qs.enqueue(5)
    qs.enqueue(6)
    qs.enqueue(7)
    qs.enqueue(8)
    print(qs.dequeue())
