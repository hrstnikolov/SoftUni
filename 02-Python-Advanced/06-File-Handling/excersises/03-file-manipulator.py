import os

END_COMMAND = 'End'


def create_file(*args):
    file_name = args[0]
    open(file_name, 'w').close()


def add_file(*args):
    file_name = args[0]
    content = args[1]
    with open(file_name, 'a') as f:
        f.write(content + '\n')


def replace_file(*args):
    file_name = args[0]
    old_str = args[1]
    new_str = args[2]
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            updated_content = content.replace(old_str, new_str)
        with open(file_name, 'w') as f:
            f.write(updated_content)
    except FileNotFoundError:
        print_error_msg()


def delete_file(*args):
    file_name = args[0]
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print_error_msg()


def print_error_msg():
    print('An error occurred')


function_mapper = {
    'Create': create_file,
    'Add': add_file,
    'Replace': replace_file,
    'Delete': delete_file,
}

arguments_count_mapper = {
    'Create': 1,
    'Add': 2,
    'Replace': 3,
    'Delete': 1,
}


def execute_commands_until(end_command):
    while True:
        line = input()
        if line == end_command:
            break
        command_word, data = line.split('-', 1)
        selected_function = function_mapper[command_word]
        arguments_count = arguments_count_mapper[command_word]
        params = data.split('-', arguments_count - 1)
        selected_function(*params)


execute_commands_until(END_COMMAND)
