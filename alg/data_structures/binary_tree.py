import functools
import random


@functools.total_ordering
class Node:
    def __init__(self, key=None, parent=None, left=None, right=None,
                 size=1):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.size = size

    def __lt__(self, other):
        if hasattr(other, "key"):
            return self.key < other.key
        else:
            return self.key < other

    def __eq__(self, other):
        if hasattr(other, "key"):
            return self.key == other.key
        else:
            return self.key == other

    def __len__(self):
        return self.size

    def __bool__(self):
        if self.key:
            return self.key is not None

    def __str__(self):
        return "key:{key}, size:{size}, left:{left},right:{right}".format(
            key=self.key, size=self.size,
            left=(self.left.key if self.left else None),
            right=(self.right.key if self.right else None))


class BinaryTree:
    def __init__(self):
        self.root = None

    def sorted(self):
        sa = []
        BinaryTree.execute_for_subtree(self.root, lambda k, a: a.append(k), sa)
        return sa

    def minimum(self, node=None):
        x = self.root if node is None else node
        while x and x.left:
            x = x.left
        return x

    def maximum(self, node=None):
        x = self.root if node is None else node
        while x and x.right:
            x = x.right
        return x

    def insert(self, node):
        y = None
        x = self.root
        while x:
            y = x
            y.size += 1
            if node < x:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node < y:
            y.left = node
        else:
            y.right = node

    def _transplant(self, dig, plant):
        if not dig.parent:
            self.root = plant
        elif dig == dig.parent.left:
            dig.parent.left = plant
        else:
            dig.parent.right = plant
        if plant:
            plant.parent = dig.parent

    def delete(self, node):
        #update sizes
        p = node.parent
        while p:
            p.size -= 1
            p = p.parent
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            next = self.minimum(node)
            if next.parent != node:
                self._transplant(next, next.right)
                next.right = node.right
                next.right.parent = next
            self._transplant(node, next)
            next.left = node.left
            next.left.parent = next

    def successor(self, node):
        if node.right:
            return self.minimum(node.right)
        y = node.parent
        while y and node == y.right:
            node = y
            y = y.parent
        return y

    def predessor(self, node):
        if node.left:
            return self.maximum(node.left)
        y = node.parent
        while y and node == y.left:
            node = y
            y = y.parent
        return y

    def rank(self, node):
        pass

    def select(self, order):
        pass

    @staticmethod
    def execute_for_subtree(root, func, *args, **kwargs):
        if root:
            BinaryTree.execute_for_subtree(root.left, func, *args, **kwargs)
            func(root, *args, **kwargs)
            BinaryTree.execute_for_subtree(root.right, func, *args,
                                           **kwargs)

    def print(self):
        BinaryTree.execute_for_subtree(self.root, print)

    def get_node(self, key):
        x = self.root
        while x:
            if x == key:
                return x
            elif key < x:
                x = x.left
            else:
                x = x.right
        raise KeyError()

if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(3):
        h = random.randint(0, 20000)
        bt.insert(Node(key=h))
    bt.print()
    print("sorted:")
    ls = bt.sorted()
    for i in ls:
        print(i)
    print("minimum")
    print(bt.minimum())
    print("maximum")
    print(bt.maximum())
    print("successor-predessor")
    for i in ls:
        print("current:" + str(i))
        print("S: " + str(bt.successor(i)))
        print("P: " + str(bt.predessor(i)))
    print("deleted")
    for i in ls:
        bt.delete(i)
        bt.print()


