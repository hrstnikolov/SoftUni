rows = 4
cols = 4

matrix = []
i = 1
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(i)
        i += 1
    matrix.append(row)

# print('\n'.join([str(row) for row in matrix]))

def move(matrix, current_row, current_col, steps):
    rows = len(matrix)
    cols = len(matrix[0])
    row = (current_row + steps) // rows
    col = (current_col + steps) // cols
    return row, col

x1, y1 = move(matrix, 0, 1, 9)
print(matrix[x1][y1])