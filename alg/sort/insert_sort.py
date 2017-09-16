from alg.test_utils import utils


@utils.test_wrapper
def insert_sort(a):
    """insertion sort alg implementation"""
    size = len(a)
    # find key
    for key in range(1, size):
        key_to_insert = a[key]
        # insert key in sorted sequence
        for margin in reversed(range(0, key)):
            if key_to_insert < a[margin]:
                a[margin + 1] = key_to_insert
                break
            else:
                # SHIFT THE MARGIN
                a[margin + 1] = a[margin]
        else:
            a[0] = key_to_insert
    return a
