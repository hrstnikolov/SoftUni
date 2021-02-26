OPENING_BRACKETS = {
    '(': 1,
    '[': 2,
    '{': 3
}
CLOSING_BRACKETS = {
    ')': 1,
    ']': 2,
    '}': 3
}


def is_balanced(seq):
    brackets_stack = []
    for ch in seq:
        if ch in OPENING_BRACKETS:
            brackets_stack.append(OPENING_BRACKETS[ch])
        elif ch in CLOSING_BRACKETS:
            last = brackets_stack.pop()
            curr = CLOSING_BRACKETS[ch]
            if not last == curr:
                print('NO')
                return
    print('YES')


is_balanced(input())