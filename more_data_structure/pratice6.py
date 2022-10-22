#!/usr/bin/python3
# def number_keys(a_dictionary):
#     result = len(a_dictionary)
#     return result


# a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
# nb_keys = number_keys(a_dictionary)
# print("Number of keys: {:d}".format(nb_keys))




# def number_keys(a_dictionary):
#     return len(a_dictionary)
 


# a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
# nb_keys = number_keys(a_dictionary)
# print("Number of keys: {:d}".format(nb_keys))


# def number_keys(a_dictionary):
#     return len(a_dictionary.keys())
   


# a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
# nb_keys = number_keys(a_dictionary)
# print("Number of keys: {:d}".format(nb_keys))




def number_keys(a_dictionary):
    if a_dictionary is not None:
        return len(a_dictionary)
    return None



a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
