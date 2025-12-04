t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # min_val = float("inf")
    # print(min_val)

    # b = []


    # print("This is b", *b)
    # print(abs(sum(b)))

    if a[0] == -1 and a[-1] != -1:
        a[0] = a[-1]

    elif a[0] != -1 and a[-1] == -1:
        a[-1] = a[0]

    elif a[0] == -1 and a[-1] == -1:
        a[-1] = a[0] = 0

    for i in range(len(a)):
        if a[i] == -1:
            a[i] = 0
    
    # for i in range(len(a) -1):
    #     b.append(a[i + 1] - a[i])

# print(abs(sum(b)))
    print(abs(a[-1] - a[0])) # telescopic sum
    print(*a)


    # print(min(b, key=lambda x: x >= 0))
    # print("This is the final", *a)
    
    # for i in range(len(a) - 1):
    # if a
    # b.append(a[i + 1] - a[i])

    # print(sum(b))


# a = list(map(int, input().split()))

# s = 0

# for i in range(len(a) - 1):
#     s += a[i + 1] - a[i]

# print(s)
