k, n, w = list(map(int, input().split()))

s = sum(k * (i + 1) for i in range(w))


if n < s:
    print(abs(s - n))
else:
    print(0)