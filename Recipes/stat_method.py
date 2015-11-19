class Mom:
	mom=None
	@staticmethod
	def call():
		global mom
		if mom is None:
			return Mom()
		else:
			return mom
	def walk(self):
		print "walking"
	def talk(self):
		print "talking"
		
mom=Mom.call()