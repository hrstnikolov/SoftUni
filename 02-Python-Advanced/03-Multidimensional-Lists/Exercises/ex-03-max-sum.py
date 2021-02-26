def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4],
        ]
    else:
        row_count, col_count = [int(x) for x in input().split(' ')]
        matrix = []
        for row_index in range(row_count):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)
        return matrix


def get_sum_of_square(matrix, starting_row, starting_col, size):
    row_range = range(starting_row, starting_row + size)
    col_range = range(starting_col, starting_col + size)
    the_sum = 0
    for r in row_range:
        for c in col_range:
            the_sum += matrix[r][c]
    return the_sum


def get_max_sum(matrix, square_size):
    row_range = range(0, len(matrix) - square_size + 1)
    col_range = range(0, len(matrix[0]) - square_size + 1)
    max_sum = 0
    max_sum_starting_row = 0
    max_sum_starting_col = 0
    for r in row_range:
        for c in col_range:
            curr_sum = get_sum_of_square(matrix, r, c, square_size)
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_sum_starting_row = r
                max_sum_starting_col = c
    return matrix, max_sum, max_sum_starting_row, max_sum_starting_col, square_size


def print_result(matrix, max_sum, starting_row, starting_col, size):
    print(f'Sum = {max_sum}')
    row_range = range(starting_row, starting_row + size)
    col_range = range(starting_col, starting_col + size)
    for r in row_range:
        for c in col_range:
            print(matrix[r][c], end=' ')
        print()


matrix = read_matrix()
result = get_max_sum(matrix, 3)
print_result(*result)
