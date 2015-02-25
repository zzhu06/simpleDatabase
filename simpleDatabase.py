'''
******************************************** 
Code challenge from Thumbtack 
Implement an in-memory database
********************************************
'''

# original version: simple and clean code but has linear time in NUMEQUALTO

# remaining problem: stdin; shell; EOF

class SimpleDatabase: 

	# Initialize the database 
	def __init__(self):
		# store paris of names and values 
		# store list of historial trasactions 
		self.tables = {}
		self.transaction = []

	# Set the variable name to the value
	def SET(self, name, value):  
		# record the most RECENT value of the name 
		# this is for convinience of the ROLLBACK function
		if self.transaction:
			if name not in self.tables: 
				self.transaction[0][name] = 'NULL'
			else: 
				self.transaction[0][name] = self.tables[name]

		self.tables[name] = value 

	# Get the value of the name
	def GET(self, name):
		if name not in self.tables:
			print 'NULL'
		else: 
			print self.tables[name]

	# Unset the name 
	def UNSET(self, name):
		# change the historial value when unset  
		if self.transaction:
			self.transaction[0][name] = self.tables[name]

		self.tables[name] = 'NULL'

	# Exit the program
	def END(self):
		exit()

	# Count the number of variables
	# Linear time; can improve by using extra space 
	def NUMEQUALTO(self, value):
		count = 0 
		for i in self.tables.values(): 
			if i == value: 
				count += 1 
		print count 

	# Open a new transaction block 
	def BEGIN(self):
		self.transaction.insert(0,{})

	# Undo all of the commands in the recent transaction 
	def ROLLBACK(self):
		if self.transaction == []:
			print 'NO transaction'
		else: 
			# reset the value of the name in tables
			for name in self.transaction[0]: 
				self.tables[name] = self.transaction[0][name]
			# delete the recent transaction
			self.transaction.pop(0)

	# Close all transaction blocks
	# Set the transaction to an empty list
	def COMMIT(self):
		self.transaction = []
	
# Test cases 
if __name__ == "__main__":
	'''
	#Ex. 5
	data = SimpleDatabase()
	data.SET('a',10)
	data.BEGIN()
	data.NUMEQUALTO(10)
	data.UNSET('a')
	data.NUMEQUALTO(10)
	data.ROLLBACK()
	data.NUMEQUALTO(10)
	data.COMMIT()
	data.END()
	
	# Ex. 4
	data = SimpleDatabase()
	data.SET('a',50)
	data.BEGIN()
	data.GET('a') 
	data.SET('a',60)
	data.BEGIN()
	data.UNSET('a')
	data.GET('a') 
	data.ROLLBACK()
	data.GET('a')
	data.COMMIT()
	data.GET('a') 
	data.END()

	
	# Ex. 3
	data = SimpleDatabase()
	data.BEGIN()
	data.SET('a',30)
	data.BEGIN()
	data.SET('a',40)
	data.COMMIT()
	data.GET('a') 
	data.ROLLBACK()
	data.END()

	
	# Ex. 2
	data = SimpleDatabase()
	data.BEGIN()
	data.SET('a',10)
	data.GET('a')
	data.BEGIN()
	data.SET('a',20)
	data.GET('a') 
	data.ROLLBACK()
	data.GET('a')
	data.ROLLBACK()
	data.GET('a')
	data.END()

	
	# Ex. 1
	data = SimpleDatabase()
	data.SET('a',10)
	data.SET('b',10)
	data.NUMEQUALTO(10)
	data.NUMEQUALTO(20)
	data.SET('b',30)
	data.NUMEQUALTO(10)
	data.END()


	# Ex. 0
	data = SimpleDatabase()
	data.SET('a',10)
	data.GET('a')
	data.UNSET('a')
	data.GET('a')
	data.END()
	'''
	
