#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
    last = number %10
else:
    last2 = number * -1
    last1 = last2 % 10
    last = last1 * -1   
if last > 5:
    print(f"last digit of {number} is {last} and is greater than 5")
elif last < 6 and last != 0:
    print(f"last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"last digit of {number} is {last} and is zero")
print()
