#!/usr/bin/python3
# def element_at(my_list, idx):

#     if idx < 0:
#         return None
#     elif idx >= len(my_list):
#         return None
#     else:
#         return my_list[idx]




def element_at(my_list, idx):

    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]


# def element_at(my_list, idx):

#     if idx < 0 and idx >= len(my_list):
#         return None
#     else:
#         return my_list[idx]






# def element_at(my_list, idx):
#     if idx < 0:
#         return None
#     if idx > len(my_list):
#         return None

#     for x in range(len(my_list)):
#         if x == idx:
#             return(my_list[idx])



def element_at(my_list, idx):
    if idx < 0 :
        return None
    if idx > len(my_list) :
        return None
    else:
        return my_list[idx]
my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
       
    