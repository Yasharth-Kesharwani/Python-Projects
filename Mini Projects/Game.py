import random

#===========================================================================================================

def Game_Easy():


    print()
    print ("                                             Guess The Number")
    print ()
    print ("You will get 10 chances to guess a number between 1 - 50")

    rand = random.randint(1, 50)
    m = 1
    while m <= 10:
        try:
            print ()
            if m == 10:
                num = int(input("Your Last chance : "))
                if num == rand:
                    print()
                    print ("Congratulations! You guessed it")
                else:
                    print ()
                    print ("Sorry! Good Luck next time.")
                    print ("Better Luck Next Time.") 
                    print ("The Number was : " + str(rand))
                print()
                print(120 * "=")
                print()
                        
            else:
                num = int(input("Your " + str(m) + " chance : "))
                if num < 1 or  num > 50:
                    print ("Guess a Number between 1 - 50")
                elif rand == num:
                    print()
                    print ("Congratulations! You guessed it")
                    print()
                    print(120 * "=")
                    print()
                    break
                elif rand > num:
                    if rand - num <= 5:
                        print ("You're very close!")
                    elif rand - num <= 12:
                        print ("You are close !")
                    elif rand - num <= 30:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
                else:
                    if num - rand <= 5:
                        print ("You're very close!")
                    elif num - rand <= 12:
                        print ("You are close !")
                    elif num - rand <= 30:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
            m += 1  

        except ValueError :
            print("Only Number!")
            print()
            print(120 * "=")
            m += 1    

        except Exception as e:
            print(e)
            print()
            print(120 * "=")
            m += 1

def Game_Medium():


    print()
    print ("                                             Guess The Number")
    print ()
    print ("You will get 10 chances to guess a number between 1 - 100")

    rand = random.randint(1, 100)
    m = 1
    while m <= 10:
        try:        
            print ()
            if m == 10:
                num = int(input("Your Last chance : "))
                if num == rand:
                    print()
                    print ("Congratulations! You guessed it on your Last Chance.")
                    print()
                else:
                    print ()
                    print ("Sorry! You Lost.")
                    print ("Better Luck Next Time !") 
                    print ("The Number was : " + str(rand))
                    print()
                print(120 * "=")
                print()
                        
            else:
                num = int(input("Your " + str(m) + " chance : "))
                if num < 1 or  num > 100:
                    print ("Guess a Number between 1 - 100")
                elif rand == num:
                    print()
                    print ("Congratulations! You guessed it")
                    print()
                    print(120 * "=")
                    print()
                    break
                elif rand > num:
                    if rand - num <= 10:
                        print ("You're very close!")
                    elif rand - num <= 25:
                        print ("You are close !")
                    elif rand - num <= 60:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
                else:
                    if num - rand <= 10:
                        print ("You're very close!")
                    elif num - rand <= 25:
                        print ("You are close !")
                    elif num - rand <= 60:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
            m += 1  

        except ValueError :
            print("Only Number!")
            print()
            print(120 * "=")
            m += 1    

        except Exception as e:
            print(e)
            print()
            print(120 * "=")
            m += 1

def Game_Hard():


    print()
    print ("                                             Guess The Number")
    print ()
    print ("You will get 10 chances to guess a number between 1 - 150")

    rand = random.randint(1, 150)
    m = 1
    while m <= 10:
        try:            
            print ()
            if m == 10:
                num = int(input("Your Last chance : "))
                if num == rand:
                    print ()
                    print ("Congratulations! You guessed it")
                else:
                    print ()
                    print ("Wrong! Good Luck next time.") 
                    print ("The Number was : " + str(rand))
                print()
                print(120 * "=")
                print()
                        
            else:
                num = int(input("Your " + str(m) + " chance : "))
                if num < 1 or  num > 150:
                    print ("Guess a Number between 1 - 150")
                elif rand == num:
                    print()
                    print ("Congratulations! You guessed it")
                    print()
                    print(120 * "=")
                    print()
                    break
                elif rand > num:
                    if rand - num <= 15:
                        print ("You're very close!")
                    elif rand - num <= 36:
                        print ("You are close !")
                    elif rand - num <= 100:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
                else:
                    if num - rand <= 15:
                        print ("You're very close!")
                    elif num - rand <= 36:
                        print ("You are close !")
                    elif num - rand <= 95:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
            m += 1  

        except ValueError :
            print("Only Number!")
            print()
            print(120 * "=")
            m += 1    

        except Exception as e:
            print(e)
            print()
            print(120 * "=")
            m += 1
               
def Game_Insane():


    print()
    print ("                                             Guess The Number")
    print ()
    print ("You will get 8 chances to guess a number between 1 - 150")

    rand = random.randint(1, 150)
    m = 1
    while m <= 8:
        try:            
            print ()
            if m == 8:
                num = int(input("Your Last chance : "))
                if num == rand:
                    print()
                    print ("Congratulations! You guessed it")
                else:
                    print ()
                    print ("Wrong! Good Luck next time.") 
                    print ("The Number was : " + str(rand))
                print()
                print(120 * "=")
                print()
                        
            else:
                num = int(input("Your " + str(m) + " chance : "))
                if num < 1 or  num > 150:
                    print ("Guess a Number between 1 - 150")
                elif rand == num:
                    print()
                    print ("Congratulations! You guessed it")
                    print()
                    print(120 * "=")
                    print()
                    break
                elif rand > num:
                    if rand - num <= 15:
                        print ("You're very close!")
                    elif rand - num <= 36:
                        print ("You are close !")
                    elif rand - num <= 100:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
                else:
                    if num - rand <= 15:
                        print ("You're very close!")
                    elif num - rand <= 36:
                        print ("You are close !")
                    elif num - rand <= 95:
                        print ("You are far !")
                    else:
                        print ("You're very far !")
            m += 1  

        except ValueError :
            print("Only Number!")
            print()
            print(120 * "=")
            m += 1    

        except Exception as e:
            print(e)
            print()
            print(120 * "=")
            m += 1
               

#============================================================================================================

if __name__ == "__main__" :
    
    global play 
    play = 1
    while True:

        try:
            if play != 1:
                answer = str(input("Want to Play Again(Y, N) ? "))
                
                if answer.lower() == "no" or answer.lower() == "n":
                    break
                elif answer.lower() == "yes" or answer.lower() == "y":
                    pass
                else:
                    print("You have only Two option - Y or N")
                    print()  
                    continue
                print()

        except Exception :
            print("Wrong Input !")
            print()

        while True:

            try:
                Mode = str(input("Enter the Difficulty (Easy/Medium/Hard/Insane) : "))
                print()
                Mode = Mode.lower()

                if Mode == "easy" or Mode == "e":
                    play += 1
                    Game_Easy()
                    break
                elif Mode == "medium" or Mode == "m":
                    play += 1
                    Game_Medium()
                    break
                elif Mode == "hard" or Mode == "h":
                    play += 1
                    Game_Hard()
                    break
                elif Mode == "insane" or Mode == "i":
                    play += 1
                    Game_Insane()
                    break
                else:
                    print()
                    print("You have only three options - Easy, Medium, Hard and Insane")
                    print()  
                    continue         

            except Exception :
                print("Wrong Input !")
                print()

