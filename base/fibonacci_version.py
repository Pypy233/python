''' As a demo for different ways to print fibonacci numbers from 1 to n'''
def fib1(n):
	a, b , count = 0, 1 , 0
	while count < n:
		print(b, end = " ")
		a, b = b, a+b
		count += 1
       #demo1:
print("demo1:", end = " ")
fib1(5)
print(" ")

'''The most common way to relize but it cannot be reused well.'''

def fib2(n):
	a, b , count = 0, 1, 0
	lst = []
	while count < n:
		lst.append(b)
		a, b = b, a+b
		count += 1
	return lst
			#demo2:
print("demo2:", end = ' ')

for num in fib2(5):
	print(num, end = ' ')

'''Though the fib2 can be reused, as the n gets bigger, the expense is more.'''

class fib3(object):
	def __init__(self, n):
		self.n = n 
		self.a, self.b, self.count = 0, 1, 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.count < self.n:
			ran = self.b
			self.a, self.b, self.count = self.b, self.a + self.b, self.count+1
			return ran
		raise StopIteration()

	#demo3
print(' ')
print('demo3:', end = ' ')
f = fib3(5)
for number in f:
	print(number, end = ' ')

'''As can be seen iteror can save expense and more fast'''

def fib4(n):
	count, a, b = 0, 0, 1
	while count < n:
		yield b
		a, b = b, a+b
		count += 1
		#demo4
print(' ')
print('demo4:', end = ' ')
for num in fib4(5):
	print(num, end = ' ')

'''The difference is that this is a generator, while the last is a generator function'''

