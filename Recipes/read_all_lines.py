import sys
file=open(sys.argv[0])
num=1
for line in file.readlines():
	print num,".",line,
	num+=1