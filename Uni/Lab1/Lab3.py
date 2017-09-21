str_numbers = raw_input("Enter series ").split()
even = 0
odd = 0

try:
    for index in range(0, len(str_numbers)):
        number = int(str_numbers[index])

        if number % 2 == 0:
            even+=1
        else:
            odd+=1

    print ("Total even numbers: {0}".format(even))
    print ("Total odd numbers: {0}".format(odd))

except ValueError:
    print("Could not parse input '{0}' as int".format(str_numbers[index]))