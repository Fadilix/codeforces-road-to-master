n = int(input()) # stops


capacity = 0
min_capacity = float("-inf")

for i in range(n):
    out, enter = map(int, input().split())
    capacity = capacity - out + enter
    print(f"The capacity is {capacity}")
    min_capacity = max(capacity, min_capacity)

print(min_capacity)

