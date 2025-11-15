n = int(input())
friends = list(map(int, input().split()))

result = []


for i in range(1, len(friends) + 1):
    result.append(friends.index(i) + 1)

print(" ".join(map(str, result)))