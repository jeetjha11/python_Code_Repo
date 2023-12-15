# WAP for get the type of given input

# swap the to variables value without using temporary variable

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# WAP to find the names of the player which is starting by the
# n latter
players_list = []
size = 0
size = int(input("how many players you want in the list: "))

for var in range(0, size):
    players_name = input(f"Please enter the {var} name of the player: ")
    players_list.append(players_name)

result_list = []
for player in players_list:
    temp_player = player.lower()
    if temp_player.startswith("n"):
        result_list.append(player)

# displaying the list of names which is start by the n
print("Here the names of players which start by N/n")
for data in result_list:
    print(data)

# value1=int(input("Enter the first number: "))
# # 2
# value2=int(input("Enter the second number: "))
# #  this is overriding the value
# print(value1,value2)
# value1=value1+value2
# # 5     2+3
# value2=value1-value2
# # 2      5-3
# value1=value1-value2
# # 3       5-3
# print(value1,value2)
#
# ss="JSDFSDFSDFSFSDF"
# resul=ss.lower()
# print(resul)
