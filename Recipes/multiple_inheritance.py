class Mom:
	
	def talk(self):
		print "Mom talking"
	def walk(self):
		print "Mom walking"
	def work(self):
		print "Dr."	
	def __del__(self):
		print "Mom's destructor"

class Dad:
	def __init__(self):
		print "Dad is born"
	def talf(self):
		print "Dad taling"
	def walk(self):
		print "Dad walkina"
		
		
class Infant(Dad,Mom):
	def talk(self):
		print "infant talking"
	def walk(self):
		print "Infant Crawling"
	def work(self):
		Mom.work(self)
		print "Ortho"
	
	
	
child=Infant()
child.walk()
child.talk()
child.work()