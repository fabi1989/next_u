def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


for x in range(10):
    print(fib(x))

fib(8)
