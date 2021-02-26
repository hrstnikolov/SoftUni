import os
import re


def get_files_in_categories(dir_path):
    dir_content = os.listdir(dir_path)
    regexp_file_extension = re.compile(r'\.[a-zA-Z]{1,5}$')
    files = {}
    for item in dir_content:
        file_extension = regexp_file_extension.search(item).group(0)
        if file_extension not in files:
            files[file_extension] = []
        files[file_extension].append(item)

    return files


def get_report(dir_path):
    files_dict = get_files_in_categories(dir_path)
    sorted_files = sorted(files_dict.items(), key=lambda x: (x[0], x[1]))
    report = ''
    for (extension, file_names) in sorted_files:
        report += extension + '\n'
        for file_name in file_names:
            report += f'- - - {file_name}\n'

    return report


def save_report(report):
    path_to_desktop = os.path.expanduser("~/Desktop")
    os.chdir(path_to_desktop)
    with open('report.txt', 'w') as f:
        f.write(report)


current_word_dir = os.getcwd()
report = get_report(current_word_dir)
save_report(report)
