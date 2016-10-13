# i2p - Homework - 8; Modules - Part 1
# By: Roopa Prakash, submitted on: 06/23/2016

class Dog(object):
	def __init__(self, name, size):
		self.name = name
		self.size = size
		
	def Bark(self):
		return 'woof woof! I\'m a ' + self.size + ' sized dog'
		
	def Greet(self):
		return 'My name is ' + self.name + ' and I LOVE YOU!'