factor = int(input())
count = int(input())

# # solution 1
# elements = []
# for index in range(1, count + 1):
#     elements.append(index * factor)

# solution 2
elements = [i * factor for i in range(1, count + 1)]

print(elements)