PUSH_COMMAND = 1
DELETE_COMMAND = 2
PRINT_MAX = 3
PRINT_MIN = 4

query_mapper = {
    PUSH_COMMAND: lambda s, el: s.append(el),
    DELETE_COMMAND: lambda s, el: s.pop(el),
    PRINT_MAX: lambda s: print(max(s)),
    PRINT_MIN: lambda s: print(min(s))
}

n = int(input())

s = []
for _ in range(n):
    command = input()
    query_index, params = command.split(' ')
    query_index = int(query_index)
    query_mapper[query_index](s, *params)

