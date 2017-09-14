import math


from test_utils import utils


class Heap:
    def __init__(self, array):
        self.heap = array
        self.size = len(array)
        self.build_heap()

    def heapify(self, pos):
        largest = self.get_node_maximum(pos)
        if largest != pos:
            self.swap(pos, largest)
            self.heapify(largest)

    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def get_node_maximum(self, root):
        largest = root
        if root < self.size:
            l = self.left(root)
            if l < self.size and self.heap[l] > self.heap[largest]:
                largest = l
            r = self.right(root)
            if r < self.size and self.heap[r] > self.heap[largest]:
                largest = r
        return largest

    @staticmethod
    def left(i):
        if i == 0:
            return 1
        return 2 * i

    @staticmethod
    def right(i):
        if i == 0:
            return 2
        return 2 * i + 1

    @staticmethod
    def parent(i):
        if i == 0:
            return None
        return i // 2

    def last(self):
        return self.size - 1

    def build_heap(self):
        for i in reversed(range(0, self.size//2)):
            self.heapify(i)

    def increase_key(self, i, new_key):
        if 0 <= i <= self.size and new_key >= self.heap[i]:
            p = self.parent(i)
            self.heap[i] = new_key
            while p and self.heap[p] < self.heap[i]:
                self.swap(p, i)
                i = p
                p = self.parent(p)
        else:
            raise ValueError()

    def add_key(self, e):
        self.heap.append(e)
        self.size += 1
        self.heap[self.last] = -math.inf
        self.increase_key(self.last(), e)


def heap_sort(a):
    h = Heap(a)
    for i in range(0, h.size):
        last_elem = h.last()
        h.swap(0, last_elem)
        h.size -= 1
        h.heapify(0)
    return h.heap

if __name__ == "__main__":
    utils.test_sort_fun(heap_sort)

