from faker import Faker
from termcolor import colored
import sys
import string

fake = Faker()
while True:
    word = (fake.words(1))[0] 
    letters = list(word)
    num_letr = len(letters)
    if num_letr < 6:
        break
all_letr = string.ascii_letters

print("                                     Wordle Game\n")
print("You'll get 6 chances to guess the Word .\n")

print("                 " + '_ '*num_letr +"\n")

chance = 0
while chance<=5:
    try:
        matched_letters = []
        chance +=1

        user = input(f"{chance}.               ")
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear line
        sys.stdout.flush()          # Force it to update
        userl = list(user.upper())
        condition = True

        if len(userl) > num_letr:
            condition = False
          
        for m in range(0,num_letr):
            if userl[m] not in all_letr:
                condition = False
        
        if condition:
            for m in range(0,num_letr):
                if userl[m].lower() == letters[m]:
                    matched_letters.append(userl[m].lower())
                    userl[m] = (colored(userl[m], "green"))

                elif userl[m].lower() in letters and not userl[m].lower() in matched_letters:
                    userl[m] = (colored(userl[m], "yellow"))
                

            print("                 " + " ".join(userl))
                
            if user.lower() == word:
                print("\nCongratulations! You Won.")
                break
        else:
            print("                Wrong Input!")

        if chance == 6:
            print("\nYou Lost ! \nBetter Luck Next")
            print("Correct Word : " + word)

    except Exception:
        print("                Wrong Input!")
