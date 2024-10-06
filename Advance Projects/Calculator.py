import pyttsx3
from math import sqrt

#Functions=====================================================================================================

def speak(text: str): 
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def cube_root(num):
    if num < 0:
        num_1 = num - (num + num)
        a = pow(num_1, (1/3)) #return to change the value given
        return (a - (a + a))
    elif num == 0:
        return 0 
    else:
        return pow(num, (1/3))
 

def factorial(n: int):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

def factorial_2(m: int):    # To return in string
    if (m == 1 or m == 0):
        return 1
    return f"{m} * {factorial_2(m-1)}"


def tetrate(a, b):
    m = 1
    while (m < b):
        a = a ** a
        m += 1
    return a

def pentate(a: int, b: int):
    m = 1
    while (m < b):
        a = tetrate(a, a)
        m += 1
    return a

#============================================================================================================
#Commands
if __name__ == "__main__":
    
    while True:
        print ("                                         Calculator ")
        print ()
        print("To Quit enter 'Q' \n")

        try:
            speak("Enter the First Number : ")
            num_1 = (input("Enter the First Number : "))
            if num_1 == "Q" or num_1 == "q":
                print()
                break

            print ()
            num_1 = float(num_1)

            speak("What do you want to do : ")
            oper = (input("What do you want to do : "))
            if oper == "Q" or oper == "q":
                print()
                break
            print ()
            oper = str(oper)

            ans = ""

            if oper == "!" or oper == "Factorial" or oper == "factorial" or oper == "FACTORIAL" or oper == "factorisation" :
                print()
                print(f"Answer : {factorial(num_1)} ({factorial_2(num_1)})")
                speak(f"Your Answer is {factorial(num_1)}")
                
            elif oper == "^2" or oper == "Square" or oper == "square" or oper == "Find Square" or oper == "Find square" or oper == "find square" or oper == "SQUARE" or oper == "FIND SQUARE":
                print()
                ans = ("Answer : " + str(num_1 ** 2))
                
            elif oper == "^3" or oper == "Cube" or oper == "cube" or oper == "Find Cube" or oper == "Find cube" or oper == "find cube" or oper == "CUBE" or oper == "FIND CUBE":
                print()
                ans = ("Answer : " + str(num_1 ** 3)) 
                            
            elif oper == "√" or oper == "Square Root" or oper == "sqrt" or oper == "Find Square Root" or oper == "SQUARE ROOT" or oper == "square root" or oper == "Find SQUARE ROOT" or oper == "find square root" or oper == "Find sqrt" or oper == "FIND SQUARE":
                print()
                ans = ("Answer : " + str(sqrt(num_1)))
                
            elif oper == "∛" or oper == "Cube Root" or oper == "cube root" or oper == "Find Cube Root" or oper == "Find cube root" or oper == "find cube root" or oper == "CUBE ROOT" or oper == "FIND CUBE ROOT":
                print()
                ans = ("Answer : " + str(cube_root(num_1))) 
                
            else :
                speak("Enter the Second Number : ")
                num_2 = input("Enter the Second Number : ")
                if num_2 == "Q" or num_2 == "q":
                    print()
                    break
                print ()
                print ()
                num_2 = float(num_2)

                if oper == "+" or oper == "Addition" or oper == "Add" or oper == "add" or oper == "addition":
                    ans = ("Answer : " + str(num_1 + num_2))

                elif oper == "x" or oper == "*" or oper == "Multiply" or oper == "multiply" or oper == "Multiplication" or oper == "multiplication" or oper == "MULTIPLY" or oper == "MULTIPLICATION":
                    ans = ("Answer : " + str(num_1 * num_2))

                elif oper == "-" or oper == "Subtract" or oper == "subtract" or oper == "Subtraction" or oper == "subtraction"or oper == "SUBTRACT" or oper == "SUBTRACTION":    
                    ans = ("Answer : " + str(num_1 - num_2))

                elif oper == "/" or oper == "÷" or oper == "Divide" or oper == "divide" or oper == "Division" or oper == "division" or oper == "DIVISION" or oper == "DIVIDE":
                    ans = ("Answer : " + str(num_1 / num_2))

                elif oper == "**" or oper == "^" or oper == "Power" or oper == "power" or oper == "Powers" or oper == "powers"or oper == "POWER" or oper == "POWERS":
                    ans = ("Answer : " + str(num_1 ** num_2))

                elif oper == "%" or oper == "Remainder" or oper == "remainder" or oper == "Find Remainder" or oper == "Find remainder" or oper == "find remainder"or oper == "REMAINDER" or oper == "FIND REMAINDER":
                    ans = ("Answer : " + str(num_1 % num_2))

                elif oper == "//" or oper == "Quotient" or oper == "quotient" or oper == "Find Quotient" or oper == "Find quotient" or oper == "find quotient" or oper == "QUOTIENT" or oper == "FIND QUOTIENT":
                    ans = ("Answer : " + str(num_1 // num_2))

                elif oper == "↑↑" or oper == "***" or oper == "Tetration" or oper == "tetration" or oper == "TETRATION":
                    ans = ("Answer : " + str(tetrate(num_1, num_2)))

                elif oper == "↑↑↑" or oper == "****" or oper == "Pentation" or oper == "pentation" or oper == "PENTATION":
                    ans = ("Answer : " + str(pentate(num_1, num_2)))

                else:
                    print ("Wrong Operator (ERROR)")
                    continue

            print(ans)
            speak(f"Your {ans}")

            input()

        except ZeroDivisionError:
            print("Division by Zero is not allowed")
            print()
            
        except ValueError:
            print("Entered value is Invalid")
            print()
            
        except RecursionError:
            print("Maximum Factorial limit is '999' ")
            print()

        except Exception as e:
            print(e)
            print()

        print(120 * "=")
        print()
        

#END==================================================================================================================================================================================================
