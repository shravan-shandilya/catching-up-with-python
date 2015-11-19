class Friend:
	
	def walk(self,shravan=""):
		'''
		>>> Friend().walk()
		walking
		'''
		print "walking",
		
	def talk(self):
		print "talking",
		
	def fight(self):
		print "fighting",
		
f1=Friend()
f1.walk()

import doctest
doctest.testmod()