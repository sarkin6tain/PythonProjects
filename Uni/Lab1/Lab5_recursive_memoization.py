memo = {}

def get_fibonacci(fib):
    if memo.has_key(fib):
        return memo[fib]

    if fib == 0:
        return 0
    elif fib == 1:
        return 1
    res = get_fibonacci(fib - 1) + get_fibonacci(fib - 2)
    memo[fib] = res
    return res

for index in range (0, 101):
    print("{0} : {1}".format(index, get_fibonacci(index)))