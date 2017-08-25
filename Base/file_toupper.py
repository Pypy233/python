try:
	f = open('read.txt', 'r')
	f1 = open('target.txt', 'w')
	while 1:
		line = f.readline()
		if not line:
			break
		else:
			print(line.upper())
			f1.write(line.upper())
	f.close()
	f1.close()

except:
	print('File Not Found!')
	exit()