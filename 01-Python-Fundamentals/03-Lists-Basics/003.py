lst = list(map(int, input().split(' ')))
k = int(input())

new_lst = []
ind = 0

while lst:
    ind = (ind + 2) % len(lst)
    new_lst.append(lst.pop(ind))

print(new_lst)