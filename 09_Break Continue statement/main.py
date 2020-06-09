"""
for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print(n, 'equals', x, "*", n//x)
			#break
	else:
		print(n, "is a prime number!")
"""

# using break statement
for i in range(1,18):
	if i == 12:
		print("your number is", i)
		break
	print(i)
else:
	print('outside for loops!')

print("="*30)

# using continue statement
for i in range(1,18):
	if i == 12:
		print("your number is", i)
		continue
	print(i)
else:
	print('outside loops!')