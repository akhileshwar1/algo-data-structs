def mergeLists(head1, head2):
    head3 = None
    print("this")
    print(head1.len() + head2.len())
    for i in range(head1.len() + head2.len()):
        if(head1.ptr is None and head2.ptr is None):
            head3.print()

        elif(head1.ptr is None):
            node = Node(head2.value(), None)
            if(i == 0):
                head3 = LinkedList(node)
            else:
                head3.insert(node)
            head2.move_right()
        elif(head2.ptr is None):
            node = Node(head1.value(), None)
            if(i == 0):
                head3 = LinkedList(node)
            else:
                head3.insert(node)
            head1.move_right()
        elif(head1.value() == head2.value()):
            node = Node(head1.value(), None)
            nodex = Node(head2.value(), None)
            if(i == 0):
                head3 = LinkedList(node)
                head3.insert(nodex)
            else:
                head3.insert(node)
                head3.insert(nodex)
            head1.move_right()
            head2.move_right()

        elif(head1.value() < head2.value()):
            node = Node(head1.value(), None)
            if(i == 0):
                head3 = LinkedList(node)
            else:
                head3.insert(node)
            head1.move_right()
        elif(head2.value() < head1.value()):
            node = Node(head2.value(), None)
            if(i == 0):
                head3 = LinkedList(node)
            else:
                head3.insert(node)
            head2.move_right()


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


if(__name__ == "__main__"):
    node1 = Node(1, None)
    node2 = Node(1, None)
    head1 = LinkedList(node1)
    head2 = LinkedList(node2)
    head1.insert(Node(3, None))
    head1.insert(Node(7, None))
    head2.insert(Node(2, None))
    print(mergeLists(head1, head2))







