# template
class Estudent:
	# private class attribute
	__total = 0

	# cons __init__
	def __init__(self,name,address):
		# private object attribute
		self.__name = name
		self.__address = address
		Estudent.__total += 1

	# staticmethod
	@staticmethod
	def total():
		print(Estudent.__total)

	# classmethod
	@classmethod
	def Total(cls):
		print(cls.__total)


# object
luduvina = Estudent("luduvina","lahane")
Estudent.total()
luduvina.total()
lourdes = Estudent("lourdes","audian")
Estudent.Total()
lourdes.Total()
lijenia = Estudent("lijenia","becora")
lijenia.total()