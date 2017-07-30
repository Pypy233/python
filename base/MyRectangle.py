import math
class MyRectangle:
	def _init_(self):
		self.width = 0
		self.height = 0
		self.times = 1
	def setSize(self, size):
		self.width, self.height, self.times = size
	def getSize(self):
		self.width = self.width * self.times
		self.height = self.height * self.times
		return self.width, self.height
	size = property(getSize, setSize)


r = MyRectangle()
r.size = (15, 10 , 10)
print(r.getSize())
print("width: {0}, height: {1}".format(r.width, r.height))
r.width = 5
r.times = 2
r.height = math.pi
print(r.getSize())