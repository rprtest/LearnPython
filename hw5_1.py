# i2p - Homework - 5; In class exercises
# By: Roopa Prakash, submitted on: 05/14/2016

# 1
my_list = range(1,11)
for index, item in enumerate(my_list):
	my_list[index] = item + 2
print my_list
print ''


# 2
my_dict = { 'bugs': 'rabbit',
            'elmer': 'human',
			'wiley': 'coyote',
			'tom': 'cat',
			'jerry': 'mouse'}
			
activity_list = {'bugs':'hops', 'elmer':'walks', 'wiley':'walks', 'tom':'schemes', 'jerry':'scampers'}
for cartoon, animal in my_dict.iteritems():
	print cartoon + ' the '+ animal + ' ' + activity_list[cartoon]
print ''


# 3
my_string = '1,55,6,89,2|7,29,44,5,8|767,822,999'
my_data =[]
for split_str in my_string.split('|'):
	my_data.append(split_str.split(','))
print my_data[1][2]
print ''


# 4
org_str = 'alberthwang-90,80,70,50|smadaan-99,80,70,90|satishm-90,90,90,90'
test_scores = {}
for item in org_str.split('|'):
	key_val = item.split('-')
	test_scores[key_val[0]] = key_val[1].split(',') 
print test_scores['smadaan'][2]
print ''


# 5
num_list = [5.2, 5.6, 5.1, 5.8, 5.9]
def rounding(number):
	if number > 6 or number < 5:
		return number
	elif number < 5.5:
		return 5
	else:
		return 6 
		
num_list = map(rounding, num_list)
print num_list
print ''


# 6
str_list = [ 'that is the best','that\'s the type of pencil you use in the SAT','that rhymes with \'me\'','i want some more','like a high-five!','what a neat trick...']
for index, add_str in enumerate(str_list):
	print 'the number is ' + str(index + 1) + ', '+ add_str
print ''


# 7
given_string = 'ldap:alberthwang,eeid:67739|ldap:meng,eeid:107,building:CL5'
key_val = []
employees = []

for item in given_string.split('|'):
	my_dict = {}	
	for key_str in item.split(','):
		key_val = key_str.split(':')
		my_dict[key_val[0]] = key_val[1]
		
	employees.append(my_dict)
print employees[1]['building']
print ''