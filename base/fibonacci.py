def fib1(n):
	a, b = 0,1
	while b<n:
		print(b, end = ' ')
		a, b = b, a+b
		print()

def fib1Tuble(n):
	a, b = 0,1
	result = []
	while b<n:
		print(b, end = ' ')
		a, b = b, a+b
		print()

def fib2(n):
	a, b, count = 0, 1, 0
	while count<n:
		print(b, end = ' ')
		a, b = b, a+b
		count+=1
		print()
		

def fib2Tuble(n):
	a, b, count = 0, 1, 0
	result = []
	while count<n:
		print(b, end = ' ')
		a, b = b, a+b
		count+=1
		print()

