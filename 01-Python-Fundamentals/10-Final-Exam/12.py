def new_follower(records, user):
    if user not in records:
        records[user] = {'likes': 0, 'comments': 0}


def like(records, user, count):
    count = int(count)
    if user not in records:
        records[user] = {'likes': count, 'comments': 0}
    else:
        records[user]['likes'] += count


def comment(records, user):
    if user not in records:
        records[user] = {'likes': 0, 'comments': 1}
    else:
        records[user]['comments'] += 1


def blocked(records, user):
    if user in records:
        records.pop(user)
    else:
        print(f"{user} doesn't exist.")


mapper = {
    'New follower': new_follower,
    'Like': like,
    'Comment': comment,
    'Blocked': blocked
}

records = {}
while True:
    data = input().split(': ')
    command = data[0]
    if command == 'Log out':
        break

    mapper[command](records, *data[1:])

summed_records = {}
for key, value in records.items():
    summed_records[key] = value['likes'] + value['comments']
sorted_records = dict(sorted(summed_records.items(), key=lambda x: (-x[1], x[0])))

print(f'{len(records.keys())} followers')
for user, value in sorted_records.items():
    print(f'{user}: {value}')
