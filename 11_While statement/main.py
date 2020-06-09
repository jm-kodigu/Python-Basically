a = 0 # initialize value

while a < 10:
	if a == 3:
		print('your number is', a)
		a += 1
		continue
	print(a)
	a += 1 # or equals a = a + 1
else:
	print('end :', a)

print("*"*20)

while True:
	x = str(input("please insert something? "))

	if x in ['qu','qui','quit','ex','exi','exit']:
		print("== program is closed! ==")
		break
	elif len(x) == 0:
		x = "*None*"
		print('write something!')

	print('user input',x)