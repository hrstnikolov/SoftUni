import re


data = input()

# шаблон
pattern = r'\d+'

# чрез фунцкия findall
matches = re.findall(pattern, data)
# генериране на листа чрез метод findall на компилиран ре обект
# matches = re.compile(pattern).findall(data)

print(" ".join(matches))