# template
class Estudent:
	# private variable
	__total = 0

	# const __init__()
	def __init__(self,name,id):
		self.__name = name
		self.__id = id
		self.__exercise = 0
		self.__homework = 0
		self.__exame = 0
		self.__math_score = (self.__exercise + self.__homework + self.__exame) // 3
		Estudent.__total += 1

	@classmethod
	def total_estudent(self):
		print(Estudent.__total)

	@property
	def info(self):
		return "{} \n\t id : {} \n\t math score \n\t\t a.exercise : {} \n\t\t b.homework : {} \n\t\t c.exame : {} \n\t\t d.total : {}".format(self.__name,self.__id,self.__exercise,self.__homework,self.__exame,self.__math_score)

	@property
	def exercise(self):
		pass

	@property
	def homework(self):
		pass

	@property
	def exame(self):
		pass

	@exercise.getter
	def exercise(self):
		return self.__exercise

	@exercise.setter
	def exercise(self,input):
		self.__exercise = input

	@homework.getter
	def homework(self):
		return self.__homework

	@homework.setter
	def homework(self,input):
		self.__homework = input

	@exame.setter
	def exame(self,exame_score):
		self.__exame = exame_score
		self.__math_score = (self.__exame + self.exercise + self.homework) // 3
		if (self.__math_score >= 100 and self.__math_score > 90):
			print("you got score A!")
		elif (self.__math_score >= 80 and self.__math_score > 70):
			print("you got score B!")
		elif (self.__math_score >= 70 and self.__math_score > 60):
			print("you got score C!")
		else:
			print(self.__name + " you're not passed!")


# object
maria = Estudent(name="maria",id=150,)
nuno = Estudent(id=151,name="nuno")
suzana = Estudent(152,"suzana")

print(maria.info)
maria.exercise = 85
maria.homework = 94
maria.exame = 78
print(maria.info)

print("#"*40)

print(nuno.info)
nuno.exercise = 40
nuno.homework = 70
nuno.exame = 55
print(nuno.info)