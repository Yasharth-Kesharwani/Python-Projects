import string
import random

try:
    print()
    length = int(input("Enter Password Length : "))
    print()

    if length > 100:
        raise Exception("It should be under 100 !")
    
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    punc = list(string.punctuation)

    c_list = []
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
