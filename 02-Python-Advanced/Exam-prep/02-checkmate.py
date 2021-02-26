UNIT_SQUARES = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]


def read_board() -> [[], []]:
    board = []
    for _ in range(8):
        row = []
        for el in input().split(' '):
            row.append(el)
        board.append(row)

    return board


def find_king_pos(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                return i, j


def is_outside(r, c):
    return r < 0 or r > 7 or c < 0 or c > 7


def get_capturing_queens(board, king_pos):
    king_i, king_j = king_pos
    res = []
    exceptions = []
    for increment in range(1, 8):
        for (ii, jj) in UNIT_SQUARES:
            check_i = king_i + increment * ii
            check_j = king_j + increment * jj
            if not is_outside(check_i, check_j) \
                    and board[check_i][check_j] == 'Q' \
                    and (ii, jj) not in exceptions:
                res.append((check_i, check_j))
                exceptions.append((ii, jj))
    return res


def print_res(res):
    if res:
        for x, y in res:
            print(f'[{x}, {y}]')
    else:
        print('The king is safe!')


board = read_board()
king_pos = find_king_pos(board)
res = get_capturing_queens(board, king_pos)
print_res(res)
