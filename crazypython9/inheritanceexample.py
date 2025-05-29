#class Superclass:

#class Subclass(Superclass): #ketu subclass trashegon prej superclass

class Animal:
    def eat(self):
        print("this animal eats")
    def sleep(self):
        print("guess what it sleeps")

class Bird(Animal):
    def fly(self):
        print("guess what it flies")
    def sings(self):
        print("it can sing?")

bilbuli=Bird()
bilbuli.sings()
bilbuli.fly()

