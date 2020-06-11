# superclass
class Zoo:
	# const __init__
	def __init__(self,name,id):
		self.name = name
		self.id = id

	# method
	def showinfo(self):
		print(f"animals\n\tname : {self.name}\n\tid : {self.id}\n")


# subclass
class Lion(Zoo):
	# const __init__
	def __init__(self,name):
		# call superclass
		# Zoo.__init__(self,name = name,id = 112)
		super().__init__(name,112)
		super().showinfo()

# subclass
class Monkey(Zoo):
	# const __init__
	def __init__(self,name):
		# call superclass
		super().__init__(name,980)
		# Zoo.showinfo(self)
		super().showinfo()
		

# object
lion = Lion("lion")
monkey = Monkey("monkey")