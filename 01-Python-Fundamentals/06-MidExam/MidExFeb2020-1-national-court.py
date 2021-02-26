receptionists_efficiencies = []

for i in range(3):
    receptionists_efficiencies.append(int(input()))

customer_count = int(input())

total_eff = sum(receptionists_efficiencies)

total_time = 0
while customer_count > 0:
    customer_count -= total_eff
    total_time += 1

    if total_time % 4 == 0:
        total_time += 1

print(f'Time needed: {total_time}h.')