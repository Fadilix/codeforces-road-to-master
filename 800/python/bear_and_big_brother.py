l, b = map(int, input().split())

count = 0
if l == b:
    print("1")
    exit()

while l <= b:
    count += 1
    l *= 3
    b *= 2

print(count)
