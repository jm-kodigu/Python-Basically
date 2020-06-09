print(20*"+")
print("""\
+   My FirstGame   +\n\
+                  +\n\
+ </> by Jm-Kodigu +""")
print(20*"+")
print('\n')

# your score
score = 0 # initialize

while True:
	# name prompt
	name = str(input("your name : "))

	if len(name) == 0:
		print("please insert your name!")
	elif len(name) != 0:
		print("\n== Welcome", name.title(), "==")
		
		# ask prompt
		ask = str(input("do you want to continue(y/n) "))
		if ask.lower() in ['y','ye','yes']:
			print('\n')
			
			# question here
			# question 1
			q1 = str(input("Good morning Mr Juliao. How are you? (fine/well) "))
			if q1.lower() == "well":
				score += 20
				print("well, thanks. How are you?")
			elif q1.lower() == "fine":
				print("incorrect!")
			elif len(q1) == 0:
				print(None)
			else:
				print("not match?")
				print("== GAME OVER! ==")
			print('\n')

			# question 2
			q2 = str(input("Tomorrow I will go to (aileu/dili) "))
			if q2.lower() == "aileu":
				score += 20
				print("good chose!")
			elif q2.lower() == "dili":
				print("incorrect!")
			elif len(q2) == 0:
				print(None)
			else:
				print("not match?")
				print("== GAME OVER! ==")
			print('\n')

			# question 3
			q3 = str(input("she wants to (rest/wake) "))
			if q3.lower() == "rest":
				score += 20
				print("because she tired!")
			elif q3.lower() == "wake":
				print("incorrect!")
			elif len(q3) == 0:
				print(None)
			else:
				print("not match!")
				print("== GAME OVER! ==")
			print('\n')

			# question 4
			q4 = str(input("calculate, 1/2 or 1:2, equals : "))
			if q4 == "0.5":
				score += 20
				print("good calculate!")
			elif len(q4) == 0:
				print(None)
			else:
				print("incorrect!")
			print('\n')

			# finally question is 5
			q5 = str(input("how many question did you answered? "))
			if q5 == "5":
				score += 20
				print("of course ^_^")
			elif len(q5) == 0:
				print(None)
			else:
				print("incorrect!")
			print('\n')

			# score calculate
			total = score / 10 
			# info check
			if total >= 10.0:
				info = "excenlent *_*"
			elif total >= 6.0:
				info = "good score!"
			else:
				info = "bad score"

			# finally index
			print(name + ' get score ' + str(total) + '%')
			print('== info : ' + info)
			print('thanks for using my application!\n(c) 2020. jm-kodigu')
			break 

		elif ask.lower() in ['n','no']:
			print("Program is closed!")
			exit()
		else:
			print("not match!")
