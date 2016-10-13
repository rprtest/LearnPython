# i2p - Homework - 2
# By: Roopa Prakash, submitted on: 04/25/2016


## Section 1
print 'Section 1'

org_str = "sUpERcaLaFragaliSticeXPialaDoshuS"

# convert to lowercase
lower_str =  org_str.lower()
print lower_str

# convert to uppercase
upper_str = org_str.upper()
print upper_str

# replace
new_str = org_str.replace('sUpER', 'sooopaaar')
print new_str

# substring using range
sub_str = org_str[5:20]
print sub_str


## Section 2
print '\nSection 2'
count = 99
str1 = ' bottles of beer on the wall, '
str2 = ' bottles of beer...\ntake 1 out, pass it around, '
str3 = '.'

while (count >= 95):
	print str(count) + str1 + str(count) + str2 + str(count-1) + str1[:-2] + str3
	count -= 1

	
## Section 3
print '\nSection 3'
user_input = raw_input('Enter an integer: ')
remainder = int(user_input)% 3
print 'If you divide ' + str(user_input) + ' by ' + str(3) + ', the remainder is ' + str(remainder) + '!'