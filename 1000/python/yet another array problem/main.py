from math import gcd

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# test

t = int(input())

# HIGH = 10**18

LOW = 2

# a = list(map(int, input().split()))

for _ in range(t):
    l = int(input())
    a = list(map(int, input().split()))

    # print(a)
    # a.sort()
    # print(a)

    best = float("inf")

    for ai in a:
        for x in range(LOW, 55):
            if gcd(ai, x) == 1 and x < best:
                best = x
                break

    if best == float("inf") or best > 10**18:
        print(-1)
    else:
        print(best)

    # print("-1")

# print(gcd(10, 458))
