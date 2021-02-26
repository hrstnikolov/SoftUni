# a = open('test_file.txt')
# b = open('../test_file_main_dir.txt', 'w')
# c = open('demos_inside_dir/test_file_inside_dir.txt', 'a')

with open('../test_file_main_dir.txt', 'r') as d:
    print(d.readline())
    # print(d.readline())
    # print(d.readlines())