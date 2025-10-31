n = int(input())
p = list(map(int, input().split()))

if sum(p) > 0:
    print("HARD")
else:
    print("EASY")