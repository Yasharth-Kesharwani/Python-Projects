#NOTES

#13 - Integer = Int
#13.0 - Decimal = Float
#print ("My age =" + age)--------Concetanation
#int()----Integer                  
#float()----Decimal                
#str()----String                   
#bool()----Boolean----True or False
#exit()----To break the program
#variable.upper()----Capital Letters----Methods
#variable.lower()----Small Letters             
#"String".upper()----Capital Letters
#variable.replace(a, b)----Replace
#variable.find(ab)-----Tells the Index
#print,input-----Keywords
#(5 // 2)----Answer in Integer
#(5 % 2)----To Find Remainder
#(5 ** 2)----For Powers
#var = var + 4
#var += 4----Shortcut----Same as above
#<,>,=,<=------Comparision Operators
#!----NOT
#(5 != 2)----Not equal to
#or, and, not ----Logical Operator
#if 5 > 2:
#elif----else if
#i = 1      ]
#while i < 5]-----Infinite Loop
#print(i)   ]
#10 * "*"----string
#while m > 10:      ]-----Loops
#for name in names: ]
#marks = [56, 45, 34, "math"]----List----Changeable
#list.append----To  Add Anything
#list.insert----To  Add Anything at a Particular Index
#len()------Number of Elements 
#break-----End
#continue-----Skip
#(56, 67, 57, "hey")----Tuple-----Not Changeable
#{45, 34, 64, "hello"}----Set-----No Duplicate-----No Index/Unordered
#{"Chemistry" : 24, "English" : 20 }----Dictionary-----For Pairs
#list--[], tuple--()/  , dictionary--{}, set--{}
#Integers          ]
#Floats            ]
#Strings           ]------ Primitive Data Types
#Booleans          ]
#------------------------
#Lists             ]
#Tuples            ]
#Dictionaries      ]------ Non-Primitive/Complex Data Types
#Sets              ]

#                                  FUNCTIONS
#        ______________________________|__________________________________
#       |                              |                                  |
#  In-built Functions         Module Functions                User-Defined Functions

#int(),str(),bool(),print(),pow(),round()----In-built Function
 
#Module ---- cv2, math
#import math ----Module
#from math import sqrt -----Module Function
#from math import * --------all modules obtained

# def function_name (parameters / values): ------Syntax of User-Defined Functions --- Function definition
#   what to do

# def print_sum (first, second):  -----Example --- Function definition
#    print(first + second)
# sum(a, b) ---- Function  Call

#======================================================================================================
#VARIABLE

first_name = "Yasharth"
last_name = "Kesharwani"
age = 13
is_adult = False
sir = "Rahul Sir"
try_ = "Hello".replace('Hello', 'Bye')
fir = 76

#======================================================================================================
#First Part-------Basics

print ("My Name is " + first_name , last_name)
print ("My age =" , str(age))
print ("I'm adult = " + str(is_adult))
#======================================================================================================
#Second Part-----Input

your_name = input("Tell your Name : ")
Age = input("Tell your age : " )
AGE = int(Age)
print ("Hello " + your_name , ",I'm" , first_name)
print ("Your age = " + str(Age))
print ("You're Adult = " + str(AGE >= 18))
print ("Nice to meet you")
print (try_)
#=======================================================================================================
#Third Part-----Strings

print (sir.upper())
print (sir.lower())
print (sir.find('ul'))
print ("RAHUL".lower())
print (sir.replace('Rahul','Amber'))
print ("Rahul" in sir)
print ("rahul" in sir)

#========================================================================================================
#Fourth Part------Operations

first_num = float(input("Enter the First Number : "))
sec_num = float(input("Enter the Second Number :"))
print ("Division : " + str(first_num / sec_num))
print ("Subtraction : " + str(first_num - sec_num))
print ("Multiplication : " + str(first_num * sec_num))
print ("Addition : " + str(first_num + sec_num))
print ("Remainder : " + str(first_num % sec_num))
print ("Power : " + str(first_num ** sec_num))
#========================================================================================================
#Fifth Part------Operators

print (5 > 2)
print (5 < 2 or 5 > 2)
print (5 == 2)
print (not 5 != 2)
print ("hello" == "hello")
print (fir == fir)
#===============================================================================================================================================================================================================
#Sixth Part------Loops

print (range(5))
i = 1
while i <= 30:
    print(i)
    i += 1 

m = 1
k = 9
while m < 10:
    print ("            " + m * " " +  m * "*" + "                          " + k * " " + m * "*" + "                          " + k * " " + m * "*" + "                          " + k * " " + m * "*")
    m += 1
    k -= 1

print ("*******************************" + "     " + "*******************************" + "     " + "*******************************" "     " + "*******************************")
print ("*******************************" + "     " + "*******************************" + "     " + "*******************************" "     " + "*******************************")

m = 9
k = 1
while m > 0:
    print ("            " + m * " " + m * "*" + "                          " + k * " " +  m * "*" + "                          " + k * " " + m * "*" + "                          " + k * " " + m * "*")
    m -= 1
    k += 1

input()

for item in range(5):
    print(item)
#================================================================================================================================================================================================================
#Seventh Part------Lists

marks = [45, 34, 32, "ret"]
print (marks[0])
print (marks[-1])
print (marks[0:2])

for score in marks:
    print (score)

mark = [45, 65, 43]
mark.append(12)
mark.insert(1 ,0<12)
print(mark)

num = [78, 79, 54, "hel"]
print (79 in num)
print (len(num))

y = 0
while y < len(num):
    print(num[y])
    y += 1

num.clear()
print(num)

names = ["atharv","armaan","yasharth","ansh","akshay","akshaj","saksham"]

for name in names:
    if name == "yasharth":
        continue
    if name == "akshay":
        break
    print (name)

#==============================================================================================================
#Eighth Part-----Tuples, Sets, Dictionaries
#Tuples

tuple = (99, 33, 56, 99, "hello")
print (tuple.count("hello"))
print (tuple.index(56))
print (len(tuple))
#--------------------------------------------
#Sets

set = {99, 33, "hello", 99, 56, 34}
print (set)
print (set.add(79))
print (set.remove(34))
print (set.discard(33))
#--------------------------------------------
#Dictionaries

diction = {"Chemistry" : 24, "English" : 20 }
print (diction["Chemistry"])
diction["Physics"] = 23
print (diction)
diction["Physics"] = 22
print (diction)
#==============================================================================================================
