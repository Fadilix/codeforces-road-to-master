r = input()


lc = len("".join(i for i in r if i.islower()))
uc = len("".join(i for i in r if i.isupper()))

if lc < uc:
    print(r.upper())
    exit()

print(r.lower())