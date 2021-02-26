def heaps_algorithm(index, lst):
    if index == len(lst) - 1:
        print(''.join(lst))
    for i in range(index, len(lst)):
        lst[index], lst[i] = lst[i], lst[index]
        heaps_algorithm(index + 1, lst)
        lst[index], lst[i] = lst[i], lst[index]


# def permutations_with_for_loop(index, lst):
#     permutations = []
#     for i in range(index, len(lst)):
#         for j in range(i, len(lst)):
#             if len(permutations) == len(lst):
#                 for p in permutations:
#                     p.extend(lst[j])
#             else:
#                 permutations.append([lst[j]])
#
#     for p in permutations:
#         print(p)


heaps_algorithm(0, list('abc'))
# permutations_with_for_loop(0, list('abc'))

