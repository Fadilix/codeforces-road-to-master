a = input()
b = input()

# print(bin(abs(int(a, 10) - int(b, 10)))[2:])
result = ""

for i in range(len(a)):
    if a[i] != b[i]:
        result += "1"
    else:
        result += "0"

print(result)

