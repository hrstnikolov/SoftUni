def replace_case(user, case_type):
    if case_type == 'lower':
        user = user.lower()
    elif case_type == 'upper':
        user = user.upper()
    print(user)
    return user


def reverse(user, start_index, end_index):
    if start_index >= 0 and end_index <= len(user):
        substring = user[end_index:start_index - 1:-1]
        print(substring)


def cut(user, substring):
    if substring in user:
        user = user.replace(substring, '')
        print(user)
        return user
    print(f"The word {user} doesn't contain {substring}.")
    return user


def replace(user, char):
    user = user.replace(char, '*')
    print(user)
    return user


def check(user, char):
    if char in user:
        print('Valid')
    else:
        print(f'Your username must contain {char}.')


user = input()
while True:
    data = input()
    if data == "Sign up":
        break
    data = data.split(' ')
    command = data[0]

    if command == 'Case':
        case_type = data[1]
        user = replace_case(user, case_type)
    elif command == 'Reverse':
        start = int(data[1])
        end = int(data[2])
        reverse(user, start, end)
    elif command == 'Cut':
        substring = data[1]
        user = cut(user, substring)
    elif command == 'Replace':
        char = data[1]
        user = replace(user, char)
    elif command == 'Check':
        char = data[1]
        check(user, char)
