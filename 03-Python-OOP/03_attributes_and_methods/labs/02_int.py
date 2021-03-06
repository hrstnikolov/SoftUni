import math

import roman_numbers


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_roman(cls, number):
        return cls(roman_numbers.number(number))

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"

        return cls(math.floor(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return int(value)

    def add(self, integer):
        if not isinstance(integer, int):
            return "number should be an Integer instance"

        return self.value + integer


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
