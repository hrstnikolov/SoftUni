data = input().split(' ')
repeated_strings = [word * len(word) for word in data]
print(''.join(repeated_strings))