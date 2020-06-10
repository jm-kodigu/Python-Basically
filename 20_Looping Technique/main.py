languag = {"python":"interpreter languague","java":"compiler languague"}

for lang, mode in languag.items():
	print(f"{lang} is {mode}")

for i, d in enumerate(["nana","nene","nini","nono","nunu"]):
	print(i, ":", d)

questions = ["name","favorite programming languague","favorite color"]
answer = ["juliao","python & java","lightblue"]

for q,a in zip(questions,answer):
	print("what's your {0}? it's {1}".format(q,a))

for i in reversed(range(1,10,2)):
	print(i)

animals = {"lion","cow","snake","giraffe"}

for x in sorted(set(animals)):
	print(x)

"""
that's my looping techquine for dictionary inside of the dictionary
- jmkodigu
"""

print(50*"=")

print("Estudent")

# date estudent
estudent_1 = {"ID":111,"name":"marciana martins","email":"marciamarciana@gmail.com","address":"matadoru"}
estudent_2 = {"ID":112,"name":"maria estrela","email":"marimariastar@gmail.com","address":"maskarinias"}
estudent_3 = {"ID":113,"name":"joaquim gomes","email":"aquimsempre@gmail.com","address":"vila-verde"}

estudent = {
	111:estudent_1,
	112:estudent_2,
	113:estudent_3
}

# get values in dictionary
for a in estudent.values():
	# get all items in dictionary
	print() # for espace date
	for k,v in a.items():
		print(f"{k} : {v}") # see result