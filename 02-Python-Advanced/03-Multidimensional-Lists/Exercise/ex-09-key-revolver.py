from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullet_sizes_stack = [int(i) for i in input().split(' ')]
lock_sizes_queue = deque([int(i) for i in input().split(' ')])
value_of_intelligence = int(input())

bullets_in_barrel = gun_barrel_size
shot_bullet_cost = 0
while lock_sizes_queue:

    # depleting bullets
    if not bullet_sizes_stack:
        locks_left = len(lock_sizes_queue)
        print(f"Couldn't get through. Locks left: {locks_left}")
        break

    # shooting
    bullet = bullet_sizes_stack.pop()
    lock = lock_sizes_queue[0]
    if bullet <= lock:
        print("Bang!")
        lock_sizes_queue.popleft()
    else:
        print("Ping!")

    # reloading
    bullets_in_barrel -= 1
    shot_bullet_cost += price_per_bullet
    if bullets_in_barrel == 0 and bullet_sizes_stack:
        bullets_in_barrel = gun_barrel_size
        print("Reloading!")
else:
    # if all lock are unlocked
    bullets_left = len(bullet_sizes_stack)
    money_earned = value_of_intelligence - shot_bullet_cost
    print(f"{bullets_left} bullets left. Earned ${money_earned}")
