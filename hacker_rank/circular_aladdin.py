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

    def circle(self):
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.head


class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


def aladdin(magic, len, dist):
    print("in here")
    for i in range(len):
        fuel = magic.value()
        initial = magic.value()
        magic.ptr = magic.ptr.next
        flag = 0
        while magic.ptr.data != initial:
            if(fuel < dist.value()):
                flag = 1
                dist.move_right()
                break
            else:
                fuel = fuel + magic.value() - dist.value()
                magic.move_right()
                dist.move_right()
        if(fuel >= 0 and flag == 0):
            return i


if(__name__ == '__main__'):
    magic = LinkedList(Node(2, None))
    magic.insert(Node(4, None))
    magic.insert(Node(5, None))
    magic.insert(Node(2, None))
    len = magic.len()
    magic.circle()
    dist = LinkedList(Node(4, None))
    dist.insert(Node(3, None))
    dist.insert(Node(1, None))
    dist.insert(Node(3, None))
    dist.circle()
    print(aladdin(magic, len, dist))
