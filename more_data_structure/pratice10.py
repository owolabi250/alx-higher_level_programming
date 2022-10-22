#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})


# def multiply_by_2(a_dictionary):
#     new_dic = {}
#     for i in a_dictionary:
#         new_dic[i] = a_dictionary[i] * 2
#     return new_dic


print_sorted_dictionary = \
    __import__('pratice7').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)