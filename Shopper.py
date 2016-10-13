# i2p - Homework - 8; Modules - Part 3
# By: Roopa Prakash, submitted on: 06/23/2016
import datetime

def main():
	shopping_cart = []
	
	# Prompt user for groceries
	count = 2
	while (count > 0):
		item = raw_input('Add item: ')
		count -= 1
		shopping_cart.append(item)
	
	item_checklist = ['wine', 'beer', 'liqour']
	items_count = 0
	shopping_cart_length = len(shopping_cart) - 1
	
	while items_count <= shopping_cart_length:
		if shopping_cart[items_count] in item_checklist:
			user_input = raw_input('Enter you birthday in mm/dd/yyyy format: ')
			birthday = datetime.datetime.strptime(user_input,'%m/%d/%Y')
			today = datetime.datetime.now()
			date_diff = today - birthday
			days = int(date_diff.days)
			if days >= 21 * 365:
				print 'Thanks and Enjoy!'
				items_count += 1
			else:
				print 'You are too young son!'
				shopping_cart.remove(shopping_cart[items_count])
				shopping_cart_length -= 1
		else:
			items_count += 1
	print shopping_cart
				
if __name__ == '__main__':
	main()
	
