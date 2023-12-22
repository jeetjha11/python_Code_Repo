# compile time polymorphism
# compile time polymorphism is achieved by the use
# of method overloading
# ex:
# in python it is not following the traditional way for method overloading
# if you want to overload the method
# you need to implement the logic according to your parameter

name = None
print(name)


class Calculator:

    def add(self, number1, number2, number3=None, number4=None):
        if number3 is not None and number4 is None:
            print(number1 + number2 + number3)
        elif number4 is not None and number3 is not None:
            print(number1 + number2 + number3 + number4)
        else:
            print(number1 + number2)

    # def add(self,number1,number2):
    #     print(number1+number2)
    #
    # def add(self,number1,number2):
    #     print(number1+number2)


calculator = Calculator()
calculator.add(1, 2, 3, 3)


class Animal:
    def sound(self):
        print("Animal Sound")


class Cat(Animal):
    def sound(self):
        print("Meow Meow")


class Dog(Cat):
    def sound(self):
        print("Bhow Bhow")


cat = Cat()
cat.sound()
dog=Dog()
dog.sound()



