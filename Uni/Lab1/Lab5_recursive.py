def get_fibonacci(fib):
    if fib == 0:
        return 0
    elif fib == 1:
        return 1
    return get_fibonacci(fib - 1) + get_fibonacci(fib - 2)

for index in range (0, 100):
    print("{0} : {1}".format(index, get_fibonacci(index)))