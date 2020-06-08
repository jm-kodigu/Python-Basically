"""
x = int(input("please enter an number "))

if x < 0:
	print("negative changed to zero!")
	x = 0
elif x == 0:
	print("zero!")
elif x == 1:
	print("single!")
else:
	print("more!")
"""

x = str(input("do you want continue (y/n) "))

if x in ['y','ye','yes']:
	print("loading ...")
elif x in ['n','no']:
	print("closed!")
else:
	print("not match!")