class Estudent:

	# magic method
	def __init__(self,name,id):
		self.name = name
		self.id = id

	# debug
	def __repr__(self):
		return "DEBUG --> object of Estudent " + self.name

	# info
	def __str__(self):
		return "object of Estudent " + self.name

	# addition 
	def __add__(self1,self2):
		return self1.id + self2.id

	# dictionary
	@property
	def __dict__(self):
		return f"== name : {self.name} = id : {self.id} =="


serafina = Estudent("serafina",112)
rivaldo = Estudent("rivaldo",122)
teresinha = Estudent("teresinha",121)

print(serafina)
print(serafina + teresinha)
print(rivaldo.__dict__)