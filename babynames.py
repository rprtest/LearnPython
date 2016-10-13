# i2p - Homework - 10 - HW10 - Web Scraping & Regex
# By: Roopa Prakash, submitted on: 07/21/2016

import sys
import re
import urllib

# Get User Input for start and end year
def GetYear(str):
	for try_num in range(4):
		try:
			year = int(raw_input(str))	
			break
		except ValueError:
			if try_num == 3:
				sys.exit('exiting script - invalid int input')
			else:
				print 'invalid int format - try again.'
	return year
	
	
	
# Get the decades between start and end year
def GetDecades(start_year, end_year):
	decades = []	
	year = start_year
	
	# validation to make sure start and end year is 4 digit and end year is after start yr
	if len(str(start_year)) != 4 or len(str(end_year)) != 4 or end_year < start_year:
		sys.exit('exiting script - Invalid input / No data available for these years')
		
	while year < end_year:
		if (year % 10 == 0):
			decades.append(year)
			year += 10
		else:
			year += 1
	return decades
	

# Getting the text data for each baby url
def UrlToText(url):
	url_obj = urllib.urlopen(url)
	txt = url_obj.read()
	return txt
	
	
def main():
	# Get the start and end year
	start_year = GetYear('start_year: ')
	end_year = GetYear('end_year: ')

	# Get the decade list between start and end
	decade_list = []
	decade_list = GetDecades(start_year, end_year)

	# For each decade, get the url
	babyname_url_list = []
	for decade in decade_list:
		if (decade >= 1880 and decade < 2010):
			babyname_url = 'http://ssa.gov/OACT/babynames/decades/names' + str(decade) + 's.html'
			babyname_url_list.append(babyname_url)
		
	# For each url, open the url and read the data
	male_births = 0
	female_births = 0
	top_names = {}

	for link in babyname_url_list:
		babydata = UrlToText(link)
	
		# Get total Male_Births
		male_birth_pattern = r'includes\s([0-9,]+)\smale'
		male_num = re.search(male_birth_pattern, babydata)
		male_births += int(male_num.group(1).replace(',', ''))
	
		# Get total Female_Births
		female_birth_pattern = r'([0-9,]+)\sfemale\sbirths'
		female_num = re.search(female_birth_pattern, babydata)	
		female_births += int(female_num.group(1).replace(',',''))
	
		#Find Most Popular Names and their numbers in a decade
		list = re.search(r'<td align="center">(.+)', babydata)
		
		pop_names = re.findall(r'<td align="center">(\w+)</td>', list.group(0))
		pop_numbers = re.findall(r'<td>([0-9,]+)</td>', list.group(0))
	
	
		# Add these to the dictionary data storing popular name and value
		for index, name in enumerate(pop_names):
			if name in top_names:
				top_names[name] += int(pop_numbers[index].replace(',',''))
			else:
				top_names[name] = int(pop_numbers[index].replace(',',''))
	
	# Print all the extracted data
	print ''	
	print 'In the full decades between ' + str(start_year) + ' and ' + str(end_year)
	print 'Male Births: ' + str(male_births)
	print 'Female Births: ' + str(female_births)	
	
	# Find most popular name and value in top_names dictionary and print it
	max_val = 0
	max_name = ''
	for name in top_names:
		if top_names[name] > max_val:
			max_val = top_names[name]
			max_name = name
	print 'Most popular name: ' + max_name + ' (' + str(max_val) + ')'
	
	
if __name__ == '__main__':
	main()
	
	


