# Operators in python
# Arithmetic Operator
num1 = 4
print(num1 + 4)
print(num1 - 4)
print(num1 * 5)
print(num1 / 4)
print(num1 // 4)
print(num1 ** 2)

# Comparison Operator
num2 = 10
print(num1 < num2)
num3 = 10
print(num3 >= 0)
print(num2 == num3)

# Logical Operator
# and

# creating a voting system for check the condition
'''wap for creating a admission system there check if
the student is male or his age is more then 19 then
allow for the admission'''

# if the both condition is required  for that we use and operator
# age_of_student = int(input("Enter your age "))
# gender = input("Give your gender please user small letter ")
# gender=gender.lower()
# print(gender)
# allowed_gender = "male"
# if age_of_student > 19 and gender == allowed_gender:
#     print("you are allowed for the admission")
# else:
#     print("You are not allowed for admission")
#
# # if any of these condition is required  for that we use or operator
# age_of_student = int(input("Enter your age "))
# gender = input("Give your gender please user small letter ")
# gender=gender.lower()
# print(gender)
# allowed_gender = "male"
# if age_of_student > 19 or gender == allowed_gender:
#     print("you are allowed for the admission")
# else:
#     print("You are not allowed for admission")

fruits = ["apple", "banana"]
empty_list = fruits

print(fruits is not empty_list)
#  false
print(fruits is empty_list)
# true
# assignment operator
var = 3
var //= 3

print(var)
# 1

# membership operator
# in
# not in

students_list = ["Akash", "Vikash", "Mahendr", "David", "Faizan", "Narandr"]
student_name="Akash1"
if student_name not in students_list:
    print("Student is present")
else:
    print("Student is absent")



