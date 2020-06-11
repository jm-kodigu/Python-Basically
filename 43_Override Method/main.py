# superclass
class Zoo:
	# const __init__
	def __init__(self,name,id):
		self.name = name
		self.id = id

	# method
	def info(self):
		print(f"animal \n\t name : {self.name} \n\t id : {self.id} \n")


# subclass
class Monkey(Zoo):
	# const __init__
	def __init__(self,name):
		# call superclass
		super().__init__(name,980)

	# override method 
	def info(self):
		print(f"animal \n\t name : {self.name} \n\t id : {self.id} \n\t color : chocolate \n")

# subclass
class Lion(Zoo):
	# const __init__
	def __init__(self,name):
		# call superclass
		super().__init__(name,112)

	# override method
	def info(self):
		print("animal \n\t name : {name} \n\t id : {id} \n\t color : yellow \n".format(name=self.name,id=self.id))

# object
monkey = Monkey("monkey")
lion = Lion("lion")

monkey.info()
lion.info()