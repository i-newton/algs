# 1.1.1
def exchange(a, b):
    a, b = b, a
    return a, b


# 1.1.2
def exchange_wo_nums(a, b):
    a += b
    b = a - b
    a = a - b
    return a, b


def test_exchange(test_fun):
    a1, a2 = 1, 2
    a1, a2 = test_fun(a1, a2)
    assert a1 == 2
    assert a2 == 1


# 1.1.3
def pow(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res


def test_pow():
    r = pow(2, 6)
    assert r == 64


#1.1.4
def pow_log(a,n):
    res = 1
    deg = 1
    while deg < n:
        a = a*a
        if 2*deg > n:
            pass
    return res


if __name__ == "__main__":
    test_exchange(exchange)
    test_exchange(exchange_wo_nums)
    test_pow()

