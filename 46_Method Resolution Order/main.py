# superclass
class A:
	# method
	def show(self):
		print("Method A!")

# superclass
class B:
	# method 
	def show(self):
		print("Method B!")

# subclass
class C(B,A):
	pass


# object 
test = C()

# checked
print(help(test))

print(50*"=")

test.show()