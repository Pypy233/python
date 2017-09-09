lst = list()
arr = list()

def Combination(n, r):
	arr = [1, 2, 3, 4, 5]
	lst = [1, 1, 1]

	if(n < r):
		return ;
	elif(n == 1):
		for i in lst:
			print(i, end = ' ')
			print()
	else:
		Combination(n - 1, r - 1)
		lst[r - 1] = arr[n - 1]
		Combination(n - 1, r)
def main():
	'''print('Enter the number n: ')
	n = input()
	print('Enter the number r: ')
	r = input()'''
	Combination(5, 3)

main()