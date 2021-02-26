def palindrome(word, index=0):
    if index >= len(word) // 2:
        return f'{word} is a palindrome'

    if word[index] == word[-1 - index]:
        return palindrome(word, index + 1)

    return f'{word} is not a palindrome'

#
# def palindrome(word, index=0):
#     if index > len(word) // 2:
#         return
#     palindrome(word, index + 1)
#     if not word[index] == word[-1 - index]:
#         return f'{word} is not a palindrome'
#     elif index == 0:
#         return f'{word} is a palindrome'
#

print(palindrome('a'))
print(palindrome('ab'))
print(palindrome('aba'))
print(palindrome('abccba'))
print(palindrome('peter'))