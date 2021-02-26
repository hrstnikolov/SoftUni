# from collections import deque
#
#
# def read_input():
#     # firework_effects = deque([5, 6, 4, 16, 11, 5, 30, 2, 3, 27])
#     # explosive_power = [1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22]
#     firework_effects = deque([int(x) for x in input().split(', ')])
#     explosive_power = [int(x) for x in input().split(', ')]
#
#     return firework_effects, explosive_power
#
#
# def has_enough_fireworks(prepared_fireworks):
#     return all([v >= 3 for v in prepared_fireworks.values()])
#
#
# def has_lost(firework_effects, explosive_power):
#     return any([
#         not firework_effects,
#         not explosive_power,
#     ])
#
#
# def prepare_fireworks(firework_effects, explosive_power):
#     has_won = True
#     prepared_fireworks = {
#         'Palm': 0,
#         'Willow': 0,
#         'Crossette': 0,
#     }
#
#     while True:
#         if has_enough_fireworks(prepared_fireworks):
#             has_won = True
#             break
#         if has_lost(firework_effects, explosive_power):
#             has_won = False
#             break
#
#         effect = firework_effects.popleft()
#         if effect <= 0:
#             continue
#         power = explosive_power.pop()
#         if power <= 0:
#             firework_effects.appendleft(effect)
#             continue
#         the_sum = effect + power
#         if the_sum % 3 == 0 and the_sum % 5 != 0:
#             prepared_fireworks['Palm'] += 1
#         elif the_sum % 3 != 0 and the_sum % 5 == 0:
#             prepared_fireworks['Willow'] += 1
#         elif the_sum % 3 == 0 and the_sum % 5 == 0:
#             prepared_fireworks['Crossette'] += 1
#         else:
#             effect -= 1
#             firework_effects.append(effect)
#             explosive_power.append(power)
#
#     return has_won, firework_effects, explosive_power, prepared_fireworks
#
#
# def print_result(has_won, firework_effects, explosive_power, prepared_fireworks):
#     if has_won:
#         print("Congrats! You made the perfect firework show!")
#     else:
#         print("Sorry. You can’t make the perfect firework show.")
#
#     if firework_effects:
#         print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
#     if explosive_power:
#         print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
#     for firework, value in prepared_fireworks.items():
#         print(f"{firework} Fireworks: {value}")
#
#
# firework_effects, explosive_power = read_input()
# result = prepare_fireworks(firework_effects, explosive_power)
# print_result(*result)

m = [1]
m[2]