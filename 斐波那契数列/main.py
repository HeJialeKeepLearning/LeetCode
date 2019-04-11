def Fibonacci(n):
    k, a, b = 0, 0, 1
    while k < n:
        a, b = b, a + b
        k += 1
        yield a

for i in Fibonacci(3):
    print(i)
