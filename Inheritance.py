from abc import ABC, abstractmethod 

# Base Class
class Animal(ABC):
    
    def __init__(self):
        pass

    def domain(self):
        pass

    def move(self):
        pass

    def funFact(self):
        pass

    def printStuff(self):
        print("Domain:",self.domain())
        print("Movement Method:",self.move())
        print("Fun Fact:",self.funFact())

# child class
class Bird(Animal):

    def __init__(self):
        print("Real bird stuff")

    def domain(self):
        return "The sky"

    def move(self):
        return "Flight"

    def funFact(self):
        return "The Eagles won the super bowl"

# child class
class Mammal(Animal):
    
    def __init__(self):
        print("Mammal gang")

    def domain(self):
        return "The land"

    def move(self):
        return "Walkin and shit"

    def funFact(self):
        return "The bible says God is a mammal"

# grandchild class
class Squirrel(Mammal):
    
    def funFact(self):
        return "God is a squirrel"

# grandchild class
class Dolphin(Mammal):
    
    def domain(self):
        return super().domain()+", but more so, water"

if __name__ == "__main__":
    bird = Bird()
    mammal = Mammal()
    squirrel = Squirrel()
    dolphin = Dolphin()
    print("\nBird stuff:")
    bird.printStuff()
    print("\nMammal stuff:")
    mammal.printStuff()
    print("\nSquirrel stuff:")
    squirrel.printStuff()
    print("\nDolphin stuff:")
    dolphin.printStuff()
