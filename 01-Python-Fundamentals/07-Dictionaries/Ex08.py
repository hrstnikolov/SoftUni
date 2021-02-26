id_nums = {}

while True:
    line = input()
    if line == 'End':
        break

    company_name, id_num = line.split(' -> ')
    if company_name in id_nums:
        if id_num not in id_nums[company_name]:
            id_nums[company_name].append(id_num)
    else:
        id_nums[company_name] = [id_num]

ordered_ids = dict(sorted(id_nums.items(), key=lambda x: x[0]))

for company_name, numbers in ordered_ids.items():
    print(f'{company_name}')
    for n in numbers:
        print(f'-- {n}')

