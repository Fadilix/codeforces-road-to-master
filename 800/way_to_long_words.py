# n = int(input())
# l = list()

# for i in range(n):
#     l.append(input())

# for word in l:
#     if len(word) > 10:
#         first = word[0]
#         last = word[-1]
#         mid = word[1:-1]
#         print(f"{first}{len(mid)}{last}")
#     else:
#         print(word)


####################### improvements ######################


for _ in range(int(input())):
    word = input()
    if len(word) > 10:
        print(f"{word[0]}{len(word) -2}{word[-1]}")
    else:
        print(word)
    