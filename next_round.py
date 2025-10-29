n, k = map(int, input().split())

l = input().split()

count = 0
for i in range(n):
    if int(l[i]) >= int(l[k -1]) and int(l[i]) > 0:
        count += 1
print(count)