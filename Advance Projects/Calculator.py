import pyttsx3
import sys
from math import sqrt
import cutie

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


            print("What do you want to do : ")
            speak("What do you want to do : ")

            opers = ["Factorial / Factorisation", "Square", "Cube", "Cube Root", "Square Root", "Addition", "Subtraction", "Multiplication", "Division", "Power", "Find Remainder", "Tetration", "Pentation", "Close"]
            oper = opers[cutie.select(opers, selected_index=0)]

            for m in range(0,15):
                sys.stdout.write("\033[F")  # Move cursor up one line
                sys.stdout.write("\033[K")  # Clear line
                sys.stdout.flush()          # Force it to update
            
            
            print(f"What do you want to do : {oper}")

            if oper == "Close":
                print()
                break
            print ()

            oper = str(oper).lower()


            ans = ""

            if oper == "!" or oper == "factorial" or oper == "factorisation" :
                print()
                print(f"Answer : {factorial(num_1)} ({factorial_2(num_1)})")
                speak(f"Your Answer is {factorial(num_1)}")
                
            elif oper == "^2" or oper == "square":
                print()
                ans = ("Answer : " + str(num_1 ** 2))
                
            elif oper == "^3" or oper == "cube"or oper == "find cube":
                print()
                ans = ("Answer : " + str(num_1 ** 3)) 
                            
            elif oper == "√" or oper == "sqrt"or oper == "square root"or oper == "find square root":
                print()
                ans = ("Answer : " + str(sqrt(num_1)))
                
            elif oper == "∛" or oper == "cube root" or oper == "find cube root" :
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

                if oper == "+" or oper == "add" or oper == "addition":
                    ans = ("Answer : " + str(num_1 + num_2))

                elif oper == "x" or oper == "*" or oper == "multiply" or oper == "multiplication" :
                    ans = ("Answer : " + str(num_1 * num_2))

                elif oper == "-" or oper == "subtraction" or oper == "subtract" :    
                    ans = ("Answer : " + str(num_1 - num_2))

                elif oper == "/" or oper == "÷" or oper == "divide" or oper == "division":
                    ans = ("Answer : " + str(num_1 / num_2))

                elif oper == "**" or oper == "^" or oper == "power" or oper == "powers":
                    ans = ("Answer : " + str(num_1 ** num_2))

                elif oper == "%" or oper == "remainder" or oper == "find remainder":
                    ans = ("Answer : " + str(num_1 % num_2))

                elif oper == "//" or oper == "quotient" or oper == "find quotient":
                    ans = ("Answer : " + str(num_1 // num_2))

                elif oper == "↑↑" or oper == "***" or oper == "Tetration" or oper == "tetration":
                    ans = ("Answer : " + str(tetrate(num_1, num_2)))

                elif oper == "↑↑↑" or oper == "****" or oper == "Pentation" or oper == "pentation" :
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
