import sys

input_data = sys.stdin.read()
iterator = iter(input_data)

n = int(next(iterator))
m = int(next(iterator))
k = int(next(iterator))

print(n, m, k)

# same as

n, m, k = map(int, sys.stdin.readline().split())