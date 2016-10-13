# i2p - Homework - 6; Challenging Version
# By: Roopa Prakash, submitted on: 06/08/2016

# Part 1 - In class exercises
class Cat(object):
	def __init__(self, name, fur_color, temper):
		self.name = name
		self.fur_color = fur_color
		self.temper = temper
		print self.name + ' the cat has been created and his fur color is ' + self.fur_color + '.'
		
	def Pur(self):
		print 'purrr...purrr...'+ 'my name is ' + self.name
	
	def GetTemperament(self):
		temper_str = ''
		if self.temper >= 5:
			temper_str = 'Angry Cat.'
		elif self.temper >= 2:
			temper_str = 'Normal Cat.'
		else:
			temper_str = 'Mellow Cat.'
		print self.name + ' is a ' + temper_str
			
	def MellowOut(self, mellow_num):
		self.temper = self.temper - mellow_num
		print 'Mellowing ' + self.name + ' out by ' + str(mellow_num) + ' temper points'
		

my_cat = Cat('Garfield', 'Orange', 10)

my_cat.Pur()
my_cat.GetTemperament()
my_cat.MellowOut(6)
my_cat.GetTemperament()
		
# Part 2 - TBD






	



