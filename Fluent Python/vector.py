# Implement vector, override some necessary or unnecessary methods...
from math import hypot


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r) ' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return abs(self)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return x + y


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = Vector(-1, 1)
vector_list = [v1, v2, v3]
for i in range(3):
    print(vector_list[i])
    print(abs(vector_list[i]))

print(v1 + v2)
print(v2 + v3)
print(v1 + v3)
print(v1 * v2)
print(v1 * v3)



