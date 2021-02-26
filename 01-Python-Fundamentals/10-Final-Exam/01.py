msg = input()

while True:
    line = input()
    if line == 'Decode':
        break
    data = line.split('|')
    command = data[0]

    if command == 'Move':
        n = int(data[1])
        msg = msg[n:] + msg[:n]

    elif command == 'Insert':
        index = int(data[1])
        value = data[2]
        msg = msg[:index] + value + msg[index:]

    elif command == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        msg = msg.replace(substring, replacement)

print(f'The decrypted message is: {msg}')
