#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg=0
    size=0
    # avg,size = 0,0
    for tup in my_list:
        avg= avg + (tup[0] * tup[1])
        size = size + tup[1]
    return (avg/size)


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))