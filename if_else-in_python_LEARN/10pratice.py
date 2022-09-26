#!/usr/bin/python3

def print_last_digit(number):
    if number >=0:
        last = number % 10
        return last

    else:
        last = (number * -1) % 10
        return last
# print(print_last_digit(11))

print(print_last_digit(98))
print(print_last_digit(0))
r = print_last_digit(-1024)
print(r)