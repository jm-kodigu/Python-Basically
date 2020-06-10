def selection_sort(date):
	for i in range(5):
		minpos = i
		for j in range(i,6):
			if date[j] < date[minpos]:
				minpos = j

		temp = date[i]
		date[i] = date[minpos]
		date[minpos] = temp		