import cutie

#Lambda

# def square(n):
#     return n*n

square = lambda x: x*x # To make function

print(square(5))

print()
#=============================================================================================
#Join Method

a = ["Harry", "Rohan", "Yasharth"]

final = "::".join(a) # Add between the values
print(final)

print()
#=============================================================================================
#Map 

num = [1, 2, 3, 4, 5]

sqList = map(square, num)
print(list(sqList))

print()
#=============================================================================================
#Filter

def even(n):
    if n%2 == 0:
        return True
    return False

onlyEven = filter(even, num)
print(list(onlyEven))

print()
#=============================================================================================
# Reduce 

from functools import reduce

sum_f = lambda a,b : a + b

sum = reduce(sum_f, num)
print(sum)

#=============================================================================================
# Cutie Module

#if cutie.prompt_yes_or_no("Are you brave enough to continue?"):

#name = names[cutie.select(names, caption_indices=captions, selected_index=8)]