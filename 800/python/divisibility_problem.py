import sys

tt = int(sys.stdin.readline())

while tt:
    a, b = map(int, sys.stdin.readline().split())
    if a % b == 0:
        print(0)
    else:
        print(b - (a % b))
    tt -= 1
