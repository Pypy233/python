#numberlines.py

import fileinput

for line in fileinput.input(inplace = 1):
	line = line.rstrip()
	num = line.lineno()
	print()