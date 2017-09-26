# static method - access w/o the need to initialise the class
# mainly used as utility method or when a real world object makes no sense to perform a task

class Sum:

    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

def main():
    print("Sum:", Sum.getSum(1,2,3,4,5))

main()