counts = dict()
try:
	f = open('romeo.txt', 'r')
	for line in f:
		words = line.split()
		if len(words) == 0 or words[0] != 'From': continue
		else:
			if words[2] in counts:
				counts[words[2]] += 1
			else:
				counts[words[2]] = 1
except:
	print('File Not Found!')
	exit()
print(counts)