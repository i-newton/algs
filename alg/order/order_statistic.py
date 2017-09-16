from alg.sort import quicksort
import random


def get_nth_item(a, n):
    b = a[:]
    return select(b, n, 0, len(a) - 1)


def select(a, n, begin, end):
    if begin == end:
        return a[begin]
    div = quicksort.randomized_partition(a, begin, end)
    order = div - begin + 1
    if order == n:
        return a[div]
    elif order > n:
        return select(a, n, begin, div - 1)
    else:
        return select(a, n - order, div + 1, end)


if __name__ == "__main__":
    a = [random.randint(0, 10) for i in range(10)]
    print(a)
    for i in range(1, 11):
        print(get_nth_item(a, i))
