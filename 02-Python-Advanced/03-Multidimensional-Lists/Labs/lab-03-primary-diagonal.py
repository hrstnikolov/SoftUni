def read_square_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [int(x) for x in input().split()]
            matrix.append(row)
        return matrix


def sum_primary_diagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    # sum = sum([matrix[i][i] for i in range(len(matrix))])
    return sum


def sum_secondary_diagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][-i - 1]

    return sum


def sum_under_primary_diagonal(matrix):
    sum = 0
    size = len(matrix)
    for row_index in range(size):
        for column_index in range(size):
            if column_index < row_index:
                sum += matrix[row_index][column_index]

    return sum


matrix = read_square_matrix()
print(sum_primary_diagonal(matrix))
# print(sum_secondary_diagonal(matrix))
# print(sum_under_main_diagonal(matrix))
