import math
import random
def dice():
	sumLst = []
	for i in range(0, 6):
		sumLst.append(0)
	for i in range(0, 1000):
		num = random.randint(0, 5)
		sumLst[num]+=1

	for i in range(0, 6):
		print(i + 1, end = ' ')
		print(sumLst[i])

def main():
	dice()
main()


