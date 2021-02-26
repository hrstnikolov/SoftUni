END_COMMAND = 'END'


def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def input_to_list_until_command(command):
    lines = []
    while True:
        line = input()
        if line == command:
            break
        lines.append(line)

    return lines


def is_vip(guest):
    return guest[0].is_digit()


def print_output(guests):
    for guest in guests:
        if is_vip(guest):


#
# number_of_guests = int(input())
# with_reservation = input_to_list(number_of_guests)
# attended = input_to_list_until_command(END_COMMAND)

with_reservation = [
    '7IK9Yo0h',
    '9NoBUajQ',
    'Ce8vwPmE',
    'SVQXQCbc',
    'tSzE5t0p',
]

attended = [
    '9NoBUajQ',
    'Ce8vwPmE',
    'SVQXQCbc',
]

with_reservation = set(with_reservation)
attended = set(attended)
delta = with_reservation - attended
print_output(delta)
