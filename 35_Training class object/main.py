# template 
class Estudent:
	# class variable
	total = 0

	# const __init__()
	def __init__(self,name,id,departament,email,address):
		# object variable
		self.name = name
		self.id = id
		self.departament = departament
		self.email = email
		self.address = address
		# use const to initializa method
		self.showinfo()

	# method
	def showinfo(self):
		print(f"{self.name}\n\tid : {self.id}\n\tdepartament : {self.departament}\n\temail : {self.departament}\n\taddress : {self.address}\n")

	# dialogue Greeting anoter one
	def great_morning(self,self2):
		print("\nGreeting another one!")
		print(f"\"{self.name}\" : good morning {self2.name}.")
		self2.get_greatmorning(self)

	def get_greatmorning(self,self2):
		print(f"\"{self.name}\" : good morning to you {self2.name}.\n")

	def great_afternoon(self,self2):
		print("\nGreeting another one!")
		print(f"\"{self.name}\" : good afternoon {self2.name}.")
		self2.get_greatafternoon(self)

	def get_greatafternoon(self,self2):
		print(f"\"{self.name}\" : good afternoon to you {self2.name}.\n")

	def great_evening(self,self2):
		print("\nGreeting another one!")
		print(f"\"{self.name}\" : good evening {self2.name}.")
		self2.get_greatevening(self)

	def get_greatevening(self,self2):
		print(f"\"{self.name}\" : good evening to you {self2.name}.\n")


# object
elia = Estudent(id=321,name="elia",email="eliaamaarl@gmail.com",departament="computer science",address="hudilaran")
eusebio = Estudent("eusebio",323,"software enginner","eusebicoaro@gmail.com","beto-timur")
genilda = Estudent("genilda",333,"software enginner","genildaliiil@gmail.com","becora")
goransia = Estudent("goransia",212,"computer science","gogoransiiia@gmail.com","metinaru")

elia.great_morning(eusebio)
eusebio.great_morning(elia)

genilda.great_afternoon(goransia)
eusebio.great_evening(genilda)