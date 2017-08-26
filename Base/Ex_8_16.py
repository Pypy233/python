lst = list()
try:
	f = open('romeo.txt', 'r')
	for line in f:
		words = line.split()
		for word in words:
			if word in lst or len(word) == 0: continue
			else:
				lst.append(word)
except:
	print('File Not Found!')
lst = sorted(lst)
for word  in lst:
	print(word, end = ' ')