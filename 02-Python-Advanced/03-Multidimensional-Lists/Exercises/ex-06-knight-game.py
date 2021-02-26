KNIGHT_CHAR = 'K'
TEST_BOARDS = {
    1: [
        ['0', 'K', '0', 'K', '0'],
        ['K', '0', '0', '0', 'K'],
        ['0', '0', 'K', '0', '0'],
        ['K', '0', '0', '0', 'K'],
        ['0', 'K', '0', 'K', '0'],
    ],
    2: [
        ['K', 'K'],
        ['K', 'K'],
    ],
    3: [
        ['0', 'K', '0', 'K', 'K', 'K', '0', '0'],
        ['0', 'K', '0', '0', 'K', 'K', 'K', 'K'],
        ['0', '0', 'K', '0', '0', '0', '0', 'K'],
        ['K', 'K', 'K', 'K', 'K', 'K', '0', 'K'],
        ['K', '0', 'K', '0', '0', '0', '0', 'K'],
        ['K', 'K', '0', '0', '0', '0', '0', 'K'],
        ['0', '0', 'K', '0', 'K', '0', '0', '0'],
        ['0', '0', '0', 'K', '0', '0', 'K', 'K'],
    ]
}
deltas = (
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
    (2, 1),
    (-2, 1),
    (2, -1),
    (-2, -1),
)


def is_inside_board(coordinates, board):
    return all([True for c in coordinates
                if 0 <= c <= len(board) - 1])


def is_knight(coordinates, board):
    row, col = coordinates
    return board[row][col] == KNIGHT_CHAR


def sum_coordinates(coordinates_1, coordinates_2):
    row = coordinates_1[0] + coordinates_2[0]
    col = coordinates_1[1] + coordinates_2[1]
    return row, col


def read_board(is_test=False, test_board_id=1):
    if is_test:
        return TEST_BOARDS[test_board_id]
    else:
        pass


def is_battle(checked_coordinates, board):
    return is_inside_board(checked_coordinates, board) \
           and is_knight(checked_coordinates, board)


def check_for_battles(board, current_coordinates):
    board_size = len(board)
    battles = []
    for delta in deltas:
        checked_coordinates = sum_coordinates(current_coordinates, delta)
        if is_battle(checked_coordinates, board):
            battle = (checked_coordinates, current_coordinates)
            battles.append(battle)

    return battles


def find_battling_knights(board):
    all_battles = []
    board_size = len(board)

    for row_index in range(board_size):
        for col_index in range(board_size):
            current_coordinates = (row_index, col_index)
            if is_knight(current_coordinates, board):
                current_battles = check_for_battles(board, current_coordinates)
                for battle in current_battles:
                    if battle not in all_battles:
                        all_battles.append(battle)

    return all_battles


def count_battles_per_knight(all_battles):
    battles_count = {}
    for battle in all_battles:
        for coordinates in battle:
            if coordinates not in battles_count:
                battles_count[coordinates] = 0
            battles_count[coordinates] += 1

    return battles_count


# четем дъска
board = read_board(is_test=True)
# списъл с координати на застрашаващи коне
all_battles = find_battling_knights(board)
battles_per_knight = count_battles_per_knight(all_battles)
