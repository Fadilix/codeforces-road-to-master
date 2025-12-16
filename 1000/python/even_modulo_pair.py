import sys

tt = int(sys.stdin.readline())

while tt:
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))

    found = False
    
    for x in range(n):
        for y in range(x + 1, n):
            if (l[y] % l[x]) % 2 == 0 and l[x] < l[y]:
                print(f"{l[x]} {l[y]}")
                found = True
                break
        if found:
            break
    
    if not found:
        print("-1")
    
    tt -= 1