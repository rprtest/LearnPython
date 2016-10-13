# i2p - Homework - 6; Challenging Version
# By: Roopa Prakash, submitted on: 06/08/2016

# Part 3
class CashRegister(object):
	def __init__(self, Name):
		self.name = Name
		self.total_cash = 0
		self.last_transaction_amt = 0
		self.total_number_transactions = 0
		
	def Transact(self, amount):
		self.last_transaction_amt = amount
		self.total_cash += amount
		self.total_number_transactions += 1
		
	def MakeChange(self, num):
		self.total_number_transactions += num
	
	def EmptyOut(self):
		self.total_cash = 0
	
	def ShowLastTransaction(self):
		print 'Last Transaction amount: ' + str(self.last_transaction_amt)
		
	def ClearHistory(self):
		self.total_number_transactions = 0
		

		
		
# Object 1 of CashRegister class
print '\nTest Object 1 ...'
register1 = CashRegister('Register1')

# Add Money
register1.Transact(100)
print '\nAfter Transaction number: ' + str(register1.total_number_transactions)
print 'Register:  ' + register1.name + ' has total cash: ' + str(register1.total_cash)
register1.ShowLastTransaction()

# Add Money
register1.Transact(50)
print '\nAfter Transaction number: ' + str(register1.total_number_transactions)
print 'Register:  ' + register1.name + ' has total cash: ' + str(register1.total_cash)
register1.ShowLastTransaction()

# Clear History
register1.ClearHistory()
print '\nAfter Clear History, Number of transactions: ' + str(register1.total_number_transactions)
print 'Register:  ' + register1.name + ' has total cash: ' + str(register1.total_cash)
register1.ShowLastTransaction()

# Make Change
register1.MakeChange(2)
print '\nAfter Make Change, Number of transactions: ' + str(register1.total_number_transactions)
print 'Register:  ' + register1.name + ' has total cash: ' + str(register1.total_cash)
register1.ShowLastTransaction()


#Empty Out
register1.EmptyOut()
print '\nAfter Empty Out, Number of transactions: ' + str(register1.total_number_transactions)
print 'Register:  ' + register1.name + ' has total cash: ' + str(register1.total_cash)
register1.ShowLastTransaction()


# Object 2 of CashRegister class
print '\nTest Object 2 .....'
register2 = CashRegister('Register2')
# Add Money
register2.Transact(60)
print '\nAfter Transaction number: ' + str(register2.total_number_transactions)
print 'Register:  ' + register2.name + ' has total cash: ' + str(register2.total_cash)
register2.ShowLastTransaction()

# Clear History
register2.ClearHistory()
print '\nAfter Clear History, Number of transactions: ' + str(register2.total_number_transactions)
print 'Register:  ' + register2.name + ' has total cash: ' + str(register2.total_cash)
register2.ShowLastTransaction()

# Make Change
register2.MakeChange(1)
print '\nAfter Make Change, Number of transactions: ' + str(register2.total_number_transactions)
print 'Register:  ' + register2.name + ' has total cash: ' + str(register2.total_cash)
register2.ShowLastTransaction()


#Empty Out
register2.EmptyOut()
print '\nAfter Empty Out, Number of transactions: ' + str(register2.total_number_transactions)
print 'Register:  ' + register2.name + ' has total cash: ' + str(register2.total_cash)
register2.ShowLastTransaction()