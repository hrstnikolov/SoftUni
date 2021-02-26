def print_personal_info(**kwargs):
    if kwargs.get('name'):
        print(f"The person name is {kwargs['name']}")
    else:
        print('No name is given')

    if kwargs.get('age'):
        if kwargs['age'] >= 18:
            print('Adult')
        else:
            print('too young')
    else:
        print('No age for this person')


print_personal_info(name='Hristo')
print_personal_info(name='Anatoli', age=20)
print_personal_info(height=182.44, name='Mike', interests=(), age=4)
print_personal_info(**{'name': 'Gosho', 'age': 3})


