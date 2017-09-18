import random
import math


def get_hash_func(size):
    a = random.randint(0, 10000)
    b = random.randint(0, 10000)
    p = 10429

    def hash(key):
        return ((a*key+b) % p) % size
    return hash


def get_hash_alt_fun(size):
    a = (math.sqrt(5) - 1)/2

    def fun(key):
        n = key*a
        fr = math.modf(n)[0]
        return math.ceil((size-1)*fr)
    return fun


class Hash:
    def __init__(self, size):
        self._size = size
        self._hash = get_hash_func(size)
        self._data = [[]for j in range(size)]

    def __getitem__(self, key):
        hash_key = self._hash(key)
        for item in self._data[hash_key]:
            if item[0] == key:
                return item[1]
        raise KeyError()

    def __setitem__(self, key, value):
        hash_key = self._hash(key)
        for pos, item in enumerate(self._data[hash_key]):
            if item[0] == key:
                self._data[hash_key][pos] = (key, value)
                break
        else:
            self._data[hash_key].append((key, value))

    def print_sizes(self):
        sizes = [(k, len(v)) for k, v in enumerate(self._data)]
        print(sorted(sizes, key=lambda size: size[1]))
        count = {}
        for item in sizes:
            count[item[1]] = count.get(item[1],0) + 1
        print(count)

if __name__ == "__main__":
    random.seed()
    h = Hash(113)
    for i in range(200):
        h[random.randint(0, 10000)] = random.random()
    h.print_sizes()
