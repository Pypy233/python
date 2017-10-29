import random
import math
def modify():
	sum = 0
	sumList = []
	for i in range(1, 20):
		sumList.append(0)
	for i in range(0, 1000):
		for j in range(0, 3):
			sum += random.randint(1, 6)
			sumList[sum] += 1
		sum = 0
	for i in range(1, 19):
		print(i, end = ' ')
		print(sumList[i])
def main():
	modify()
main()