#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # for key in sorted(a_dictionary):
    #     print("{}: {}".format(key, a_dictionary[key]))


    [print("{}: {}".format(items, a_dictionary[items])) for items in sorted(a_dictionary)]

if __name__ == '__main__':

    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)

