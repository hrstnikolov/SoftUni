def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        matrix = []
        (rows_count, columns_count) = [int(x) for x in input().split(', ')]
        for _ in rows_count:
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)
        return matrix

def sum_matrix_columns(matrix):
    for column_index in range(len(matrix[0])):
        sum_column = 0
        for row_index in range(len(matrix)):
            sum_column += matrix[row_index][column_index]
        print(sum_column)


matrix = read_matrix(is_test=True)
sum_matrix_columns(matrix)
