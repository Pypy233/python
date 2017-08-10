def print_lol(the_list):
	for item in the_list:
		if(isinstance(item, list)):
			print_lol(item)
		else:
			print(item)

demo = ['s', 'g', [1, 2, 3, [1, [2, 3, 4], 5]], ['demo', 'demo1', 'demo2' ], 'a']
print_lol(demo)