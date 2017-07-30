from math import hypot
class MyVector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def setVector(self, x, y):
		self.x = x
		self.y = y

	def getVector(self):
		return (self.x, self.y)

	def add(v1,v2):
		return (v1.x + v2.x, v1.y + v2.y)

	def abs(self):
		return hypot(self.x, self.y)

	def bool(self):
		return bool(abs(self))

	def mul(self, scalar):
		x = self.x * scalar
		y = self.y * scalar
		return (x, y)

	def mulProduct(v1, v2):
		product = v1.x * v2.x + v1.y * v2.y
		return product

#demo
v1 = MyVector()
v2 = MyVector()
v3 = MyVector()
v1.setVector(3, 4)
v2.setVector(1, 3)
v3.setVector(0, 0)
print('The abs val of v1 :', v1.abs(), ', and the abs val of v2 :', v2.abs())
print('Whether v1 is zero vector? ', bool(v1), ' and v3?', bool(v3))
print('The v1 mul 3 is :', v1.mul(3))
print('V1 * v2 is :', v1.mulProduct(v2))
