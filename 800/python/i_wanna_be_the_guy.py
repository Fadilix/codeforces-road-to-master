import sys

n = int(sys.stdin.readline())

x = list(map(int, sys.stdin.readline().split()))[1:]
y = list(map(int, sys.stdin.readline().split()))[1:]


# print(x)
# print(y)
for i in range(1, n + 1):
    # print(i)
    # print(i not in x)
    # print(i not in y)
    if i not in x and i not in y:
        print("Oh, my keyboard!")
        exit()
print("I become the guy.")