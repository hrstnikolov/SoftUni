PUSH_COMMAND = '1'
DELETE_COMMAND = '2'
PRINT_MAX = '3'
PRINT_MIN = '4'

mapper = {
    PUSH_COMMAND: lambda s, el: s.append(el),
    DELETE_COMMAND: lambda s: s.pop(),
    PRINT_MAX: lambda s: print(max(s)),
    PRINT_MIN: lambda s: print(min(s))
}

s = []

n = int(input())
for _ in range(n):
    query, *command_params = input().split(' ')
    mapper[query](s, *command_params)

print(', '.join(reversed(s)))
