# Object Oriented Programming
# Real World Objects : Attributes & capabilities
# Dog Attributes (Fields / Variables) : HEight, Weigh, Faborite Food
# Dog Capabilities (Methods / Function): Run, Walk, Eat

class Dog:
    dogCount = 0
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
        Dog.dogCount += 1

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

#used to count the number of class (dogs) created
    @staticmethod
    def GetTotaldogCount():
        print("Number of dogs: {}".format(Dog.dogCount))


def main():
    spot = Dog("Spot", 66, 23)

    spot.bark()

    bowser = Dog()

    bowser.name = "bowser"

    bowser.bark()

    sissy = Dog("Sissy", 70, 20)

    sissy.eat()

    Dog.GetTotaldogCount()
# W/o main file won't run; Use main to load tut9 in another file
main()
