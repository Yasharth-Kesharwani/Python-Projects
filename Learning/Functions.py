#Functions - 

def greet():
    print("Good Day")

a =greet()
print()

#==============================

def greet_2(name, end):
    print("Good Day, " + name)
    print(end)

greet_2("Yashingo", "Thanks")
print()

#==============================

def greet_3(name, end = "Thank You"):    #If end is not provided end will be Thak You
    print("Good Day, " + name)
    print(end)

greet_3("Yashingo")
print()

#==============================

def sum(a: int,b: int):
    c = a + b
    return c
    print("Not Reachable") # return ends the function and provides value 

print(sum(6,5))

#==============================

def factorial(n: int):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

i = int(input("Enter the Number : "))

print(f"The Factorial of {i} : \n")
