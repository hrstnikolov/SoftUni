def input_to_list_until_digit():
    lines = []
    while True:
        line = input()
        if line.isdigit():
            break
        lines.append(line)
    last_input = line

    return lines, last_input


def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def create_phone_book(entries):
    phone_book = {}
    for entry in entries:
        name, phone_num = entry.split('-')
        phone_book[name] = phone_num

    return phone_book

def print_contacts(phone_book, names):
    for name in names:
        if name in phone_book:
            print(f'{name} -> {phone_book[name]}')
        else:
            print(f'Contact {name} does not exist.')


entries, searches_count = input_to_list_until_digit()
phone_book = create_phone_book(entries)
searched_contacts = input_to_list(int(searches_count))
print_contacts(phone_book, searched_contacts)