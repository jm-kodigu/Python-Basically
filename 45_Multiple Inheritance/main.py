# superclass
class Superman:
	
	# method
	def whs_superman(self):
		print(self.name + ' is superman')

# superclass
class Person:
	
	# method
	def info(self):
		print("he name is", self.name)

# subclass
class Who(Superman,Person):
	# const __init__
	def __init__(self,name):
		self.name = name


# object
joaquim = Who("joaquim")

# checked 
# print(help(joaquim))

joaquim.whs_superman()
joaquim.info()