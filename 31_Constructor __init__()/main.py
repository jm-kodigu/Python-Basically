# template
class Estudent:
	# constructor __init__()
	def __init__(self,inputName,inputId,inputEmail,inputAddress):
		# object attribute
		self.name = inputName
		self.id = inputId
		self.email = inputEmail
		self.address = inputAddress


# object
aprilia = Estudent("aprilia",114,"aprilialili@gmail.com","bebonuk")
aurito = Estudent(inputName="aurito",inputId=115,inputAddress="cacaulidu",inputEmail="auritorita@gmail.com")
auxilia = Estudent("auxilia",116,"auxilaxila@gmail.com","kuluhun")

print(aprilia.name)
print(aprilia.address)
print(auxilia.id)
print(auxilia.email)
print(aurito.__dict__)