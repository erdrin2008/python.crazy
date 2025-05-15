total=0

for number in range(1,11):
    if number%2==0:
        total+=number
print("the sum of even number from 1 to 10 is",total)

#this is defining a function, keyword def- in python defines functions,greet - name of function
def greet():
    print("hello world!")
#this is how wew use the function
greet()

def greet_person(name):
    print("hello", name)

greet_person("alma")

def shuma(x,y): #this type of function it returns something but in this case it returns a number
    z=x+y
    return z
resultati=shuma(3,4)
print("3+4=",resultati)

#local variable - variablat e deklaruara lokalishte perbrenda nje funksioni
def greet(name):
    message=f"hello,{name}!"
    print(message)
    greet("alma")


#print(message) - this outputs an error because the message variable is defined only for the function 😑

#argumentet dhe definimi i tyre
def greet_person(name, greeting="😑"):
    messages=f"{greeting}, {name}"
    return messages
default_greeting=greet_person("alma")
print(default_greeting)
custom_greeting=greet_person("alma","😑")
print(custom_greeting)



hello="hi"
def greet_people(name):
    global hello
    return f"{hello}, {name}"
variabla=greet_people("alma")
print(variabla)
