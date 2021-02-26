import re


def get_file_words(file_path):
    with open(file_path, 'r') as f:
        file_text = f.read()
        pattern = r"\w+'\w|\w+"
        words = re.findall(pattern, file_text)
    return words


def get_frequencies(words_list, input_list):
    result = {}
    for word in words_list:
        for input_word in input_words:
            if word.lower() == input_word.lower():
                if word not in result:
                    result[word] = 0
                result[word] += 1
    return result


words_file_path = 'words.txt'
input_file_path = 'input.txt'
output_file_path = 'output.txt'

words_list = get_file_words(words_file_path)
input_words = get_file_words(input_file_path)

result = get_frequencies(words_list, input_words)
result_sorted = sorted(result.items(), key=lambda x: x[1], reverse=True)

with open(output_file_path, 'w') as f:
    for word, occ in result:
        f.write(f'{word} - {occ}\n')
