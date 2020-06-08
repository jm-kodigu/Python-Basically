for i in ['cat','dog','cow','elephant']:
	print(i, len(i))

print(20*"=")

animal = ['tiger','horse','monkey','lion']
item = ['basketbal','banana','t-shirt','notebook']

items = [animal, item]

for i in items:
	for j in i:
		print(j, len(j))