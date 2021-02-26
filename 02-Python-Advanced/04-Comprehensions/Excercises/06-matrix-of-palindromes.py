STARTING_CHAR = 'a'


def get_palindromes_matrix(rows_cnt, cols_cnt, starting_char):
    palindromes_matrix = []
    for row_index in range(rows_count):
        row = []
        for col_index in range(cols_count):
            first_last_char = chr(ord(starting_char) + row_index)
            middle_char = chr(ord(first_last_char) + col_index)
            palindrome = first_last_char + middle_char + first_last_char
            row.append(palindrome)
        palindromes_matrix.append(row)

    return palindromes_matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


rows_count, cols_count = [int(x) for x in input().split(' ')]
# rows_count = 4
# cols_count = 6

palindromes_matrix = get_palindromes_matrix(rows_count, cols_count, STARTING_CHAR)
print_matrix(palindromes_matrix)
