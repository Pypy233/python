'''The classic problem: eight queens
		EightQueens.py'''
	# Judge whether the position conflicts with each other
def conflict(state, nextX):
		nextY = len(state)
		for i in range(nextY):
			if abs(state[i] - nextX) in (0, nextY - i):
				return True
		return False
		''' recursion'''
def queens(num, state = ()):
	
	if len(state) == num-1:
		for i in range(num):
			if not conflict(state, i):
				yield(i, )
	else:
		for i in range(num):
			if not conflict(state, i):
				for result in queens(num, state + (i, )):
					yield(i, ) + result
						

#demo:
for i in list(queens(8)):
	print(i)



