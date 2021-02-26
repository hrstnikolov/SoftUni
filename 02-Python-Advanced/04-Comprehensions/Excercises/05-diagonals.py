def input_to_list():
    matrix_size = int(input())
    lst = [[int(el) for el in input().split(', ')]
           for _ in range(matrix_size)]
    # lst = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    #
    # ]
    return lst


def is_on_first_diagonal(row_index, col_index):
    return row_index == col_index


def is_on_second_diagonal(row_index, col_index, matrix_size):
    return col_index == matrix_size - row_index - 1


def get_diagonals(matrix):
    matrix_size = len(matrix)
    first_diagonal = []
    second_diagonal = []
    for row in range(matrix_size):
        for col in range(matrix_size):
            value = matrix[row][col]
            if is_on_first_diagonal(row, col):
                first_diagonal.append(value)
            if is_on_second_diagonal(row, col, matrix_size):
                second_diagonal.append(value)

    return first_diagonal, second_diagonal


def print_result(first_diagonal, second_diagonal):
    values_1 = ", ".join(map(str, first_diagonal))
    sum_1 = sum(first_diagonal)
    values_2 = ", ".join(map(str, second_diagonal))
    sum_2 = sum(second_diagonal)

    print(f'First diagonal: {values_1}. Sum: {sum_1}')
    print(f'Second diagonal: {values_2}. Sum: {sum_2}')


matrix = input_to_list()
first_diagonal, second_diagonal = get_diagonals(matrix)
print_result(first_diagonal, second_diagonal)
