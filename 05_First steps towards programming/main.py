a,b = 0,1
while a < 200:
	print(a, end=",")
	a,b = b, a+b
print()

date = 0

while date < 20:
	print(date)
	date += 1 # or equal date = date + 1
else:
	print("finally :", date)

begin = 0
final = 100

while begin < final:
	print(begin, end=",")
	begin += 1
else:
	print("end of :", begin)
