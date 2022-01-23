# from heap.build_heap import heap
# core principle: the bst property is satisfied at every node aka every
# subtree.

class BTree():
    def __init__(self, root):
        self.head = root

    def find(self, r, key):
        if(key == r.data):
            return r
        elif(key > r.data):
            if(r.right is not None):
                return self.find(r.right, key)
            else:
                return r
        elif(key < r.data):
            if(r.left is not None):
                return self.find(r.left, key)
            else:
                return r

    def left_descendant(self, r):
        if(r.left is not None):
            return self.left_descendant(r.left)
        else:
            return r

    def right_ancestor(self, r):
        if(r.parent.data > r.data):
            return r.parent
        else:
            return self.right_ancestor(r.parent)

    def next(self, r):
        if(r.right is not None):
            return self.left_descendant(r.right)
        else:
            return self.right_ancestor(r)

    def range_search(self, x, y, r):
        lst = []
        nxt = self.find(r, x + 1)
        while nxt.data <= y:
            if(nxt.data >= x):
                lst.append(nxt.data)
            nxt = self.next(nxt)
        return lst

    def insert(self, r, k):
        n = self.find(r, k)
        node = Node(k)
        if(r.data > k):
            n.attach_left(node)
        else:
            n.attach_right(node)

    def delete(self, r, k):
        n = self.find(r, k)
        # to check if the deleted node is a left or right child of its parent.
        # if the node to be deleted is a leaf node, just delete it.
        if(n.right is None and n.left is None):
            if(n.parent.left == n):
                n.parent.left = None
                n.parent = None
            else:
                n.parent.right = None
                n.parent = None

        elif(n.right is None):
            if(n.parent.left == n):
                n.parent.left = n.left
                n.left.parent = n.parent
            else:
                n.parent.right = n.left
                n.left.parent = n.parent

        else:
            nxt = self.next(n)
            # it will only get attached to the left leaf as we found the
            # next biggest integer with the smallest diff via that path.
            if(n.parent.left == n):
                if(nxt.right is None):
                    n.parent.left = nxt
                    nxt.parent = n.parent
                    nxt.left = n.left
                else:
                    # moving nxtt.right to nxts position
                    nxt.parent.left = nxt.right
                    nxt.right.parent = nxt.parent

                    n.parent.left = nxt
                    nxt.parent = n.parent
                    nxt.left = n.left
                    nxt.right = n.right

            else:
                if(nxt.right is None):
                    n.parent.right = nxt
                    nxt.parent = n.parent
                    nxt.left = n.left

                else:
                    # moving nxtt.right to nxts position
                    nxt.parent.left = nxt.right
                    nxt.right.parent = nxt.parent

                    n.parent.left = nxt
                    nxt.parent = n.parent
                    nxt.right = n.right
                    nxt.left = n.left


#        return self.queue[r]

#    def find(self, r, key):
#        if(key == self.at_index(r)):
#            return self.root
#        elif(key > self.at_index(r)):
#            if(super().left(r) is not None):
#                return self.find(super().left(r), key)
#            else:
#                return r
#        elif(key < self.at_index(r)):
#            if(super().right(r) is not None):
#                return self.find(super().right(r), key)
#            else:
#                return r


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def attach_left(self, node):
        self.left = node
        node.parent = self
        return node

    def attach_right(self, node):
        self.right = node
        node.parent = self
        return node


if __name__ == "__main__":
    root = Node(4)
    left = root.attach_left(Node(2))
    right = root.attach_right(Node(5))
    left.attach_left(Node(1))
    right = left.attach_right(Node(3))
    btree = BTree(root)
    print(btree.next(btree.find(root, 2)).data)
    print(btree.range_search(1, 4, root))
    btree.insert(root, 6)
    print(btree.find(root, 6).data)
    btree.delete(root, 2)
    print(btree.find(root, 3).left.data)
