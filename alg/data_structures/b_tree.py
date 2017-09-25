import pickle
import uuid
STORAGE = 'resources/'

class Node:
    def __init__(self, leaf=False):
        self.refs = []
        self.keys = []
        self.leaf = leaf
        self.id = uuid.uuid4()

    @property
    def size(self):
        return len(self.keys)

    @staticmethod
    def read(key):
        filename = STORAGE + key
        with open(filename) as f:
            return pickle.load(f)

    def save(self):
        filename = STORAGE + self.id
        with open(filename, 'w') as f:
            pickle.dump(self, f)


class Btree:
    def __init__(self, limit):
        self.minimum = limit
        self.maximum = 2*limit
        self.root = Node(True)
        self.root.save()

    def split(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass