#!/usr/bin/python3
# def search_replace(my_list, search, replace):
#     new = []
#     for num in my_list:
#         if num == search:
#             search = replace
#             new.append(search)
#         else:
#             new.append(num)
#     return new
    

# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)



# def search_replace(my_list, search, replace):
#     return[replace if num == search else num for num in my_list]
# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)



def search_replace(my_list, search, replace):
    return[num if num != search else replace for num in my_list]
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

