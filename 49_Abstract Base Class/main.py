from abc import ABC,abstractmethod

# class abstract
class Button(ABC):

	# constructor __init__()
	def __init__(self,seTlink):
		self.link = seTlink

	@abstractmethod
	def click(self):
		pass

	@property
	@abstractmethod
	def link(self):
		pass

# class / instance
class Pushbutton(Button):

	def click(self):
		print('go to : https://' + self.link)

	@Button.link.setter
	def link(self,input):
		self.__link = input

	@link.getter
	def link(self):
		return self.__link

button1 = Pushbutton('www.jm-kodigu.com')

button1.click()