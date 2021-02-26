PLAYER_SYMBOL = 'P'
WALL_SYMBOL = 'X'
TARGET_COINS = 100
DELTAS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def read_matrix(is_test=False):
    if is_test:
        matrix = [
            ['1', 'X', '7', '9', '11'],
            ['X ', '14', '46', '62 ', '0'],
            ['15', '33', '21', '95', 'X'],
            ['P', '14', '3', '4', '18'],
            ['9', '20', '33', 'X', '0'],

        ]
    else:
        size = int(input())
        matrix = [input().split(' ') for _ in range(size)]
    return matrix


def find_player(matrix):
    size = len(matrix)
    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == PLAYER_SYMBOL:
                return row_index, col_index


def is_out(matrix, position):
    size = len(matrix)
    row, col = position

    return not (0 <= row < size and 0 <= col < size)


def has_hit_wall(matrix, position):
    row, col = position
    return matrix[row][col] == WALL_SYMBOL


def has_lost(matrix, position):
    return is_out(matrix, position) or has_hit_wall(matrix, position)


def play(matrix, player_position):
    has_won = True
    path = []
    total_coins = 0
    while True:
        command = input()
        delta = DELTAS.get(command)
        if delta:
            player_position = tuple(
                [player_position[i] + delta[i] for i in range(len(delta))]
            )
            if has_lost(matrix, player_position):
                has_won = False
                total_coins //= 2
                return has_won, path, total_coins
            else:
                path.append(player_position)
                row, col = player_position
                coins = matrix[row][col]
                total_coins += int(coins)
                if total_coins >= TARGET_COINS:
                    has_won = True
                    return has_won, path, total_coins


def print_result(has_won, path, total_coins):
    if has_won:
        print(f"You won! You've collected {total_coins} coins.")
    else:
        print(f"Game over! You've collected {total_coins} coins.")

    print('Your path:')
    for position in path:
        row, col = position
        print(f'[{row}, {col}]')


matrix = read_matrix()
initial_player_position = find_player(matrix)
result = play(matrix, initial_player_position)
print_result(*result)
