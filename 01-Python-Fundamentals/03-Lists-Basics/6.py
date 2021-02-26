lst = list(map(int, input().split(' ')))
n = int(input())

for num in sorted(lst)[:n]:
    lst.remove(num)

print(lst)
