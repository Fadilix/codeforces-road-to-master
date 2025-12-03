from math import isqrt, gcd

def sieve_of_erathosthes(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, isqrt(n) + 1):
        for x in range(i*i, n, i):
            if is_prime[x]:
                is_prime[x] = False
    return [i for i in range(n) if is_prime[i]]

candidates = sieve_of_erathosthes(55)

t = int(input())
best = float("inf")

for _ in range(t):
    l = int(input())
    a = list(map(int, input().split()))

    for ai in a:
        for candidate in candidates:
            if gcd(candidate, ai) == 1:
                best = min(best, candidate)

    print("-1" if best == float("inf") else best)
