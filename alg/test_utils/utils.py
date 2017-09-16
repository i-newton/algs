import random

funcs_test = {}


def test_wrapper(fun):
    funcs_test[str(fun)] = fun


def test_sort_fun(sort_fun, max_num=1000, max_items=1000):
    tc1 = []
    tc2 = [random.randint(0, max_num) for i in range(max_items)]
    print(sort_fun(tc1))
    print(tc2)
    print(sort_fun(tc2))
    tc3 = [78]
    print(sort_fun(tc3))
    print(sort_fun(list(reversed(tc2))))
    tc4 = [51, 48, 88]

    print(sort_fun(tc4))
