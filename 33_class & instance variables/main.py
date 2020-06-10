# template
class Estudent:
	# class variable
	departament = '"departament"'

	# constructor __init__()
	def __init__(self,name,id):
		# object variable
		self.name = name
		self.id = id


# object
basilio = Estudent("basilio",119)
beatriz = Estudent("beatriz",120)

print(basilio.__dict__)
print(beatriz.__dict__)

print(basilio.departament)

# override variable
beatriz.departament = "computer science"

print(beatriz.departament)

print(basilio.__dict__)
print(beatriz.__dict__)

# add variable in object
basilio.hobby = "dance"

print(basilio.hobby)

print(basilio.__dict__)
print(beatriz.__dict__)

print(20*"=")

print(basilio.hobby)
print(beatriz.departament)