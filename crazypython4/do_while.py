
while True:
    user_input=input("enter a positive number:")
    if user_input.isnumeric():
        number=int(user_input)
        if number>0:
            break
    print("invalid input please try again and put the correct input")
print("you have enter an valid positive number",number)