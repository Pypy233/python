def binarySearch(sequence, target, lower, upper):
	sequence = sorted(sequence)
	print(sequence)
	if sequence==None:
		print("The sequence is not existed!")
	else:
		middle = (lower+upper)//2
		if lower == upper:
			assert target == sequence[upper], "The target number is not existed!"
			return upper
		else:
			if(target > sequence[middle]):
				return binarySearch(sequence, target, middle+1, upper)
			else:
				return binarySearch(sequence, target, lower, middle)

sequence = [0, 999, 111, 222, 333, 4, 555]
n = binarySearch(sequence, 111, 0 ,5)
print(n)
n = binarySearch(sequence,22,0,5)