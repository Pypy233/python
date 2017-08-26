counts = dict()
try:
	f = open('romeo.txt', 'r')
	for line in f:
		words = line.split()
		for word in words:
			if word not  in counts:
				counts[word] = 1
			else:
				counts[word] += 1
except:
	print('File Not Found!')
print(counts)