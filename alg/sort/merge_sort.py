import math

from test_utils import utils


def merge_sort(a):
    return merge_sort_subarray(a, 0, len(a))


def merge(a, first, middle, last):
    la = a[first:middle]
    ra = a[middle:last]
    li = ri = 0
    la.append(math.inf)
    ra.append(math.inf)
    for i in range(first, last):
        if la[li] <= ra[ri]:
            a[i] = la[li]
            li += 1
        else:
            a[i] = ra[ri]
            ri += 1


def merge_sort_subarray(a, first, last):
    subarray_size = last - first
    if subarray_size > 1:
        middle = (first+last)//2
        merge_sort_subarray(a, first, middle)
        merge_sort_subarray(a, middle, last)
        merge(a, first, middle, last)
    return a

utils.test_sort_fun(merge_sort)
