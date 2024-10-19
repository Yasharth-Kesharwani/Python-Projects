import random

def Quiz():
    print("                                    Maths Quiz\n")
    print("You'll get 10 questions to answer.\n")
    point = 0
    q_no = 1
    while q_no <= 10:
        try:
            q = random.randint(1, 6)
            one = random.randint(1, 500)
            two = random.randint(1, 400)
            three = random.randint(1, 101)
            four = random.randint(1, 11)
            five = random.randint(1, 4)
            if q == 1:
                print(f"{q_no}. What is {one} + {two} ?")
                ans = input("Answer : ")
                a = one + two
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif q == 2 and three % four == 0:
                print(f"{q_no}. What is {three} / {four} ?")
                ans = input("Answer : ")
                a = three/four
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif q == 3 and one > two:
                print(f"{q_no}. What is {one} - {two} ?")
                ans = input("Answer : ")
                a = one - two
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif q == 4:
                print(f"{q_no}. What is {three} x {four} ?")
                ans = input("Answer : ")
                a = three*four
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif q == 5  and five != 1:
                if five == 2:
                    print(f"{q_no}. What is the square of {four} ?")
                    ans = input("Answer : ")
                    a = four*four
                    if int(ans) == a:
                        print("Correct!\n")
                        point += 1
                    else :
                        print(f"Wrong! ({a})\n")
                else:
                    print(f"{q_no}. What is the cube of {four} ?")
                    ans = input("Answer : ")
                    a = four*four*four
                    if int(ans) == a:
                        print("Correct!\n")
                        point += 1
                    else :
                        print(f"Wrong! ({a})\n")
            else :
                continue
            
            q_no += 1
        except Exception as e:
            print(f"{e}\n")
            q_no += 1

    print("Your Score : " + str(point) +"\n")


#================================================================================================

if __name__ == "__main__":

    Quiz()

    while True:
            
        try:

            answer = str(input("Want to Play Again(Y, N) ? "))
                
            if answer.lower() == "no" or answer.lower() == "n":
                break
            elif answer.lower() == "yes" or answer.lower() == "y":
                Quiz()
            else:
                print("You have only Two option - Y or N")
                print()  
                continue
            print()

        except Exception :
            print("Wrong Input !")
            print()

