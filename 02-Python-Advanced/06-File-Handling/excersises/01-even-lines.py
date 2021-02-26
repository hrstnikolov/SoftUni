import re

PUNCTUATION_MARKS = r'[\-\?\!\,\.]'
REPLACEMENT_CHAR = '@'


def format_line(line):
    return re.sub(PUNCTUATION_MARKS, REPLACEMENT_CHAR, line)


def get_even_lines(file_path):
    even_lines = []
    with open(file_path, 'r') as f:
        for line_num, line in enumerate(f):
            if line_num % 2 == 0:
                even_lines.append(line)

    return even_lines


def get_result(file_path):
    even_lines = get_even_lines(file_path)
    result = []
    for line in even_lines:
        formatted_line = format_line(line)
        words = formatted_line.split()
        sorted_words = reversed(words)
        new_line = ' '.join(sorted_words)
        result.append(new_line)

    return result


def print_result(result):
    for line in result:
        print(line)


input_path = 'text.txt'
result = get_result(input_path)
print_result(result)
