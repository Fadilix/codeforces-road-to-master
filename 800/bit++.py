starter = 0
for _ in range(int(input())):
    s = input()
    if s == "--X" or s == "X--":
        starter -= 1
    elif s == "++X" or s == "X++":
        starter += 1
print(starter)