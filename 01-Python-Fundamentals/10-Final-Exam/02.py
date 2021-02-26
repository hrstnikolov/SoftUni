import re


class FoodItems:
    def __init__(self, item_name, expiration_date, calories):
        self.item_name = item_name
        self.expiration_date = expiration_date
        self.calories = calories

    def __repr__(self):
        return f'Item: {self.item_name}, ' \
               f'Best before: {self.expiration_date}, ' \
               f'Nutrition: {self.calories}'


food_items = []
data = input()
pattern = r'([#\|])' \
          r'(?P<item>[a-zA-Z\s]+)\1' \
          r'(?P<date>\d{2}/\d{2}/\d{2})\1' \
          r'(?P<calories>([0-9]|[1-9][0-9]{0,3}|10000)\1'
matches = re.finditer(pattern, data)

sum_calories = 0
for match in matches:
    res = match.groupdict()
    item = res['item']
    date = res['date']
    calories = int(res['calories'])

    food_items.append(FoodItems(item, date, calories))
    sum_calories += calories

days = sum_calories // 2000
print(f'You have food to last you for: {days} days!')
for item in food_items:
    print(item)
