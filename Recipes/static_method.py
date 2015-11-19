class People():
	people=None
	
	@staticmethod
	def getInstance():
		if People.people == None:
			People.people=People(); 
		return People.people
	
p1=People.getInstance()
p2=People.getInstance()

if id(p1)==id(p2):
	print "Singleton working"
else:
	print "something went wrong"