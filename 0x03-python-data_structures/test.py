#!/usr/bin/python3
# def print_list_integer(my_list=[]):
    # my_list = [5, 6, 7, 8, 9,]
#     for content in my_list:
#         print(content,end=' ')
# print_list_integer([11, 12, 13])




        
    # for i in range(len(my_list)):
    #     # print(i,end=' ')
    #     print("{:d}".format(my_list[i]))


# def element_at(my_list, idx):
#   
#     else:
#         return my_list[idx]
    
# list1 = [1, 2, 3, 4, 5]
# index = 5
# print("Element at index {:d} is {}".format(index, element_at(list1, index)))  

# def replace_in_list(my_list, idx, element):
#     if idx < 0:
#         return my_list
#     elif idx >= len(my_list):
#         return my_list
#     my_list[idx] = element
#     return my_list

# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_element = 9
# new_list = replace_in_list(my_list, idx, new_element)

# print(new_list)
# print(my_list)
    
# def print_reversed_list_integer(my_list=[]):
#     t = reversed(my_list)
#     for i in t:
#         print(i)
    
# def print_reversed_list_integer(my_list=[]):
#     for i in reversed(range(len(my_list))):
#         print(my_list[i])



# def new_in_list(my_list, idx, element):
#     if idx < 0 and idx >= len(my_list):
#         return my_list
#     else:
#         new_list = my_list[:]
#         new_list[idx] = element
#         return new_list


# def no_c(my_string):
#     a = ''
#     for i in my_string:
#         if i == "c" or i == "C":
#             continue
#         a = a + i
#     return a



# def no_c(my_string):
#     for i in my_string:
#         if i == "c" or i == "C":
#             continue
#         print(i,end='')
#     print()
# no_c("Best School")
# no_c("Chicago")
# no_c("C is fun!")



# def print_matrix_integer(matrix=[[]]):
#     for l in matrix:
#         for i in range(len(l)):
#             print(l[i],end ="")
#             if i < len(l) - 1:
#                 print(" ",end ="")
#             else:
#                 print()





# def add_tuple(tuple_a=(), tuple_b=()):
#     if len(tuple_a) < 2:
#         tuple_a = tuple_a + (0,0)
#     if len(tuple_b) < 2:
#         tuple_b = tuple_b + (0,0) 

    # new_list = []
    # for a, b in zip(tuple_a, tuple_b):
    #     new_list.append(a + b)
    # return tuple(new_list) 
#     new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
#     return new_tuple

# tuple_a = (1, 89)
# tuple_b = (88, 11)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)

# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))



# def multiple_returns(sentence):
   
#     if len(sentence) == 0:
#         return 0, None
#     else:
#         length = len(sentence)
#         first = sentence[0]
#         return length, first
        

# sentence ="At school, I learnt C!"
# length, first = multiple_returns(sentence)
# print("Length: {:d} - First character: {}".format(length, first))


# def max_integer(my_list=[]):
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     f = 0
    # g = 0
    # if len(my_list) == 0:
    # if not my_list:
    #     return None
    # else:
        # new_list = sorted(my_list)
        # revd = list(reversed(my_list))
        #     for num in 
        # # for i in range(len(my_list)):
            # if a < my_list[i]:
                # g = f
                # f =e
                # e =d
                # d = c
                # c = b
                # b = a
                # a = my_list[i]
        # return [a, b, c, d, e, f]
        # return new_list#[- 1], new_list[-2]
#         return revd
# my_list = [1,2, 13, 34, 5, -13, 3,60]
# max_value = max_integer
# print("Max: {}".format(max_value(my_list)))

# # print("Max: {}".format(max_integer(my_list)))


# print("Max: {}".format(max(my_list)))


# def divisible_by_2(my_list=[]):
    # res_list = []
    # for num in my_list:
        # if num % 2 == 0:
        # res_list.append(num % 2 == 0)
        # else:
            # res_list.append(False)
    # return [num % 2 == 0 for num in my_list]
    # print(res_list)
    # return res_list



# my_list = [0, 1, 2, 3, 4, 5, 6]
# list_result = divisible_by_2(my_list)
# print(list_result)

# i = 0
# while i < len(list_result):
#     print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
#     i += 1


# import random
# k = [i*2 for i in range(10)]
# print(k,end="")

# for i in range(10):
#     if i % 2 != 0:
#         continue
#     print(i,end="")


# def delete_at(my_list=[], idx=0):
#     if idx < 0 or idx > len(my_list):
#         return my_list
#     else:
#         my_list.remove(idx)
#     return my_list
       
# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_list = delete_at(my_list, idx)
# print(new_list)
# print(my_list)



# def delete_at(my_list=[], idx=0):
#     if idx < 0 or idx > len(my_list):
#         return my_list
#     else:      
#         my_list.remove(idx)
#     return my_list
       
# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_list = delete_at(my_list, idx)
# print(new_list)
# print(my_list)


    



# a = 89
# b = 10
# # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
# a,b = b,a
# print("a={:d} - b={:d}".format(a, b))



# def square_matrix_simple(matrix=[]):
#     new = []
#     for row in matrix:
#         sub = []
#         # new.append([num * num for num in row])
#         for num in row:
#             sq = num * num 
#             sub.append(sq)
#         new.append(sub)
#     return new

  

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
# print(matrix)


def search_replace(my_list, search, replace):
    # new = []
    # for num in my_list:
    #     if num == search:
    #         new.append(replace)
    #     else:
    #         new.append(num)
    # return new


#     new = my_list[:]
#     searchcount = my_list.count(search)
#     for i in range(searchcount):
#         idx = 0
#         idx = my_list.index(search,idx)
#         new[idx] = replace
#     return new


# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)







