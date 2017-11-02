from math import sqrt
print((sqrt(5) + 1)/2)
def h(x):
	return 7 - (x % 7)
t = (6173, 4344, 9679, 1989)
for i in range(0, 4):
	print(h(t[i]) + t[i] % 10)