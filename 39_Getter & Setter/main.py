# template
class Estudent:
	# private class variable
	__total = 0

	# const __init__()
	def __init__(self,name,id,departament,email,address):
		# private object variable
		self.__name = name
		self.__id = id
		self.__departament = departament
		self.__email = email
		self.__address = address


	@property
	def info(self):
		return "{} \n\t id : {} \n\t departament : {} \n\t email : {} \n\t address : {} \n".format(self.__name,self.__id,self.__departament,self.__email,self.__address)

	# getter
	@property
	def name(self):
		pass

	@name.getter
	def name(self):
		return self.__name

	@property
	def email(self):
		pass

	@email.getter
	def email(self):
		return self.__email

	@property
	def address(self):
		pass

	@address.getter
	def address(self):
		return self.__address

	# setter
	@property
	def departament(self):
		pass

	@departament.setter
	def departament(self,changed):
		self.__departament = changed

	@address.setter
	def address(self,newaddress):
		self.__address = newaddress

# object
lizania = Estudent("lizania",131,"computer science","lizaniaaza@gmail.com","taibesi")
marciana = Estudent("marciana",133,"computer enginner","marciaandbear@gmail.com","matdoru")

print(lizania.info)
print(marciana.info)

print(marciana.name)
print(lizania.email)
print(lizania.address)
print(marciana.address)

lizania.departament = "software enginner"
marciana.address = "tibar"

print(lizania.info)
print(marciana.info)