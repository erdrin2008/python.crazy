from crazypython5.functionexamples import resultati


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 == 0:
            raise ValueError("Cannot divide by zero.")
        else:
            return number1 / number2
    else:
        raise ValueError("Invalid operator. Use '+', '-', '*', or '/'.")

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter an arithmetic operation (+, -, *, /): ")
    resultati=calculate(number1,number2,operator)
    print(f"the result of {num1} {operator} {number2}:{resultati}")
except ZeroDivisionError as e:
    print()