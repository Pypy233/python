import math
import random
def dice():
 # As the sum of three dices is the range of 3 to 18
	sum = 0;
	num = 0;
	sumLst = []
	for i in range(0, 20):
		sumLst.append(0)
	for i in range(0, 10000):
		for j in range(0, 3):
			num = random.randint(1, 6)
			sum += num
		sumLst[sum]+=1
		sum = 0

	for i in range(0, 20):
		print(i, end = ' ')
		print(sumLst[i])

def main():
	dice()
main()



