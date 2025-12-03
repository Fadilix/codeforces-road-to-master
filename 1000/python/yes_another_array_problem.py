# from math import gcd

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
# test

t = int(input())
HIGH = 10e8
LOW = 2
finished = False

# a = list(map(int, input().split()))

for _ in range(t):
    l = int(input())
    a = list(map(int, input().split()))

    for i in range(l):
        for x in range(int(LOW), int(HIGH)):
            if gcd(a[i], x) == 1:
                print(x)
                finished = True
                break
        if finished:
            finished = False
            break
print("-1")

# i will come back
# print(gcd(10, 458))
