#! /usr/bin/python
a,b,c,d,e=10,20,30,40,50
def funcA():
	a,b,c,d=100,200,300,400
	print "In A", a, b, c, d, e
	def funcB():
		a,b,c=1000,2000,3000
		print "In B", a, b, c, d, e
		def funcC():
			a,b=10000,20000
			print "In C", a, b, c, d, e
		funcC()
	funcB()
funcA()
print "Global", a,b,c,d,e