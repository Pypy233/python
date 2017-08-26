counts = dict()
try:
	f = open('romeo.txt', 'r')
	for line in f:
		if line.startswith('From'):
			words = line.split()
			if words[3] in counts:
				counts[words[3]] += 1
			else:
				counts[words[3]] = 1
except:
	print('File Not Found!')
	exit()
print(counts)