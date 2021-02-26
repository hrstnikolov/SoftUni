def take_odd(text):
    new_text = text[1::2]
    print(new_text)
    return new_text


def cut(text, ind, length):
    ind = int(ind)
    length = int(length)
    substring = text[ind: ind + length]
    text = text.replace(substring, '', 1)
    print(text)
    return text


def substitute(text, substring, replacement):
    if substring in text:
        new_text = text.replace(substring, replacement)
        print(new_text)
        return new_text
    print('Nothing to replace!')
    return text


mapper = {
    'TakeOdd': take_odd,
    'Cut': cut,
    'Substitute': substitute
}

password = input()
while True:
    data = input().split(' ')
    command = data[0]
    if command == 'Done':
        break

    parameters = data[1:]
    password = mapper[command](password, *parameters)

print(f"Your password is: {password}")








