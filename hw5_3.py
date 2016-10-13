# i2p - Homework - 5 ; Challenging version
# By: Roopa Prakash, submitted on: 05/17/2016


# Part 2
# Employees dictionary
employees = {}

# Maximum number of records that can be stored in employees dictionary
max_employee_records = 5

''' Sub routine to add a record to the employees dictionary'''
def add_employee_record():
	employee_dict = {}
	employee_key = '' 
	print ''
	employee_key = raw_input('Employee LDAP: ')
	employee_dict['name'] = raw_input('Employee Name: ')
	employee_dict['title'] = raw_input('Employee Title: ')
	for existing_key in employees:
		if employee_key == existing_key:
			print employee_key + ' already has a record! \n'
			return
	employees[employee_key] = employee_dict
	print employee_key + ' has been added successfully! \n'
	
	
''' Sub routine to display all records in the employee dictionary'''
def display_employees_records():
	print '\nHere are the Employee Records! \n'
	for key_value in employees:
		print key_value + '\'s name is \'' + employees[key_value]['name'] + '\' and he/she is a ' + employees[key_value]['title']
	
	
	
''' Loop to take user input - Add/ Quit 
- calls add_employee_record or display_employees_records depending on user_choice
- quits with calling display_employees_records if max_employee_records have been added in the dictionary'''
while (len(employees) < max_employee_records):
	user_choice = raw_input('Add/ Quit - ')
	if user_choice.lower() == 'add':
		add_employee_record()
	elif user_choice.lower() == 'quit':
		break

display_employees_records()	
print ''



# Part 3 - Sort Function
data = []
total_ints = 0

def sort_list():
	not_sorted = True
	while not_sorted:
		swap_counter = 0
		for index in range(len(data) - 1):
			if data[index] > data[index + 1]:
				data[index], data[index + 1] = data[index + 1], data[index]
				swap_counter += 1
		if swap_counter == 0:
			not_sorted = False
				
	print data		


# Taking user input to create the data list of integers to sort	
while True:
	total_ints = int(raw_input('Total integers in data: '))
	if total_ints <= 0:
		print 'Invalid entry. Please enter a positive integer' 
	else:
		break
for count in range(total_ints):
	data.append(int(raw_input('Enter an integer: ')))

# calling the function to sort 	
sort_list()
	

