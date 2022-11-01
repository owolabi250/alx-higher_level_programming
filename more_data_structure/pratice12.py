#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # return[i*4 for i in my_list]
    # new = []
    # for i in my_list:
    #     mul = i * 4
    #     new.append(mul)
    # return new
    func = lambda x: x * number
    mp = map(func,my_list)
    ls = list(mp)
    return ls




my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list) 