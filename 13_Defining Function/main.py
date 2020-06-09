# define function
def say():
	print("say, Hi")

# call
"""
# you can call/use more!	
say()
say()
say()
say()
"""

# function argumen
"""
def estudent(name):
	print(f"estudent name : {name}")

estudent("juliao")
"""

def estudent(name,id):
	print("{}\n\t id : {}".format(name,id)) 

estudent("juliao",127)
"""
x incorrect write argumen when call function
estudent(120,"joaquim")
"""
# solve
estudent(id=120,name="joaquim")
estudent(name="leonardo",id=122)

# return
def equals():
	return 30*"="

a = equals()
print(a)
print(equals())

# local & global
dogname = "elefante" # local variable
color = "black & white"

# define 
def change(newname,newcolor):
	global dogname,color

	dogname = newname
	color = newcolor
	print("change dog name to", dogname)
	print("color", color)

# call 
change("metan","black")

print("now dog name", dogname, "color", color)

# can call function inside function
def voice_cat():
	print("miaaaauu *~*")

# default argumen
def color_cat(color="Orange"):
	# call function
	voice_cat()
	print("color", color)

def set_cat(name=None):
	print("cat name :", name, "\n== INFO ==")
	color_cat()

print('\n')
# call function
set_cat(name="celi")

print(50*"+")
# lambda functions

addition = lambda x,y: print(x+y)

addition(4,3)

subtration = lambda a,b: a-b

print(subtration(3,9))

copyright = lambda : print("c 2020. jm-kodigu")

copyright()