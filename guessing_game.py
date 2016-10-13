# i2p - Homework - 8; Modules - Part 2
# By: Roopa Prakash, submitted on: 06/23/2016
import random

def main():
	while(True):
		lowest = int(raw_input('Enter the lower limit: '))
		highest = int(raw_input('Enter the upper limit: '))
	
		if (lowest > highest):
			print 'Try again'
		else:
			break
	
	# Generate random int within lower and upper limit
	my_int = random.randint(lowest,highest)
	count = 5
	while (count > 0):
		user_guess = int(raw_input('Guess the random number:'))
		if user_guess == my_int:
			print 'CONGRATULATIONS! THE NUMBER WAS ' + str(my_int) + '!'
			break
		count -= 1
	if count == 0:
		print 'WA.. WAAA ..THE NUMBER WAS ' + str(my_int) + '!' 
	


if __name__ == '__main__':
	main()