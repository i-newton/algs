
class Node:
    def __init__(self, leaf=False):
        self.refs = []
        self.keys = []
        self.leaf = leaf

    @property
    def key_len(self):
        return len(self.keys)


    def read(self, key):
        filename = "resources//"+key
        with open(filename) as f:




class Btree:
    def __init__(self, limit):
        self.limit = limit

