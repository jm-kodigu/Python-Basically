# template
class Estudent:
	# private class varible
	__total = 0

	# const __init__()
	def __init__(self,name,departament):
		# object variable
		self.name = name
		self.departament = departament

		# public object varible
		# self.hobby = '"hobby"'
		# protected 
		# self._hobby = '"hobby"'
		# private 
		self.__hobby = '"hobby"'
		Estudent.__total += 1


# object
hermengildo = Estudent("hermengildo","computer science")
ilda = Estudent("ilda","software enginner")
januario = Estudent("januario","computer science")

'''
print(hermengildo.__dict__)
print(hermengildo.hobby)
# override public variable 
hermengildo.hobby = "play guitar"
print(hermengildo.hobby)
print(hermengildo.__dict__)


print(januario.__dict__)
print(januario._hobby)
# override protected variable
januario._hobby = "estudy"
print(januario._hobby)
print(januario.__dict__)

print(ilda.__dict__)

# try to access
# print(ilda.__hobby)
# print(ilda.hobby)

# override
# ilda.__hobby = "sign"
# it's add new items in object not override default in class
#print(ilda.__hobby) 
'''