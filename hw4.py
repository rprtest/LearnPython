# i2p - Homework - 4
# By: Roopa Prakash, submitted on: 05/09/2016


# Section 1
print 'Section 1\n'
list_of_names = ['albert', 'angela', 'leo', 'bridget']
print list_of_names

position = 0
for name in list_of_names:
	new_name = ''
	for char in name:
	   if char != 'a':
		new_name = new_name + char.upper()
	   else:
		new_name = new_name + char
	list_of_names[position] = new_name
	position += 1
print list_of_names

last_names = [ 'hwang', 'ellington', 'chau', 'campbell']
position = 0
for name in last_names:
	list_of_names[position] = list_of_names[position] + ' ' + name
	position += 1
print list_of_names
		
dict_of_names = {}
position = 0
for name in list_of_names:
	key = name.replace(' ','').lower()
	dict_of_names[key] = name
	position += 1

# printing the entire dictionary
print dict_of_names

# printing some values from dictionary
print dict_of_names['alberthwang']
print dict_of_names['bridgetcampbell']
print ''


# Section 2
print '\nSection 2 \n'
data = []
summary = {}
sum = 0
max_int = 0
max_odd_int = 0

total_ints = int(raw_input('Total integers in data: '))

for count in range(0, total_ints):
	data.append(int(raw_input('Enter an integer: ')))

for num in data:
	sum += num
	
	if num > max_int:
		max_int = num
		
	if( num % 2 != 0):
		if num > max_odd_int:
			max_odd_int = num
			
summary['sum'] = sum
summary['max'] = max_int
summary['max_odd'] = max_odd_int

print 'The sum of all the data is: ' + str(summary['sum'])
print 'The max int is: ' + str(summary['max'])
print 'The max odd int is: ' + str(summary['max_odd'])
print ''


# Section 3
print '\nSection 3 \n'
def ConvertToFeet(yards):
    return str(yards * 3) + ' feet'

	
distances = [1, 2, 10, 32, 56, 111, 100]
for position in range(0, len(distances), 1):
	distances[position] = ConvertToFeet(distances[position])	
print distances



	
