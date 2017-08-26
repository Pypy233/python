numlist = list()
while True:
	print('Enter a number:')
	num = input()
	if num == 'done': break
	else: numlist.append(num)
print('The max: ', max(numlist))
print('The min: ', min(numlist))