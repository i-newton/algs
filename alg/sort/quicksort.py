from test_utils import utils


def partition(a, start, end):
    delim = end
    less_div = start - 1
    for more_div in range(start, end):
        if a[more_div] < a[delim]:
            less_div += 1
            a[less_div], a[more_div] = a[more_div], a[less_div]

    a[delim], a[less_div+1] = a[less_div+1], a[delim]
    return less_div + 1


def quick_sort_impl(a, start, end):
    if start < end:
        delimeter = partition(a, start, end)
        quick_sort_impl(a, start, delimeter - 1)
        quick_sort_impl(a, delimeter + 1, end)


def quick_sort(a):
    quick_sort_impl(a, 0, len(a) - 1)
    return a


if __name__ == "__main__":
    utils.test_sort_fun(quick_sort)
