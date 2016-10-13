# i2p - Homework - 8; Modules - Part 1
# By: Roopa Prakash, submitted on: 06/23/2016

from animals import Dog, Labrador

def main():
	my_dog = Dog.Dog('Dog 1', 'small')
	my_lab = Labrador.Labrador('Dog 2', 'medium')
	
	print my_dog.Bark()
	print my_dog.Greet()
	
	print my_lab.Bark()
	print my_lab.Greet()
	
if __name__ == '__main__':
	main()