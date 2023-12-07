def add():
    print("adding two numbers")


def sub():
    print("sub two numbers")


def mul():
    print("multipling two numbers")


def default():
    print("this is the default")


def switch_case(option):
    switch_dict = {
        1: add,
        2: sub,
        3: mul
    }

    operation = switch_dict.get(option, default)
    operation()


while True:
    print("1. add\n"
          "2. sub\n"
          "3. mul\n"
          "4. Exit")
    input_value = int(input("Please choose an options: "))
    if input_value == 4:
        break
    switch_case(input_value)
