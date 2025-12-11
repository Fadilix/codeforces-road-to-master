import time
import sys

start = time.time()

array = [int(sys.stdin.readline()) for _ in range(1000)]

end = time.time()

print(end - start)