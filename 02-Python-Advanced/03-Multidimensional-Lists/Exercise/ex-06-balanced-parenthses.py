PAIRED_BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}'
}

text = input()
brackets_stack = []
is_balanced = True

for bracket in text:
    # ако скобата е отваряща
    if bracket in PAIRED_BRACKETS:
        brackets_stack.append(bracket)

    # ако скобата е затваряща
    elif bracket in PAIRED_BRACKETS.values():
        if brackets_stack:
            last_opening_bracket = brackets_stack.pop()
            expected_closing_bracket = PAIRED_BRACKETS[last_opening_bracket]
            if not bracket == expected_closing_bracket:
                is_balanced = False
                break
            else:
                is_balanced = False
                break

if is_balanced:
    print('YES')
else:
    print('NO')
