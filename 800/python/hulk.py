import sys

n = int(sys.stdin.readline())

feelings = ["I hate", "I love"]

if n == 1:
    print(feelings[0] + " it")
else:
    result = ""
    for i in range(n):
        result += feelings[i % len(feelings)]
        # print(result, i)
        if i != n - 1:
            result += " that "
    result += " it"
    print(result)
