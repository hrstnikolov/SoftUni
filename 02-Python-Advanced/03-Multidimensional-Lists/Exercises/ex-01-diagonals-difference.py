def read_sq_matrix(is_test=False):
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


def get_sum_primary_diagonal(matrix):
    size = len(matrix)
    return sum(matrix[i][i] for i in range(size))


def get_sum_secondary_diagonal(matrix):
    size = len(matrix)
    return sum(matrix[i][- i - 1] for i in range(size))


def get_diagonal_difference(matrix):
    sum_primary_diagonal = get_sum_primary_diagonal(matrix)
    sum_secondary_diagonal = get_sum_secondary_diagonal(matrix)
    difference = sum_primary_diagonal - sum_secondary_diagonal

    return abs(difference)


matrix = read_sq_matrix()
result = get_diagonal_difference(matrix)
print(result)