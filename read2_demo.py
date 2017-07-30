'''readchar, readline demo'''
def process(string):
	print('Processing: ', string)

def readEachChar(fileName):
	f = open(fileName)
	while True:
		char = f.read(1)
		if not char: break
		process(char)
	f.close()

def readEachLine(fileName):
	f = open(fileName)
	while True:
		line = f.readline()
		if not line: break
		process(line)
	f.close

def readCharIterator(fileName):
	f = open(fileName)
	for char in f.read():
		process(char)
	f.close()

def readLineIterator(fileName):
	f = open(fileName)
	for line in f.readline():
		process(line)
	f.close()

#demo1
fileName = '/Users/py/python/read_demo.txt'
print('readChar_demo: ')
readEachChar(fileName)
print()

#demo2
print('readLine_demo: ')
readEachLine(fileName)
print()

#demo3
print('readCharIterator_demo: ')
readCharIterator(fileName)
print()

#demo4
print('readLineIterator: ')
readLineIterator(fileName)
