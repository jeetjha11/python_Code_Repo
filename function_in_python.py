# functions
#  define a function for addition of two numbers
number1 = 5
number2 = 10
add = number1 + number2


# print(add)


def addition_of_two_numbers(num1, num2):
    add = num1 + num2
    return add


result = addition_of_two_numbers(number1, number2)
print("Result of addition is: ", result)

# input: please enter the name,please enter the message like: good mornng/
# :
#  create 4 functions who return those messages  to the user

name = input("Enter the name: ")
greetings_message = input("Enter the greetings message: \n"
                          "EX- Good Morning\n")


def greet_message(name, greet_message):
    result = f"Hello {name} {greet_message}"
    return result


message = greet_message(name, greetings_message)
print(message)
