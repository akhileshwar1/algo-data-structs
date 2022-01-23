class Llist():
    def __init__(self):
        self.head = None
        self.ptr = None

    def remove(self, Node):
        while self.ptr.next is not None:
            current = self.ptr
            next = self.ptr.next
            if(Node.data == next.data):
                current.next = Node
            self.ptr = self.ptr.next

    def insert(self, Node):
        while self.ptr.next is not None:
            self.ptr = self.ptr.next

        self.ptr.next = Node

    def max(self):


class Node():
    def __init__(self):
        self.data = None
        self.next = None


flag = False
n = int(input())
ads = new Llist()
for i in range(n):
    while flag is False:
        x = int(input())
        if(ad > 0 and ad < 1000):
            ad = new Node()
            ad.data = x
            flag = True
            ads.insert(ad)

    flag = False


