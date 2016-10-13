# i2p - Homework - 5 ; Very Challenging version
# By: Roopa Prakash, submitted on: 05/17/2016


# Part 2 - Sort function
input_data = []
total_ints = 0

''' Sub routine to sort a list '''
def sort_list():
	not_sorted = True
	while not_sorted:
		swap_counter = 0
		for index in range(len(input_data) - 1):
			if input_data[index] > input_data[index + 1]:
				input_data[index], input_data[index + 1] = input_data[index + 1], input_data[index]
				swap_counter += 1
		if swap_counter == 0:
			not_sorted = False				
	print input_data
	print ''

# Take user input to fill the data list of integers
while True:
	total_ints = int(raw_input('Total integers in data: '))
	if total_ints <= 0:
		print 'Invalid entry. Please enter a positive integer' 
	else:
		break		
for count in range(total_ints):
	input_data.append(int(raw_input('Enter an integer: ')))

# calling the sort function to sort the list	
sort_list()




# Part 3 - Printing a data matrix as a table
data1 = [[1,2,3,78],[4,5,6,42],[7,8,9,90]]
data2 = [['albert','tom','sarahughes'],['abe','abrahamlincoln', 'ac'],['this is a random string', 'john','todd'],['yu','chen','cheng']]
data3 = [[1,5],['albert','hwang'],[79,'seventy-nine']]


''' Sub routine to print a data list as a table '''
def CreateTable(data):
	number_of_rows = len(data)
	number_of_columns = len(data[0])
	# list to store max data with in each column
	col_max_width = []
	
	# iterate over the input data matrix, find the max width of data in each column and store it in list col_max_width[]
	for column_index in range(0, number_of_columns):
		max_width = 0
		for row_index in range(0, number_of_rows):
			if len(str(data[row_index][column_index])) > max_width:
				max_width = len(str(data[row_index][column_index]))
		col_max_width.append(max_width)
	
	# print the top line
	data_width = 0
	total_width = 0
	for width in col_max_width:
		data_width += width
	padding = number_of_columns * 4
	separator = number_of_columns - 1
	total_width = data_width + padding + separator
	print '+' + '=' * total_width + '+'
	
	# print each row and the line below it
	for row_index in range(0,number_of_rows):
		row_output = '|'
		row_separator = '|'
		trailing_space = 0
		
		#form the row to print in a string
		for col_index in range(0, number_of_columns):
			trailing_space = col_max_width[col_index] - len(str(data[row_index][col_index])) + 2
			row_output += ' ' * 2 + str(data[row_index][col_index])+ ' ' * trailing_space + '|'			
			
			# form the line that separates 2 rows; adding the last char '|' or '+' depending on if it is last column
			if(col_index == number_of_columns - 1):
				row_separator += '=' * 2 + '=' * len(str(data[row_index][col_index]))+ '='* trailing_space + '|'
			else:
				row_separator += '=' * 2 + '=' * len(str(data[row_index][col_index]))+ '='* trailing_space + '+' 
		
		# print row of data		
		print row_output
		
		# check if it last row to update the row_separator accordingly
		if(row_index == number_of_rows - 1):
			row_separator = row_separator.replace('+', '=')
			row_separator = row_separator.replace('|', '+') 
		print row_separator
	
# Calling the CreateTable function with data to print	
CreateTable(data1)
print ''
CreateTable(data2)
print ''
CreateTable(data3)
print ''