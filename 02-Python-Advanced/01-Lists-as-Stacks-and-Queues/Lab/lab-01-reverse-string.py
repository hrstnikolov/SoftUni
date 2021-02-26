# line = input()
# stack = []
# for ch in line:
#     stack.append(ch)
# for _ in range(len(line)):
#     print(stack.pop(), end='')


text = list(input())
stack = []

for _ in range(len(text)):
    stack.append(text.pop())

print("".join(stack))