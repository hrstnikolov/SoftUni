from collections import deque

qty_food = int(input())

orders_queue = deque()
for order in input().split(' '):
    orders_queue.append(int(order))

biggest_order = max(orders_queue)
print(biggest_order)

while orders_queue:
    current_order = orders_queue[0]
    if current_order <= qty_food:
        orders_queue.popleft()
        qty_food -= current_order
    else:
        break
else:
    print('Orders complete')

if orders_queue:
    remaining_orders = ' '.join(map(str, orders_queue))
    print(f"Orders left: {remaining_orders}")
