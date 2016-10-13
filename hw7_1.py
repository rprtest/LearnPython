# i2p - Homework - 7; OOP Part 2
# By: Roopa Prakash, submitted on: 06/12/2016


# Part 1 - Comma Exercise
''' Format input number to display it with commas '''
def NumFormat(number):
	input_str = str(number)
	input_str_len = len(input_str)
	formatted_str = ''

	while (input_str_len > 3):
		temp_str = ''
		temp_str = ',' + input_str[input_str_len - 3:input_str_len]
		formatted_str = temp_str + formatted_str
		input_str_len = input_str_len - 3
	formatted_str = input_str[0:input_str_len] + formatted_str
	return formatted_str
	
	
print NumFormat(1000)
print NumFormat(1000000)
print NumFormat(12322456)
print NumFormat(123356)
print NumFormat(100)
print NumFormat(1)

print ''

# Part 2 - Main Assignment
''' Parent class - Human '''
class Human(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		print 'Hi, I am ' + self.name
		
	def ThankHeavens(self):
		return 'Thank Gods!'
		
	
''' Child class - Soldier extends Human '''
class Soldier(Human):
	def __init__(self, name, gender, rank):
		super(Soldier,self).__init__(name,gender)
		self.rank = rank
		self.Greet()
	
	''' Function to print that the object is created'''
	def Greet(self):
		print 'Hi there, I am ' + self.name
		print self.rank.upper() + ' ' + self.name + ' reporting!'
		

''' Child class Officer extends Soldier'''
class Officer(Soldier):
	def __init__(self, name, gender, rank, num_subordinates):
		Soldier.__init__(self, name,gender,rank)
		self.num_subordinates = num_subordinates
	
	''' Overriding __setattr__ to check if the value of rank is valid'''
	def __setattr__(self, attribute, value):
		if attribute == 'rank':
			if value not in ['lieutenant','captain','major','colonel','commander','admiral']:
				print 'Invalid officer rank'
			else:
				Soldier.__setattr__(self, attribute, value)
		else:
			Soldier.__setattr__(self, attribute, value)
		
	
	''' Property decorator for num_superior_ranks returns the number of ranks above the current rank '''
	@property
	def num_superior_ranks(self):
		ranks = ['lieutenant','captain','major','colonel','commander','admiral']
		for index, item in enumerate(ranks):
			if self.rank == item:
				return len(ranks) - index - 1

		
''' Child class Admiral extends Officer '''					
class Admiral(Officer):
	def __init__(self, name, gender, num_subordinates):
		if num_subordinates < 10:
			num_subordinates = 10
		super(Admiral,self).__init__(name, gender, 'admiral', num_subordinates)
		
	''' Private Method  '''		
	def __InitiateNuclearStrike(self, target):
		return target + ' anihilated.'
		
''' Base class Cylon'''
class Cylon(object):
	def __init__(self, name, model_number, body_number):
		self.name = name
		self.model_number = model_number
		self.body_number = body_number
	
	''' function to greet after object is built '''
	def Greet2(self):
		print 'I am Model Number ' + str(self.model_number) + ', ' + self.name
		
	def ThankHeavens(self):
		return 'Thank God ...'
	
	def Resurrect(self):
		self.body_number += 1
		return 'Resurrected... '+ str(self.body_number) + ' times'
	
''' Child class HybridBeing ingerits from Human and Cylon class '''
class HybridBeing(Human, Cylon):
	def __init__(self, name, gender, human_parent, cylon_parent):
		super(HybridBeing, self).__init__(name, gender)
		self.model_number = cylon_parent.model_number
		self.body_number = 0
		
		''' Calling the greeting method'''
		super(HybridBeing, self).Greet2()
	 
		
		
		
# Calling the functions, objects, variables per the HW instructions
gbaltar = Human(name = 'Gaius Baltar',
                gender = 'm') 

dee = Soldier(name = 'Dualla',
              gender = 'm',
			  rank = 'specialist')

helo = Officer( name='Agathon',
			    gender = 'm',
			    rank = 'lieutenant',
			    num_subordinates = 0)
			   
print helo.name + ' has ' + str(helo.num_superior_ranks) + ' ranks ahead'	
	
helo.rank = 'private'

print helo.rank
	
william = Admiral(name='Adama', gender = 'm', num_subordinates=100)		
print william._Admiral__InitiateNuclearStrike('Cylon Baseship')

sharon = Cylon(name='sharon',
				model_number=8,
				body_number=3)
				
hera = HybridBeing( name = 'Hera',
				    gender = 'f',
					human_parent= helo, cylon_parent=sharon)
	
					
print hera.body_number

print hera.ThankHeavens()

print hera.Resurrect()
