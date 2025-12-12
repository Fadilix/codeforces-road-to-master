import sys


# def getIndex(s, idx, range="min"):
#     if range == "min":
#         for i in range(len(s), -1, -1):
#             if s[i] == s[idx]:
#                 return s[i]


def getMinRightIndex(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] == min(s):
            return i


def getMaxLeftIndex(s):
    for i in range(len(s)):
        if s[i] == max(s):
            return i


n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))


count = 0

idx_max = getMaxLeftIndex(s)
idx_min = getMinRightIndex(s)

# # while s[0] != max(s) and s[-1] != min(s):
# while idx_max != 0 and idx_min != len(s) - 1:
#     if idx_max != 0:
#         idx_max -= 1
#         count += 1

#     if idx_max != 0:
#         idx_min += 1
#         count += 1

# print(count)


# print(idx_max)
# print(idx_min)

count += idx_max + (len(s) - 1 - idx_min)

if idx_max > idx_min:
    count -= 1

print(count)


# print(count)
