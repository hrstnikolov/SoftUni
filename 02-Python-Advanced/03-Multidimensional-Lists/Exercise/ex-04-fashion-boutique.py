clothes_stack = [int(el) for el in input().split(' ')]

rack_capacity = int(input())

curr_rack_capacity = 0
rack_counter = 1
while clothes_stack:
    curr_value = clothes_stack.pop()
    if curr_rack_capacity + curr_value <= rack_capacity:
        curr_rack_capacity += curr_value
    else:
        rack_counter += 1
        curr_rack_capacity = 0
        curr_rack_capacity += curr_value

print(rack_counter)
