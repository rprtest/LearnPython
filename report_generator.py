# i2p - Homework - 9 - File Manipulations and Exceptions
# By: Roopa Prakash, submitted on: 07/04/2016

import csv
from datetime import date

def main():
	# Sets to store unique values of oc member, region and office
	data_oc_member = set()
	data_region = set()
	data_office = set()
	
	# Open the contributions.csv and read it
	data_file = open('contributions.csv', 'rU')
	reader = csv.reader(data_file)
	
	# list to store all rows in the contributions.csv
	all_data = []
	
	# store each row in file into all_data list, store unique values in region, oc member and office in sets 
	for row in reader:
		all_data.append(row)
		if row[1] != 'OC_MEMBER':
			data_oc_member.add(row[1])
		if row[2] != 'REGION':
			data_region.add(row[2])
		if row[3] != 'OFFICE':
			data_office.add(row[3])
	
	# close the data file after reading and storing
	data_file.close()
	
	# Milestone 1 and 2 - print number of unique values and the sorted values themselves
	print 'Number of unique values in REGION: ' + str(len(data_region))
	s = ', '
	print s.join(sorted(data_region))
	print ''
	
	print 'Number of unique values in OC_MEMBER: ' + str(len(data_oc_member))
	print s.join(sorted(data_oc_member))
	print ''
	
	print 'Number of unique values in OFFICE: ' + str(len(data_office))
	print s.join(sorted(data_office))
	print ''
	
	# Milestone 3 and 4; list to store data to be written in results.csv
	write_data = []
	
	# For each item in unique set of data_oc_member get the num_contrib, mean_contrib
	for item in data_oc_member:
		num_contrib = 0
		mean_contrib = 0.0
		for row in all_data:	
			if item == row[1]:
				num_contrib += 1
				mean_contrib = mean_contrib + float(row[4]) / num_contrib			
		print 'OC Member: ' + str(item)
		print 'Num Contributions: ' + str(num_contrib)
		print 'Mean Contribution: ' + str(mean_contrib)
		print ''
		
		# appending the oc roll up calculation in write_data along with today's date
		write_data.append([item, num_contrib, mean_contrib, date.today().strftime('%m/%d/%Y')])
	
	# Sort write_data and write it to results.csv
	write_data = sorted(write_data)
	write_data.insert(0, ['oc_member', 'num_contribs', 'mean_contribs', 'date'])
	
	write_data_file = open('results.csv', 'w')
	writer = csv.writer(write_data_file)
	writer.writerows(write_data)
	write_data_file.close()
	
	
	
if __name__ == '__main__':
	main()
	
	
	
