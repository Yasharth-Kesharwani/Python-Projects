#String Features
# {var} --- Instead of '+' (only in f string)
# '\n' --- For new line
# '\t' --- For space till next tab
#  \"  --- For double inverted comma
#  \'  --- For single inverted comma

print("Hello Coder\nHow are You?")

print("Hello Yasharth\t W0W! \n")

print()

#========================================================================================
#Walrus Operator -- :=

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long,[{n} elements, expected <= 3]")
print()    

#========================================================================================
#Type Defination

n: int = 22
name: str = "name"

def sum(a: int, b: int) -> int:
    return a + b

print(sum(n, 23))
print()

#========================================================================================
#Match Case ---- switch of java

def TVerror(status: int):
    match(status):
        case 150:
            return "Bad Connection from Delhi"
        case 200:
            return "Electricity Problem"
        case 140:
            return "Recharge not Done"
        case _:
            return "Unknown Status"

print(TVerror(150))
print()
#=========================================================================================
#Dict Merge

Dict1 = {"a" : 1, "b" : 2}
Dict2 = {"c" : 3, "d" : 4}
Merge = Dict1 | Dict2

print(Merge)
print()
#=========================================================================================
#Exception Handling --- try except
#All exceptions come in Exception

try:
    a = int(input("Hey, Enter a Number : "))
    print(a)

except ValueError as v:
    print(v)
except Exception :
    print("Hey, Enter a valid Number ")

print("OK")
print()
#=========================================================================================
#Try with else

try:
    b = int(input("Hey, Enter a Number : "))
    print(b)

except Exception :
    print("Hey, Enter a valid Number ")

else:
    print("OK")   #Execute when try works

print()
#=========================================================================================
#Try with finally

try:
    b = int(input("Hey, Enter a Number : "))
    print(b)

except Exception :
    print("Hey, Enter a valid Number ")

finally:
    print("OK")   #Always Execute breaking all rules (return also)

print()
#========================================================================================
#Exception Raise
'''
b = 0

if b == 0:
    raise ZeroDivisionError("Hello")
'''
#========================================================================================
#Importing

from Calculator import cube_root # Importing from another file
print(cube_root(10))

print()
#========================================================================================
#Global Keyword

a = 89

def fun():
    global a  #Give the value of 'a' outside the function also
    a = 3
    print(a)

print(a)
fun()

print()
#========================================================================================
#Enumerate Function -

l = [41, 23, 12, 87]

# index = 0
# for item in l:
#     print(f"The item at index {index} is {item}")
#     index += 1

# This can be simplified with enumerate function

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")

print()
#=========================================================================================
#List Comprehension

numlist = [1, 2, 6, 4, 9]

# squaredList = []
# for item in numlist:
#     squaredList.append[item*item]

squaredList = [i*i for i in numlist]

print(squaredList)

print()
#=========================================================================================

