
# file = open("Input_T.txt")
# print(file.read())
# file.close()

# This same can be written using with statement :

with open("Input_T.txt") as file:
    print(file.read())

# It will automatically close the file