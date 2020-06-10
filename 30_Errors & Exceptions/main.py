while True:
	try:
		a = int(input("first number "))
		b = int(input("division number "))
		t = a / b # + c
		print("result : " + str(t))
		break
	except ValueError:
		print("oops! that's not a number!")
	except ZeroDivisionError:
		print("oops! can't division by zero!")
	except NameError:
		print("Variable isn't defined!")
	except Exception as err:
		print(err)

try:
	import pandas
except ImportError:
	print("no module name panda!")

print("="*30)

# define function
def division(a,b):
		try:
			t = a / b
		except ZeroDivisionError:
			print("can't division by zero")
		else:
			print("result : " + str(t))
		finally:
			print("== finally program! ==")

# call function
division(1,0) 

print("x"*20)

division(35,7)
