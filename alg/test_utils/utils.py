import random


def test_sort_fun(sort_fun):
    tc1 = []
    tc2 = [random.randint(0, 10000) for i in range(100)]
    sort_fun(tc1)
    print(tc1)
    print(tc2)
    sort_fun(tc2)
    print(tc2)
    tc3 = [78]
    sort_fun(tc3)
    print(sort_fun(list(reversed(tc2))))
    tc4 = [5196, 4899, 8878]
    sort_fun(tc4)
    print(tc4)
