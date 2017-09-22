def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


for i in range(1, 101):
    print(fib(i))
