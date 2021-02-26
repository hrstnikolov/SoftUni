IN_DIRECTION = 'IN'
OUT_DIRECTION = 'OUT'


def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


lines_count = int(input())
lines = input_to_list(lines_count)

# car_data = [
# 'IN, CA2844AA',
# 'IN, CA1234TA',
# 'OUT, CA2844AA',
# 'IN, CA9999TT',
# 'IN, CA2866HI',
# 'OUT, CA1234TA',
# 'IN, CA2844AA',
# 'OUT, CA2866HI',
# 'IN, CA9876HH',
# 'IN, CA2822UU',
# ]

parking_lot = set()
for line in lines:
    direction, plate_number = line.split(', ')
    if direction == IN_DIRECTION:
        parking_lot.add(plate_number)
    elif direction == OUT_DIRECTION:
        parking_lot.remove(plate_number)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print('Parking Lot is Empty')