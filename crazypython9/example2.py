class Animal:
    def sound(self):
        print("some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("woof woof? i think it more like bark bark")

class Cat(Animal):
     def sound(self):
         print("meow")

kafshe=Animal()

kafshe.sound()

rex=Dog()
rex.sound()

tom=Cat()
tom.sound()