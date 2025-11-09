r = input()

if len(r) == 1:
    print(r)
    exit()

lr = list(map(int, r.split("+")))

# print(lr)
lr.sort()
# print(lr)

print("+".join(map(str, lr)))
