# python3
import sys
import threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.nodes = [0 for i in range(self.n)]
    for i in range(self.n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        self.key[i] = a
        self.left[i] = b
        self.right[i] = c

  def makeTree(self):
    nodes = self.nodes
    for i in range(self.n):
        nodes[i] = Node(self.key[i], None, None)
    for j in range(self.n):
        if(self.left[j] == -1 or self.right[j] == -1):
            if(self.left[j] == -1):
                left = None
                right = nodes[self.right[j]]
            elif(self.right[j] == -1):
                right = None
                left = nodes[self.left[j]]
        elif(self.left[j] == -1 and self.right[j] == -1):
            left = None
            right = None
        else:
            left = nodes[self.left[j]]
            right = nodes[self.right[j]]
        nodes[j].left = left
        nodes[j].right = right

  def printTree(self):
    for i in range(self.n):
        print(self.nodes[i].key)
    for i in range(self.n):
        if(self.nodes[i] is not None and self.nodes[i].left is not None and self.nodes[i].right is not None):
            print(self.nodes[i].key, self.nodes[i].left.key, self.nodes[i].right.key)

  def inOrder(self):
    def in_or(tree):
        if(tree is None):
            return
        in_or(tree.left)
        print(tree.key)
        in_or(tree.right)
    in_or(self.nodes[0])


  def preOrder(self):
    def pre_or(tree):
        if(tree is None):
            return
        print(tree.key)
        pre_or(tree.left)
        pre_or(tree.right)
    pre_or(self.nodes[0])



  def postOrder(self):
    def post_or(tree):
        if(tree is None):
            return
        post_or(tree.left)
        post_or(tree.right)
        print(tree.key)
    post_or(self.nodes[0])



class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def main():
    tree = TreeOrders()
    tree.read()
    tree.makeTree()
    tree.printTree()
    # tree.inOrder()
    # tree.preOrder()
    # tree.postOrder()
    # print(" ".join(str(x) for x in tree.inOrder()))
    # print(" ".join(str(x) for x in tree.preOrder()))
    # print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
