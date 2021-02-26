from re import *


data = input()
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
finditer()


'''
matches = search(pattern, data)  # returns ONLY 1 match - the first one
print(matches.re)
print(matches.group())
print(matches.groups())
print(matches.groupdict())
print(matches.lastgroup)
print(matches.start())  # returns index of first
'''