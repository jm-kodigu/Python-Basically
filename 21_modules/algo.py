def buble(date):
	for x in range(len(date)-1,0,-1):
		for y in range(x):
			if date[y] > date[y+1]:
				temp = date[y+1]
				date[y+1] = date[y]
				date[y] = temp