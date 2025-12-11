import time
start = time.time()

array = [int(input().split()) for _ in range(1000)]

end = time.time()

print(end - start)