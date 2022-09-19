#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print("the number is {} and it is positive".format(number))
elif number == 0:
    print("the number is {} and it is zero".format(number))
else:
    print("the number is {} and it is negative".format(number))
print()
        
