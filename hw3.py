# i2p - Homework - 3
# By: Roopa Prakash, submitted on: 05/01/2016

# Section 1
str_count = 0
start_str = "the number is "
first_str = "that is the best"
second_str = "that\'s the type of pencil you use in the SAT"
third_str = "that rhymes with \'me\'"
fourth_str = "i want some more"
fifth_str = "like a high-five!"
sixth_str = "what a neat trick..."

while str_count < 6:
	str_count += 1
	if str_count == 1:
		print start_str + str(str_count) + ', ' +  first_str
	elif str_count == 2:
		print start_str + str(str_count) + ', ' +  second_str
	elif str_count == 3:
		print start_str + str(str_count) + ', ' +  third_str
	elif str_count == 4:
		print start_str + str(str_count) + ', ' +  fourth_str
	elif str_count == 5:
		print start_str + str(str_count) + ', ' +  fifth_str
	else:
		print start_str + str(str_count) + ', ' +  sixth_str


# Section 2
num_bottles = 99
bottles_str = "\nX bottles of beer on the wall, X bottles of beer..."
take_str = "take 1 out, pass it around, Y bottles of beer on the wall."
even_str = "YAY...even number of bottles!"
even_str_92 = "NINETY TWO IS LUCKY!"
exit_str = "\noh man, I really can\'t have any more!"

while (num_bottles >= 0):
	print bottles_str.replace('X', str(num_bottles))
	print take_str.replace('Y', str(num_bottles - 1))
	num_bottles -= 1
	if (num_bottles % 2) == 0:
		if num_bottles == 92:
			print even_str_92
		else:
			print even_str
			if num_bottles == 84:
				print exit_str
				break	