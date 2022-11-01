#!/usr/bin/python3
def uniq_add(my_list=[]):



    # new_list = []
    # for i in my_list:
    #     if i not in new_list:
    #         new_list.append(i)
    # return sum(new_list)



    # new_list = []
    # for i in my_list:
    #     if i in new_list:
    #         continue
    #     new_list.append(i)
    # return sum(new_list)
 



    # new = set(my_list)
    # res = 0
    # for i in new:
    #     res += i
    # return res



    # new = set(my_list)
    # return sum(new)


    return sum(set(my_list))

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {}".format(result))

