# # creating a variable
# # variable_name=variable_value
# var = 2
# # datatypes
# # 1.
# print(var)
# float_var = 1.2
# print("Decimal value", float_var)
# # 2. sequence type:
#
# str_var = "Any value"
# print("Printing string", str_var)
#
# # list data type
# list1 = [1, 2, 3, 3, 4, 5, "dasnjakdnjkandkjandjka", 3, 2, 2]
# # index  0  1  2  3  4  5  6  7  8  9
# # print(list1[6])
# # inbuilt methods for performing operations
# # ho to add a data into the list
# fruits = ["apple", "banana", "grapes"]
# print("Oldest list", fruits)
# fruits.append("orange")
# updated_list = fruits
# print("Updated_list", updated_list)
# # sorting a list
# # fruits.sort()
# # print("Sorted List", fruits)
# # fruits.pop(2)
# # print("after pop", fruits)
#
# # tuple
# tuple_1 = (1, 2, 3, 4, 5, 6)
# print(tuple_1)
# var = tuple_1.index(6)
# print("Number of element in the tuple are", var)
#
# # boolean
# user_value = input("Enter the value: ")
# # user_value=True
# is_authenticated = user_value.lower() == "true"
# #                    false==true->False
# print(type(is_authenticated))
# #  why the input value is giving True even we are passing the inputs as False
# if is_authenticated:
#     print(type(is_authenticated))
#     print("Welcome to the library you are allowed")
# else:
#     print("You are not allowed for the library")
#
# # set data types
# # set_types = {1, 2, 3, 4, 3, 1, 3, 4, 4, 4, 4, 4}
# # print(type(set_types))
# # print(set_types)
#
# # mapping data_types
#
# dict_type = {
#     # key    value
#     "name": "Akash",
#     "age": 24,
#     "address": "Bhopal",
#     "education": "B.tech"
# }
# dict_type.update({"pass_out": "2022"})
# print(dict_type)
# name = ""
# designation = ""
#
#
# list_of_team_1_front_end = []
# list_of_team_2_backend = []
# for val in range(1, 4):
#     name = input("Enter the name: ")
#     designation = input("Enter the Designation: ")
#     structure_of_team = {
#         "name": name,
#         "designation": designation
#     }
#     list_of_team_1_front_end.append(structure_of_team)
#
# for val in range(1, 4):
#     name = input("Enter the name: ")
#     designation = input("Enter the Designation: ")
#     structure_of_team = {
#         "name": name,
#         "designation": designation
#     }
#     list_of_team_2_backend.append(structure_of_team)
#
# user_t_find=input("Please enter the name of employee which you want to find")
#
# print(list_of_team_1_front_end)
# print(list_of_team_2_backend)


def greetings(name):
    # it is taking a name in parameter and making a greetings messages
    message = f"Hello {name} Good Morning!!"
    return message


def adding_dict_value(user_name, age, address):
    user_dict = {
        "user_name": user_name,
        "age": age,
        "address": address,
    }
    return user_dict


user_name = input("Enter the name: ")
age = int(input("Enter the age: "))
address = input("Enter the address: ")
result=adding_dict_value(user_name,age,address)
print("Dict is ",result)
# name = input("Enter your name: ")
# result_message = greetings(name=name)
# print(result_message)
