def decrypt_word(w):
    digits = ''.join(filter(str.isdigit, w))
    letters = list(filter(str.isalpha, w))

    # swap first and last letter
    letters[0], letters[-1] = letters[-1], letters[0]

    return chr(int(digits)) + ''.join(letters)


msg = input().split()

decrypted_msg = [decrypt_word(word) for word in msg]

print(' '.join(decrypted_msg))
