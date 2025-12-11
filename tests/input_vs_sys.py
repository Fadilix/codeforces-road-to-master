import sys
import time
from io import StringIO

# -----------------------------------------------------------
# Generate fake stdin input (N lines)
# -----------------------------------------------------------
N = 300_000  # number of lines to test
fake_input = "\n".join(str(i) for i in range(N)) + "\n"

print("Generated", N, "lines of input =", len(fake_input), "bytes")

# -----------------------------------------------------------
# Test 1: input()
# -----------------------------------------------------------
sys.stdin = StringIO(fake_input)

t0 = time.time()
total = 0
for _ in range(N):
    total += int(input())
t1 = time.time()

print("input() time:", t1 - t0)


# -----------------------------------------------------------
# Test 2: sys.stdin.readline()
# -----------------------------------------------------------
sys.stdin = StringIO(fake_input)

t0 = time.time()
total = 0
for _ in range(N):
    total += int(sys.stdin.readline())
t1 = time.time()

print("sys.stdin.readline() time:", t1 - t0)


# -----------------------------------------------------------
# Test 3: sys.stdin.read().split()
# -----------------------------------------------------------
sys.stdin = StringIO(fake_input)

t0 = time.time()
data = sys.stdin.read().split()
total = sum(map(int, data))
t1 = time.time()

print("sys.stdin.read().split() time:", t1 - t0)
