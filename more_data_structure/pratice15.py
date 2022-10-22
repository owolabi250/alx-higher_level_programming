#!/usr/bin/python3
def square_matrix_map(matrix=[]):

    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))



    # new = []
    # for row in matrix:
    #     a = []
    #     for num in row:
    #         sq = num * num
    #         a.append(sq)
    #     new.append(a)
    # return new



    # return[[num ** 2 for num in row] for row in matrix]
    


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)