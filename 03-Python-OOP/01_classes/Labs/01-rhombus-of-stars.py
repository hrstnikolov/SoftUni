def generate_line(n, i, ch='*'):
    offset = ' ' * (n - i - 1)
    edge = ch
    content = f' {ch}' * i
    return f'{offset}{edge}{content}'

def print_line(n, i, ch='*'):
    print(generate_line(n, i, ch))


def draw_rhombus(n):
    for i in range(n):
        print_line(n, i, '*')

    for i in range(n - 2, -1, -1):
        print_line(n, i, '*')


draw_rhombus(int(input()))


'''
  *
 * *
* * *
 * *
  *

'''
