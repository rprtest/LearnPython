# i2p - Homework - 8; Modules - Part 4
# By: Roopa Prakash, submitted on: 06/23/2016

def main():
	numlist = []
	layers = int(raw_input("Enter number of layers: "))
	count = 0
	addrow = []
	while (count < layers):
		if count == 0:
			addrow = []
			addrow.append(1)
			numlist.append(addrow)
			count = count+1
		elif count >= 1:
			addrow = []
			for index, num in enumerate(numlist[count-1]):
				if index == 0:
					addrow.append(1)
				elif index <= len(numlist[count-1]):
					addrow.append(num + numlist[count-1][index-1])
			addrow.append(1)
			numlist.append(addrow)
			count = count +1	
			
	for row in numlist:
		output = ' '.join(str(n) for n in row)
		print output
		
		


if __name__ == '__main__':
	main()