count = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split(" "))
    if a + b + c >= 2:
        count += 1
print(count)