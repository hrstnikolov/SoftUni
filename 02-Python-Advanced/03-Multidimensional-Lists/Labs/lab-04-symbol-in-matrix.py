def read_square_matrix(is_test=False):
    if is_test:
        return [
            'ABC',
            'DEF',
            'X!@',
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [x for x in input()]
            matrix.append(row)
        return matrix


def find_character_in_matrix(matrix, char):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for row_index in range(rows_count):
        for column_index in range(columns_count):
            if matrix[row_index][column_index] == char:
                return row_index, column_index
    return None


def print_result(result, symbol):
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


def read_symbol(is_test=False):
    if is_test:
        return '!'
    return input()


table = read_square_matrix(is_test=True)
symbol = read_symbol(is_test=True)
result = find_character_in_matrix(table, symbol)
print_result(result, symbol)
