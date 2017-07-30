class Reverse:
	"""Iterator for looping over a sequence backwards"""
	def _init_(self, data):
		self.data = data
		self.index = len(data)

	def _iter_(self):
		return self

	def _next_(self):
		if self.index==0:
			raise StopIteration
		self.index-=1
		return self.data[self.index]

 >>> rev = Reverse('spam')
    iter(rev)

    for char in rev:
    	print(char)