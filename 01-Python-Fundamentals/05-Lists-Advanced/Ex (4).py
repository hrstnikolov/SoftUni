old_version = input().split('.')

new_version = int(''.join(old_version)) + 1

print('.'.join(str(new_version)))