'''
******************************************** 
Code challenge from Thumbtack 
Implement an in-memory tables
********************************************
'''
import sys

class SimpleDatabase: 

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
			if self.tables[name] not in self.count:
				self.count[self.tables[name]] = 0
			else: 
				self.count[self.tables[name]] += 1

			# delete the recent transaction
			self.transaction.pop(0)

	# Close all transaction blocks
	# Set the transaction to an empty list
	def COMMIT(self):
		self.transaction = []

# Testing starts here 
if __name__ == "__main__":

	data = SimpleDatabase()
	#cmd = sys.stdin.readline()

	print 'Welcome to Julia\'s SimpleDatabase'
	
	while True:
		f = raw_input('>>> Enter your command: ') 
		cmd = f.split()

		if cmd[0] == 'SET':
			data.SET(cmd[1],str(cmd[2]))
		elif cmd[0] == 'GET':
			data.GET(cmd[1])
		elif cmd[0] == 'UNSET': 
			data.UNSET(cmd[1])
		elif cmd[0] == 'END': 
			data.END()
		elif cmd[0] == 'NUMEQUALTO': 
			data.NUMEQUALTO(cmd[1])
		elif cmd[0] == 'BEGIN': 
			data.BEGIN()
		elif cmd[0] == 'ROLLBACK': 
			data.ROLLBACK()
		elif cmd[0] == 'COMMIT': 
			data.COMMIT()
		else: 
			print 'Invalid Command'

##### Instructions for compiling from the command line #####
# Find the right directory, enter: python simpleDatabse.py 
# Enter one command per line 
# See the attached txt files for command examples 
# Enjoy! :)  

