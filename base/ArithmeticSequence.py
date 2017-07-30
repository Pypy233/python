def checkIndex(key):
	#Check whether the index can be accepted
	if not isinstance(key, (int, long)): raise TypeError
	else:
		if key<0:
			raise IndexError

class ArithmeticSequence:
	def _init_(self, start = 0, step = 1):
		self.start = start
		self.step = step
		self.changed = {}

	def _getItem_(self, key):
		checkIndex(key)
		try:
			return self.changed(key)
		except KeyError:
			return self.start + key*self.step

	def _setItem_(self, key, value):
		checkIndex(key)
		self.changed[key] = value