# superclass
class Zoo:
	# const __init__
	def __init__(self,name,id):
		self.name = name
		self.id = id

# subclass
class Lion(Zoo):
	pass

# subclass
class Bison(Zoo):
	pass


# object
monkey = Zoo("monkey",980)	
lion = Lion("lion",112)
bison = Bison("bison",101)

# how to see inheritance
# print(help(lion))

print(monkey.__dict__)
print(lion.__dict__)
print(bison.__dict__)