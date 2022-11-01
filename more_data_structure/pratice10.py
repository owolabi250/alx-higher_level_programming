#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # return {key: 2 * a_dictionary[key] for key in a_dictionary}



    new_dic = {}
    for key in a_dictionary:
        new_dic[key] = a_dictionary[key] * 2
    return new_dic


print_sorted_dictionary = \
    __import__('pratice7').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)