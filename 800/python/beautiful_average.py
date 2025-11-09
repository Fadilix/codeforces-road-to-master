t = int(input())

for _ in range(t):
    max_so_far = float("-inf")
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_arr = arr[i:j]
            avr = sum(sub_arr) / len(sub_arr)
            max_so_far = max(max_so_far, avr)
    print(int(max_so_far))
