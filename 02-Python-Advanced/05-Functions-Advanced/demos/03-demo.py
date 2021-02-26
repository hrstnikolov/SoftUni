def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{value}, {key}")


def greet_me_2(dct):
    for key, value in dct.items():
        print(f"{value}, {key}")


d = {
    'Peter': 'Hello',
    'George': 'Bye',
}

greet_me(Peter="Hello", George="Bye")
greet_me_2(d)

d.get('Peter')
d['Peter']