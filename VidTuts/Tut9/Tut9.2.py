import random
import math

# Warrior & Battle Class
#Warriors will have names, health, and attack and block maximums
# Capabilities: they will attack and block random amounts

#Attack random() 0.0 to 1.0 * maxAttack + .5

# Block will use random()

class Warrior:

    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

# Battle class capability of looping until one warrior dies
#Warriros will each get a turn to attack each other (loop inside of a method)


class Battle:

    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    # Function gets 2 warriors
    # 1 warrior attacks the other
    # Attacks and Blocks be integers
    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttkAmount = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmount - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,warriorB.name,damage2WarriorB))

        print("{} is down to {} health".format(warriorB.name,warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():

    maximus = Warrior("Maximus", 50, 20, 10)

    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus,galaxon)

main()

