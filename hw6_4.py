# i2p - Homework - 6; Challenging Version
# By: Roopa Prakash, submitted on: 06/08/2016

class SuperString(object):
	def __init__(self, str):
		self.baseString = ''
		self.vowels = 0
		
		self.baseString = str.strip()
		for char in self.baseString:
			if char in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
				self.vowels += 1
				
		
	def Replacer(self, str1, str2):
		index = 0
		newStr = self.baseString
		if str1 == str2:
			return newStr
		else:
			while(str1 in newStr):
				index = newStr.find(str1)
				newStr = newStr[0:index]+ str2 + newStr[index+len(str1):]	
		return newStr
		
	
	def Splitter(self, seperator):
		return_list = []
		index = 0
		str = self.baseString
		
		if str == '' or str == None:
			return ['']
		elif seperator == '' or seperator == 'None':
			print '\n Invalid seperator '
			return ['']
		
		while (seperator in str):
			index = str.find(seperator)
			return_list.append(str[0:index])
			str = str[index+ len(seperator):]
			
		index = len(str)	
		return_list.append(str[0:index])
		return return_list
			
			

my_super = SuperString('albert,salbUwei,hwang')

print 'Total Vowels ' + str(my_super.vowels)
print my_super.Replacer('a', 'E')
print my_super.Replacer('lb', 'YX')
print my_super.Splitter(',')
print my_super.Splitter('lb')

print '\nTesting Overlapping Patterns'
new_super = SuperString('teee')
print new_super.Replacer('ee', 'me')

