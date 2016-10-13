# i2p - Homework - 5 ; Regular version
# By: Roopa Prakash, submitted on: 05/17/2016


# Part 2
# List that stores each employee info as a dictionary
employees = []

# Ask user to input 3 employee records
for count in range(3):
	# dictionary record for each employee info
	employee_dict = {}
	employee_dict['ldap'] = raw_input('ldap: ')
	employee_dict['name'] = raw_input('name: ')
	employee_dict['title'] = raw_input('title: ')
	# Append the dictionary record to employees list
	employees.append(employee_dict)
	print ''

print 'Here are the Employee Records! \n'
for count in range(3):
	print 'Employee Number - ' + str(count)
	print employees[count]['name'] + '\'s ' + 'LDAP is ' + employees[count]['ldap'] + ' and he/she is a ' + employees[count]['title'] + '\n'
	
