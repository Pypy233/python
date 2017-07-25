try:
	x = input("Enter the first number: ")
	y = input("Enter the second number: ")
	print(x/y)
except ZeroDivisionError:
	print("Divisor can't be zero!")
