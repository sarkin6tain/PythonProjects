# Object Oriented Programming
# Real World Objects : Attributes & capabilities
#Dog Attributes (Fields / Variables) : HEight, Weigh, Faborite Food
#Dog Capabilities (Methods / Function): Run, Walk, Eat

class Dog:

    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.heigh = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
         print("{} the dog barks".format(self.name))


def main():
    spot = Dog("Sport", 66, 23)

    spot.bark()

    bowser = Dog()



    bowser.name = "bowser"

    bowser.bark()

main()