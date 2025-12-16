def g(a, b):
    if b == 0:
        return 1
    res = g(a, b // 2)

    if b % 2 == 0:
        result = res * res
        return result
    if b % 2 == 1:
        return res * res * a


print(g(2, 3))
