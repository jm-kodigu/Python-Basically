"""
that's script i make with python basically syntax
"""

# index
print(17*"+")
print("+ My First Game +")
print(17*"+","\n")

# name prompt
name = str(input("what's your name? "))
print(20*"=")
print("Welcome", name.title())
print(10*"+=")
# your score initialize
score = 10

print('\n')

# while statement
while True:
	# aks prompt
	aks_cont = str(input("do you want to continue (y/n) "))

	if aks_cont.lower() in ['y','ye','yes']:
	
		# question number 1	
		q1 = str(input('which do you choose (apple/grape)? '))
		if q1 == "grape":
			score += 30
			print("good chose!")
		elif q1 == "apple":
			print("incorrect!")
		else:
			print("not match answer!")
			print("*== GAME OVER ==*")
			break

		print('\n')

		# question number 2
		q2 = str(input('do you want (eat/discard)? '))
		if q2 == "eat":
			score += 30
			print("yammi!")
		elif q2 == "discard":
			print("incorrect!")
		else:
			print("not match answer!")
			print("*== GAME OVER ==*")
			break

		print('\n')

		# question number 3
		q3 = str(input("calculate (3*3)+10 = "))
		if q3 == "19":
			score += 30
			print("correct")
		else:
			print("incorrect!")
		
		break # break statement to out the loops

	elif aks_cont.lower() in ['n','no']:
		print("closed!")
		exit() # built in function
	else:
		print('not match!')

print('\n')

if score == 100:
	info = "excelent ^_^"
elif score >= 70:
	info = "good score!"
else:
	info = "bad score ~_~"

print(name, 'you got ' + str(score) + '% score =||=', info,'\nthank you for using my application!')

print('\n')
print("(c) 2020. built by jm-kodigu")