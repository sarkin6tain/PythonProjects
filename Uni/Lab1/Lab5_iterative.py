fib1 = 0
fib2 = 1
fib3 = 0

print(fib1)
print(fib2)

for index in range(0, 100):
    fib3 = fib1 + fib2
    print(fib3)
    fib1 = fib2
    fib2 = fib3