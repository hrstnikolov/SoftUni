def valentine_jump(neighborhood, jump_len, curr_ind):

    if (curr_ind + jump_len) < len(neighborhood):
        curr_ind = curr_ind + jump_len
    else:
        curr_ind = 0

    if neighborhood[curr_ind] == 0:
        print(f"Place {curr_ind} already had Valentine's day.")
    else:
        neighborhood[curr_ind] -= 2
        if neighborhood[curr_ind] <= 0:
            print(f"Place {curr_ind} has Valentine's day.")

    return neighborhood, curr_ind


neighborhood = [int(el) for el in input().split('@')]

command = input()
house_index = 0

while not command == 'Love!':
    action, jump_len = command.split()
    jump_len = int(jump_len)

    if action == 'Jump':
        neighborhood, house_index = valentine_jump(neighborhood, jump_len, house_index)

    command = input()

print(f"Cupid's last position was {house_index}.")
if all(value == 0 for value in neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - neighborhood.count(0)} places.")

