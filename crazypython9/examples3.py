class Animal:
    def __init__(self, name):#example for one construction and one variable which incoherent per kete klass
        self.name=name

    def sound(self):
        print("some generic animal sound")
    def description(self):
        print(f"this animal name is {self.name}")

class Dog(Animal):
    def __init__(self, breed,name):#in here is the construction  of the class and the variable of the class
        self.breed=breed # variable which value is only for this class
        super().__init__(name)# here we call the construction  of the superclasses
    def sound(self):
        print("woof woof? i think it more like bark bark")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self,color,name):
        self.color=color
        super().__init__(name)
    def sound(self):
         print("meow")

    def description(self):
        super().description()
        print(f"color:{self.color}")

rex=Dog("golden retriever", "Rex")
rex.sound()
rex.description()

cat=Cat("grey and black","tom and jerry")
cat.sound()
cat.description()