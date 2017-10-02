# static method - access w/o the need to initialise the class
# mainly used as utility method or when a real world object makes no sense to perform a task

class Sum:

    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

    @staticmethod
    def getSumAlt(input1, input2, input3, input4):
        return input1 + input2 + input3 + input4

    @staticmethod
    def getSumAlt2(inputArr):

        sum = 0

        for variable in inputArr:
            sum += variable

        return sum


def main():
    print("Sum:", Sum.getSum(1,2,3,4,5))

    print("Sum:", Sum.getSumAlt2([1, 2, 3, 4, 5, 6, 7, 8]))

    print("Sum:", Sum.getSumAlt(1, 2, 3, 4))

main()