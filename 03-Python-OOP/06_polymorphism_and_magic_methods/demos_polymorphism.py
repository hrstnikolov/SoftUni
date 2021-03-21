class Shape: pass
class Circle(Shape): pass
c = Circle()

# all True
print(isinstance(c, Circle))
print(isinstance(c, Shape))
print(isinstance(c, object))

