
#stdin; shell

class SimpleDatabase: 

	def __init__(self):
		# table has the current value of names 
		# transaction records the value of name from last time 
		self.table = {}
		self.transaction = []

	def SET(self, name, value): 
		if self.transaction:
			if name not in self.table: 
				self.transaction[0][name] = 'NULL'
			else: 
				self.transaction[0][name] = self.table[name]

		self.table[name] = value 

	def GET(self, name):
		if name not in self.table:
			print 'NULL'
		else: 
			print self.table[name]

	def UNSET(self, name):
		# if inside of a transaction, record the value befroe unset
		if self.transaction:
			self.transaction[0][name] = self.table[name]
		self.table[name] = 'NULL'

	# How to test the end of the program; import sys; sys.exit()
	def END(self):
		exit()

	# Improve to Log(N) worst time; Sorting and binary search?  
	def NUMEQUALTO(self, value):
		count = 0 
		for i in self.table.values(): 
			if i == value: 
				count += 1 
		print count 

	# BEGIN a new transaction
	def BEGIN(self):
		self.transaction.insert(0,{})

	def ROLLBACK(self):
		if self.transaction == []:
			print 'NO TRANSACTION'
		else: 
			for name in self.transaction[0]: 
				self.table[name] = self.transaction[0][name]
			self.transaction.pop(0)

	def COMMIT(self):
		self.transaction = []

	# Part II: transaction block? 	

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
	
