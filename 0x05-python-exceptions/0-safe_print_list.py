afe_print_list(my_list=[], x=0):
    if x == 0:
        print()
        return 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return i + 1
    except IndexError:
        print()
        return i
