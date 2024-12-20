import random
import cutie

def Quiz():
    print("                                    Maths Quiz\n")
    print("You'll get 10 questions to answer.\n")
    point = 0
    ques_no = 1
    while ques_no <= 10:
        try:
            ques = random.randint(1, 6)
            one = random.randint(1, 500)
            two = random.randint(1, 400)
            three = random.randint(1, 101)
            four = random.randint(1, 11)
            five = random.randint(1, 4)
            if ques == 1:
                print(f"{ques_no}. What is {one} + {two} ?")
                ans = input("Answer : ")
                a = one + two
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif ques == 2 and three % four == 0:
                print(f"{ques_no}. What is {three} / {four} ?")
                ans = input("Answer : ")
                a = three/four
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif ques == 3 and one > two:
                print(f"{ques_no}. What is {one} - {two} ?")
                ans = input("Answer : ")
                a = one - two
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif ques == 4:
                print(f"{ques_no}. What is {three} x {four} ?")
                ans = input("Answer : ")
                a = three*four
                if int(ans) == a:
                    print("Correct!\n")
                    point += 1
                else :
                    print(f"Wrong! ({a})\n")
            elif ques == 5  and five != 1:
                if five == 2:
                    print(f"{ques_no}. What is the square of {four} ?")
                    ans = input("Answer : ")
                    a = four*four
                    if int(ans) == a:
                        print("Correct!\n")
                        point += 1
                    else :
                        print(f"Wrong! ({a})\n")
                else:
                    print(f"{ques_no}. What is the cube of {four} ?")
                    ans = input("Answer : ")
                    a = four*four*four
                    if int(ans) == a:
                        print("Correct!\n")
                        point += 1
                    else :
                        print(f"Wrong! ({a})\n")
            else :
                continue
            
            ques_no += 1
        except Exception as e:
            print("Wrong Input\n")
            ques_no += 1

    print("Your Score : " + str(point) +"\n")
    print(120*"=" + "\n")


#================================================================================================

if __name__ == "__main__":

    Quiz()

    while True:
            
        try:

            if cutie.prompt_yes_or_no("Want to Play Again ? "):
                Quiz()
            else:
                break

            print()

        except Exception :
            print("Wrong Input !")
            print()

