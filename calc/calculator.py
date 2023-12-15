# Creating a dynamic calculator
"""
    features:
    adding
    subtraction
    multiplication
    division
    moduls
    percentage
"""


# add function
def add(number1, number2):
    return number1 + number2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return "Please Enter something else causer 0 is not acceptable"
    return num1 / num2


def mod(num1, num2):
    return num1 % num2


def percentage(num, percent):
    result = num * percent / 100
    return result


print("................WELCOME..................")

while True:
    print("Please Choose Options...")
    print("1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. moduls\n"
          "6. Percentage\n"
          "7. Exit to the Application")

    choice = int(input())
    if choice == 1:
        number1 = float(input("Please Enter the First number: "))
        number2 = float(input("Please Enter the Second number: "))
        result = None
        result = add(number1, number2)
        print("Sum is: ", result)
    elif choice == 2:
        number1 = float(input("Please Enter the First number: "))
        number2 = float(input("Please Enter the Second number: "))
        result = None
        result = sub(number1, number2)
        print("Subtraction is: ", result)
    elif choice == 3:
        number1 = float(input("Please Enter the First number: "))
        number2 = float(input("Please Enter the Second number: "))
        result = None
        result = mul(number1, number2)
        print("Multiplication is: ", result)

    elif choice == 4:
        number1 = float(input("Please Enter the First number: "))
        number2 = float(input("Please Enter the Second number: "))
        result = None
        result = div(number1, number2)
        if type(result)==str:
            while number2==0:
                print(result)
                number2 = float(input("Please Enter the Second number: "))
        result=div(number1,number2)
        print("Division is: ", result)

    elif choice == 5:
        number1 = float(input("Please Enter the First number: "))
        number2 = float(input("Please Enter the Second number: "))
        result = None
        result = mod(number1, number2)
        print("Moduls is: ", result)

    elif choice == 6:
        number1 = float(input("Please Enter the number: "))
        number2 = float(input("Please Enter the percent amount you want: "))
        result = None
        result = percentage(number1, number2)
        print("Percentage is: ", result)
    elif choice == 7:
        print("Thank You")
        break
    else:
        print("Please Enter the Valid Choice")
