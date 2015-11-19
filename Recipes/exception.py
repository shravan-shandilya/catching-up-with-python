num=1
import sys
while num!= -1:
	try:
		num=int(raw_input("Enter a number"))
		if num==999:
			sys.exit()
		print num
	except SystemError:
		print "Syntax is wrong"
	except ValueError,detail:
		print "Hahahaha",detail
	
	except EOFError:
		print "Hahahaha"
		
	except SystemExit,detail:
		print "Hahahaha",detail
	else:
		print "In else"
	finally:
		print "Go to hell"
		exit(0)