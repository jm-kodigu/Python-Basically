class A:
	def show(self):
		print("method A!")

class B(A):
	def show(self):
		print("method B!")

class C(A):
	def show(self):
		print("method C!")

class D(C,B):
	pass


test = D()

test.show()