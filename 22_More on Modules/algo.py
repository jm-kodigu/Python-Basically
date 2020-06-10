def buble(date):
	for x in range(len(date)-1,0,-1):
		for y in range(x):
			if date[y] > date[y+1]:
				temp = date[y+1]
				date[y+1] = date[y]
				date[y] = temp

def selec(date):
	for i in range(5):
		minpos = i
		for j in range(i,6):
			if date[j] < date[minpos]:
				minpos = j

		temp = date[i]
		date[i] = date[minpos]
		date[minpos] = temp		