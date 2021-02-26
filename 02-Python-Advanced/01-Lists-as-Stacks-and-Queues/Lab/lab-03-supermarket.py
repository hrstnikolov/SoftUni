from collections import deque


q = deque()

text = input()
while not text == 'End':
    if text == 'Paid':
        while q:
            print(q.popleft())
    else:
        q.append(text)
    text = input()

print(f'{len(q)} people remaining.')