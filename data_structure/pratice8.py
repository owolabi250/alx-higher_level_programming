#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,0) 

    # new_list = []
    # for a, b in zip(tuple_a, tuple_b):
    #     new_list.append(a + b)
    # return tuple(new_list) 
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
