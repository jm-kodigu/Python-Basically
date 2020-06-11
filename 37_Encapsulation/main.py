# template
class Estudent:
	# private class variable
	__total = 0

	# const __init__()
	def __init__(self,name,id):
		# private object variable
		self.__name = name
		self.__id = id
		Estudent.__total += 1

	# method as getter & setter (standar paradigm)
	
	# getter
	def showname(self):
		print(self.__name)

	def showid(self):
		return self.__id

	# setter
	def ChangeName(self,new):
		self.__name = new

	def change_id(self,new):
		self.__id = new


# object
joaquim = Estudent("joaquim",118)
leonardo = Estudent("leonardo",119)
licenia = Estudent("licenia",212)

joaquim.showname()

print(leonardo.showid())
leonardo.change_id(789)
print(leonardo.showid())

licenia.ChangeName("lice")
licenia.showname()