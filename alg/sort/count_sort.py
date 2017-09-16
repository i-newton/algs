from alg.test_utils import utils

MAX_NUM = 100


def count_sort(a):
    count = [0 for i in range(MAX_NUM+1)]
    res = a[:]
    for item in a:
        count[item] += 1
    for k in range(1, len(count)):
        count[k] += count[k-1]
    for item in reversed(a):
        res[count[item] - 1] = item
        count[item] -= 1

    return res

utils.test_sort_fun(count_sort, max_num=MAX_NUM, max_items=10)
