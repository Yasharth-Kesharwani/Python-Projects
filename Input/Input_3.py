#=========================================================================================================

file = open("Input_T.txt", "r") 
# lines = file.readlines()  # Lines is a list 
# print(lines, type(lines))

# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# line4 = file.readline()
# line5 = file.readline()

# print(line1, type(line1))
# print(line2, type(line2))
# print(line3, type(line3))
# print(line4, type(line4))
# print(line5, type(line5)) # Blank

line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()

file.close()

#=========================================================================================================