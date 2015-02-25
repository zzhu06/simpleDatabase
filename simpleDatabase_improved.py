'''
******************************************** 
Code challenge from Thumbtack 
Implement an in-memory tables
********************************************
'''

# Improved version: Log(N) time for worst case, but cuased more lines and extra space 

# remaining problem: stdin; shell; EOF

# Questions  for engineer: extra space for counting? 

class Simpletables: 

	# Initialize the database 
	def __init__(self):
		# table stores paris of names and values 
		# transaction stores list of historial trasactions 
		# count stores count of values 
		self.tables = {}
		self.transaction = []
		self.count = {}

	# Set the variable name to the value
	def SET(self, name, value): 
		# record the most RECENT value of the name 
		# this is for convinience of the ROLLBACK function
		if self.transaction:
			if name not in self.tables: 
				self.transaction[0][name] = 'NULL'
			else: 
				self.transaction[0][name] = self.tables[name]

		# change the counting number in count 
		if value not in self.count.keys(): 
			self.count[value] = 1 
		else: 
			self.count[value] += 1 

		if name in self.tables: 
			self.count[self.tables[name]] -= 1

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

		# change the counting number when unset 
		self.count[self.tables[name]] -= 1 

		# set the value of the name to NULL
		self.tables[name] = 'NULL'

	# Exit the program
	def END(self):
		exit()

	# Count the number of variables
	# Log(N) time but use extra space 
	# Suggestion for improving: sorting and binary search?  
	def NUMEQUALTO(self, value):
		if value not in self.count:
			print 0 
		else: 
			print self.count[value]

	# BEGIN a new transaction block 
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

			# change the counting number when Rollback 
			self.count[self.tables[name]] += 1

			# delete the recent transaction
			self.transaction.pop(0)

	# Close all transaction blocks
	# Set the transaction to an empty list
	def COMMIT(self):
		self.transaction = []

# Test cases 
# Need to improve: StdIn 
if __name__ == "__main__":
	'''
	#Ex. 5
	data = Simpletables()
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
	data = Simpletables()
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
	data = Simpletables()
	data.BEGIN()
	data.SET('a',30)
	data.BEGIN()
	data.SET('a',40)
	data.COMMIT()
	data.GET('a') 
	data.ROLLBACK()
	data.END()
	
	# Ex. 2
	data = Simpletables()
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
	data = Simpletables()
	data.SET('a',10)
	data.SET('b',10)
	data.NUMEQUALTO(10)
	data.NUMEQUALTO(20)
	data.SET('b',30)
	data.NUMEQUALTO(10)
	data.END()

	# Ex. 0
	data = Simpletables()
	data.SET('a',10)
	data.GET('a')
	data.UNSET('a')
	data.GET('a')
	data.END()
	'''
	
