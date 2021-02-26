def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'B', 'D'],
            ['E', 'B', 'B', 'B'],
            ['I', 'J', 'B', 'B'],
        ]
    else:
        row_count, col_count = [int(x) for x in input().split(' ')]
        matrix = []
        for row_index in range(row_count):
            row = [x for x in input().split(' ')]
            matrix.append(row)
        return matrix


def is_square_of_same_chars(matrix, starting_row, starting_col, size):
    row_range = range(starting_row, starting_row + size)
    col_range = range(starting_col, starting_col + size)
    value = matrix[starting_row][starting_col]
    for r in row_range:
        for c in col_range:
            if not matrix[r][c] == value:
                return False
    return True


def count_equal_squares(matrix, square_size):
    row_range = range(0, len(matrix) - square_size + 1)
    col_range = range(0, len(matrix[0]) - square_size + 1)
    sqaure_count = 0
    for r in row_range:
        for c in col_range:
            if is_square_of_same_chars(matrix, r, c, square_size):
                sqaure_count += 1

    return sqaure_count


matrix = read_matrix()
result = count_equal_squares(matrix, 2)
print(result)
