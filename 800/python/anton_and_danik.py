n = int(input())
r = input()

if r.count("A") > r.count("D"):
    print("Anton")
elif r.count("A") < r.count("D"):
    print("Danik")
else:
    print("Friendship")