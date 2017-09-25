import os

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

# ask how many numbers they want
numFbValues = int(input("How many Fibunacci values should be found: "))

#loop while calling for each new number
i = 1

while i < numFbValues:

    fibValue =fib(i)

    print(fibValue)

    i += 1

print("All Done")

#print the result and increment