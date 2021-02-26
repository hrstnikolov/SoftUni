import re

data = input()
pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
# alternative_pattern = r'\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b'

full_names = re.findall(pattern, data)

print(' '.join(full_names))