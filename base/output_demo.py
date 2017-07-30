s = 'Hello world!'
print(str(s))
print(repr(s))
#Double demo
print(str(1/3))
x = 10*37.2332
y = 7*23.43436
print("The value of x is ",repr(x)," and the value of y is ",repr(y))
print("The value of x is "+repr(x)," and the value of y is ",repr(y))
print(x,y,repr('demox'),repr('demo(x+1)'))
for x in range(1,11):
	print(repr(x).rjust(3), repr(x*x).rjust(3), end = ' ')
	print(repr(x*x*x).rjust(4))
for n in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(n, n*n, n*n*n))