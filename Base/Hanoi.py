def move(disk_number, N, M):
	print('The ' +disk_number++ + 'from '+'N to M is ' )
def Tower(self, A, B, C, n):
	if(n==1):
		print('The time is the end.')
	else:
		move(n-1, A, B)
		Tower.move(n, B, C)
		move(n-1, B, A)
		n-=1
Tower('A', 'B', 'C', 3)	
