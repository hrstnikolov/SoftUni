class A:
    def __init__(self, value_a):
        self.value_a = value_a

    def __repr__(self):
        return f'Class A {self.value_a}'


class B:
    def __init__(self, value_b):
        self.value_b = value_b

    def __repr__(self):
        return f'Class B {self.value_b}'

# тук имаме пример за
# Mro = Method Resolution Order
# т.е. реда на викане на класовете
class C(A, B):
    def __init__(self, a, b):
        # super().__init__(a)  # така super реферира само към клас А
        A.__init__(self, a)
        B.__init__(self, b)

    def __repr__(self):
        return f'{A.__repr__(self)}, {B.__repr__(self)}'


c = C(1, 2)
print(c)
print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(help(C))
