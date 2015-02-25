
#stdin; shell
#EOF

# Questions  for engineer: extra space for counting? 

class SimpleDatabase: 

	def __init__(self):
		# database has the current value of names 
		# history records the value of name from last time 
		self.database = {}
		self.history = []
		self.count = {}

	def SET(self, name, value): 
		if self.history:
			if name not in self.database: 
				self.history[0][name] = 'NULL'
			else: 
				self.history[0][name] = self.database[name]


		if value not in self.count.keys(): 
			self.count[value] = 1 
		else: 
			self.count[value] += 1 

		if name in self.database: 
			self.count[self.database[name]] -= 1

		self.database[name] = value 
		

	def GET(self, name):
		if name not in self.database:
			print 'NULL'
		else: 
			print self.database[name]

	def UNSET(self, name):
		# if inside of a history, record the value befroe unset
		if self.history:
			self.history[0][name] = self.database[name]

		self.count[self.database[name]] -= 1 

		self.database[name] = 'NULL'

	# How to test the end of the program; import sys; sys.exit()
	def END(self):
		exit()

	# Improve to Log(N) worst time; Sorting and binary search?  
	def NUMEQUALTO(self, value):
		if value not in self.count:
			print 0 
		else: 
			print self.count[value]

	# BEGIN a new history
	def BEGIN(self):
		self.history.insert(0,{})

	def ROLLBACK(self):
		if self.history == []:
			print 'NO history'
		else: 
			for name in self.history[0]: 
				self.database[name] = self.history[0][name]

			self.count[self.database[name]] += 1

			self.history.pop(0)

	def COMMIT(self):
		self.history = []

	# Part II: history block? 	

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
	
