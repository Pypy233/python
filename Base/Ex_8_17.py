lst = list()
try:
	f = open('mxbox-short.txt', 'r')
	for line in f:
		if not line.startswith('From'): continue
		else:
			words = line.split()
			print(words[1])
	
except:
	print('File Not Found!')

