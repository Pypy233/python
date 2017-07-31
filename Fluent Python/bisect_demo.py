import bisect
def grade(scores, breakpoints = [60, 70, 80, 90], grades = 'FDCBA'):
	i = bisect.bisect(breakpoints, scores)
	return grades[i]

#demo
print([grade(score) for score in [0 , 80, 100, 99, 2, 9, 70, 65]])
