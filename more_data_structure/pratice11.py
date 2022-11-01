#!/usr/bin/python3
# def best_score(a_dictionary):
    # new = 0
    # if a_dictionary:
    #     for i in a_dictionary:
    #         if a_dictionary[i] > new:
    #             new = a_dictionary[i]
    #             n = i
    #     return n
 

# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))

# num1, num2 = input("Enter 2 values to divide: ").split()
# print()
# try:
#     quotient = int(num1) / int(num2)
#     print(" {} / {} = {}".format (num1, num2, quotient))
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("You can't didvide a string")
# except SyntaxError:
#     print("incorrect syntax")
# except ModuleNotFoundError:
#     print("incorrect module")
# else:
#     print("You didn't raise an exception")
# finally:
#     print("i execute no matter what")


try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")
