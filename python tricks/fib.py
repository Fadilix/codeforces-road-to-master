def fibo(n, dct={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in dct:
        return dct[n]
    
    dct[n] = fibo(n - 2) + fibo(n - 1)
    return dct[n]

# print(fibo(0))
# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))
# print(fibo(5))
# print(fibo(6))
# print(fibo(7))
# print(fibo(8))
# print(fibo(9))
# print(fibo(10))

n = 5
fib = 0 * (n + 1)
print(fib)