matrix = [
    [7, 1, 3, 3, 2, 1],
    [1, 3, 9, 8, 5, 6],
    [4, 6, 7, 9, 1, 0],
]

matrix_sum = 0

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        matrix_sum += matrix[r][c]

print(matrix_sum)