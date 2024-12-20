import string
import random
import cutie

try:
    print(                                           "Password Generator")
    print()
    length = int(input("Enter Password Length : "))
    ldiff = ["Low", "Medium", "Strong"]
    print("Enter the Password Difficulty : ")
    diff = ldiff[cutie.select(ldiff, selected_index=0)]

    print()

    if length > 100:
        raise Exception("It should be under 100 !")
    
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    punc = list(string.punctuation)

    c_list = []
    if diff.lower() == "low" or diff.lower() == "l":
        c_list.extend(letters)
    elif diff.lower() == "medium" or diff.lower() == "m":
        c_list.extend(numbers)
        c_list.extend(letters)
    else:
        c_list.extend(letters)
        c_list.extend(numbers)
        c_list.extend(punc)
    

    m = 1
    while (m <= length):
        char = random.choice(c_list)
        if m == 1:
            password = char
        else:
            password = password + char
        m += 1
    
    print("Your Password :")
    print(password)

except ValueError:
    print("It should be a Number !")
