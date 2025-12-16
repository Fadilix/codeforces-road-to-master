def h_rec(lst, x, d, f):
    if d > f:
        return False

    mid = (d + f) // 2

    if x == lst[mid]:
        return True

    if x < lst[mid]:
        return h_rec(lst, x, d, mid - 1)
    return h_rec(lst, x, mid + 1, f)


def h(lst, x):
    return h_rec(lst, x, 0, len(lst) - 1)
