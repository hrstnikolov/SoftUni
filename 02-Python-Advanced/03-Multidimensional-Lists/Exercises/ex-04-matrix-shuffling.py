def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
        ]
    else:
        row_count, col_count = [int(x) for x in input().split(' ')]
        matrix = []
        for row_index in range(row_count):
            row = [el for el in input().split(' ')]
            matrix.append(row)
        return matrix


def swap_elements(matrix, coord_1, coord_2):
    print('swap')


matrix = read_matrix(is_test=True)
while True:
    data = input()
    if data == 'End':
        break
    try:
    split_data = data.split(' ')
    command = split_data[0]
    row1, col1, row2, col2 = split_data[]
    is_valid = all([
        command == 'swap',

    ])
    if command == 'swap':
        matrix = swap_elements(matrix, coord_1, coord_2)

