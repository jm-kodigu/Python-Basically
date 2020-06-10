# template
class Estudent:
	# class variable 
	total = 0

	# const __init__()
	def __init__(self,name,id):
		# object variable
		self.name = name
		self.id = id
		Estudent.total += 1

	# method
	def showtotal(): # none argumen for class 
		print("estudent total :", Estudent.total)

	def show_info(self): # one argumen positional for object
		print("{} \n\tid : {}".format(self.name,self.id))

	def showid(self):
		return "estudent \n\t id => {}".format(self.id)

	def ChangeId(self,newId):
		self.id = newId

# object
carmelinda = Estudent("carmelinda",122)
dircia = Estudent("dircia",123)
donacio = Estudent("donacio",124)
donilia = Estudent("donilia",125)

# call method
carmelinda.show_info()
dircia.show_info()
print(donacio.showid())

print(donilia.__dict__)

donilia.ChangeId(396)

donilia.show_info()
print(donilia.showid())

print(donilia.__dict__)

Estudent.showtotal()