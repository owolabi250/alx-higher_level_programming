#!/usr/bin/python3

def max_integer(my_list=[]):
    bigger = 0
    if my_list == 0:
        return None
    else:
        for num in  my_list:
            if num > bigger:
                bigger = num
    return bigger
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))