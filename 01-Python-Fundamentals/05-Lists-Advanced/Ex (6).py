electron_number = int(input())

distribution = []
curr_shell = 1
while True:
    shell_capacity = 2 * (curr_shell ** 2)

    if electron_number > shell_capacity:
        distribution.append(shell_capacity)
        electron_number -= shell_capacity
    else:
        distribution.append(electron_number)
        break

    curr_shell += 1

print(distribution)