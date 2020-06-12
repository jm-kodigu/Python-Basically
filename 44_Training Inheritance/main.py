# superclass
class Estudent:
	# private class variable
	__total_estudent = 0

	# const __init__()
	def __init__(self,name,id,math_exercise,math_homework):
		self.__name = name
		self.__id = id
		self.__exercise = math_exercise
		self.__homework = math_homework
		self.__exame = 0
		self.__total = 0
		Estudent.__total_estudent += 1

	@property
	def info(self):
		return f"{self.__name} \n\t id : {self.__id} \n\t math score : \n\t\t a. exercise : {self.exercise} \n\t\t b. homework : {self.homework} \n\t\t c. exame : {self.exame} \n\t\t d. total : {self.__total}"

	@property
	def exercise(self):
		pass
	
	@property
	def homework(self):
		pass

	@property
	def exame(self):
		pass

	@property
	def total(self):
		pass

	@exercise.getter
	def exercise(self):
		return self.__exercise

	@homework.getter
	def homework(self):
		return self.__homework

	@exame.getter
	def exame(self):
		return self.__exame

	@exame.setter
	def exame(self,input):
		self.__exame = input
		self.total

	@total.getter
	def total(self):
		self.__total = (self.exercise + self.homework + self.exame) // 3
		
		if 100>=self.__total>=90:
			print(self.__name + " you're got score A!")
		elif 90>self.__total>=80:
			print(self.__name + "you're got score B!")
		elif 80>self.__total>=60:
			print(self.__name + "you're got score C!")
		else:
			print(self.__name + "you're not passed!")

# subclass
class Juliao(Estudent):
	# const __init__
	def __init__(self,name):
		# call superclas
		super().__init__(name,111,math_exercise=70,math_homework=100)

# subclass
class Rivaldo(Estudent):
	# const __init__
	def __init__(self,name,):
		# call superclass
		super().__init__(name,112,83,98)

# subclass
class Joaquim(Estudent):
	# const __init__
	def __init__(self,name):
		# call superclass
		super().__init__(name,113,100,76)


# object 
juliao = Juliao("juliao")
rivaldo = Rivaldo("rivaldo")
joaquim = Joaquim("joaquim")


print(juliao.info)
juliao.exame = 90
print(juliao.info)

print("#"*20)

print(rivaldo.info)
rivaldo.exame = 93
print(rivaldo.info)

print("+"*20)

print(joaquim.info)
joaquim.exame = 46
print(joaquim.info)