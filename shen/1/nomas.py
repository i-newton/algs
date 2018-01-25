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


# 1.1.4
def pow_log(a, n):
    res = 1
    c = a
    while n > 0:
        if (n % 2) == 0:
            n = n // 2
            c = c * c
        else:
            res = res * c
            n -= 1
    return res


def test_pow(f):
    r = f(2, 10)
    assert r == 1024

# 1.1.5


if __name__ == "__main__":
    test_exchange(exchange)
    test_exchange(exchange_wo_nums)
    test_pow(pow)
    test_pow(pow_log)
