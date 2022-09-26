#!/usr/bin/python3
# for i in range(122, 96, -1):
    # if i % 2 == 0:
    #     print(chr(i),end='')
    # else:
    #     print(chr(i-32),end='')
    # print(chr(i) if i % 2 == 0 else chr(i - 32),end='')

# i = 122
# while i > 96:
#     if i % 2 == 0:
#         print(chr(i),end='')
#     else:
#         print(chr(i-32),end='')
#     i -= 1


# def remove_char_at(str, n):
#     if n < 0:
#         return str
#     else:
#         return str[0:n] + str[n+1:]
# print(remove_char_at("Best School", 3))
# print(remove_char_at("Chicago", 2))
# print(remove_char_at("C is fun!", 0))
# print(remove_char_at("School", 10))
# print(remove_char_at("Python", -2))




# def remove_char_at(str, n):
#     # strLen = len(str)
#     newStr = ''
#     i = 0
#     while i < len(str): #"Best School"
#         if i == n:
#             continue
#         newStr += str[i]
#         i += 1
#     return newStr  

 
# print(remove_char_at("Best School", 3))
# print(remove_char_at("Chicago", 2))
# print(remove_char_at("C is fun!", 0))
# print(remove_char_at("School", 10))
# print(remove_char_at("Python", -2))   



def my_function(counter = 89):
    return counter + 1
print(my_function())