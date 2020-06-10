def buble_sort(date):
	for x in range(len(date)-1,0,-1):
		for y in range(x):
			if date[y] > date[y+1]:
				temp = date[y+1]
				date[y+1] = date[y]
				date[y] = temp

def info():
	print("algorithm module. built by jm-kodigu")

if "__main__" == __name__:
	info()