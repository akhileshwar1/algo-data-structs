class LinkedList():
    def __init__(self, node):
        self.head = node
        self.ptr = self.head
        self.pos = 0

    def move_right(self):
        self.ptr = self.ptr.next
        self.pos = self.pos + 1

    def value(self):
        return self.ptr.data

    def insert(self, Node):
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = Node

    def remove(self, data):
        ptr = self.head
        prev = None
        while ptr.data != data:
            prev = ptr
            ptr = ptr.next
        prev.next = ptr.next
        ptr.next = None

    def len(self):
        len = 0
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
            len = len + 1

        return len + 1

    def print(self):
        ptr = self.head
        while ptr.next is not None:
            print(ptr.data)
            ptr = ptr.next


class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Cookie_jar(LinkedList):
    def __init__(self, k, node):
        self.k = k
        super().__init__(node)

    def min_2(self):
        first = self.head.data
        second = self.head.next.data
        self.head = self.head.next.next
        return first, second

    def put_new(self, data):
        ptr = self.head
        if(data <= self.head.data):
            new = Node(data, self.head)
            self.head = new
        else:
            k = 0
            print(ptr.next.data)
            while (ptr.next is not None):
                if(ptr.next.data <= data):
                    ptr = ptr.next
                else:
                    new = Node(data, ptr.next)
                    ptr.next = new
                    k = 1
                    break
            if(k == 0):
                new = Node(data, ptr.next)
                ptr.next = new

    def check(self):
        ptr = self.head
        flag = 0
        while ptr is not None:
            if(ptr.data < self.k):
                flag = 1
            ptr = ptr.next
        if(flag == 0):
            return True
        else:
            return False


def cookies(jar, count):
    if(jar.check()):
        return count
    else:
        first, second = jar.min_2()
        new_cookie = 1*first + 2*second
        jar.put_new(new_cookie)
        return cookies(jar, count + 1)


if __name__ == '__main__':
    k = int(input())
    node = Node(2, None)
    jar = Cookie_jar(k, node)
    jar.insert(Node(7, None))
    jar.insert(Node(3, None))
    jar.insert(Node(6, None))
    jar.insert(Node(4, None))
    jar.insert(Node(6, None))
    print("answer add 1 at the end")
    print(cookies(jar, 0))
